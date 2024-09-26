import kue from 'kue';

// Create the queue
const queue = kue.createQueue();

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification with job tracking
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

// Process jobs from 'push_notification_code_2' queue with a concurrency of 2
queue.process('push_notification_code_2', 2, function(job, done) {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

