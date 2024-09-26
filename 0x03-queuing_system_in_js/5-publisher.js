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

// Function to publish messages to the Redis channel
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
}

// Call the function with various messages
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);

