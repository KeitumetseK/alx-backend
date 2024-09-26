// 1-redis_op.js
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

// Function to set a new school value
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to display school value
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error: ${err.message}`);
      return;
    }
    console.log(reply);
  });
}

// Testing the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

