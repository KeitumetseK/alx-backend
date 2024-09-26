import kue from 'kue';

// Create the queue
const queue = kue.createQueue();

// Define the function to send notification
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process the queue for 'push_notification_code'
queue.process('push_notification_code', function(job, done) {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});

