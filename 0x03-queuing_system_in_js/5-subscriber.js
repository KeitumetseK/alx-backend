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

// Subscribe to a Redis channel
client.subscribe('holberton school channel');

// Listen for messages on the subscribed channel
client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});

