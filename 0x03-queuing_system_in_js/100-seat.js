import { createClient } from 'redis';
import { promisify } from 'util';
import kue from 'kue';
import express from 'express';

const client = createClient();
client.on('error', (err) => console.log('Redis Client Error', err));

const reserveSeat = (number) => {
  client.set('available_seats', number);
};

const getCurrentAvailableSeats = promisify(client.get).bind(client);

// Initialize seats to 50 on launch
reserveSeat(50);

const queue = kue.createQueue();

const app = express();
const port = 1245;

let reservationEnabled = true;

// GET /available_seats route
app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats });
});

// GET /reserve_seat route
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

// GET /process route
app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const seats = await getCurrentAvailableSeats();
    const availableSeats = parseInt(seats, 10);

    if (availableSeats > 0) {
      reserveSeat(availableSeats - 1);
      if (availableSeats - 1 === 0) {
        reservationEnabled = false;
      }
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
