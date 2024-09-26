import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Event when connected to Redis successfully
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event when there's an error connecting to Redis
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Function to set values in a Redis hash
function setHolbertonSchools() {
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

function displayHolbertonSchools() {
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.log(err);
    } else {
      console.log(reply);
    }
  });
}

// Call the functions
setHolbertonSchools();
displayHolbertonSchools();

