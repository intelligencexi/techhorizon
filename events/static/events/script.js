// Redirect to home when the header is clicked
const heading = document.getElementById('tech-horizon');
heading.addEventListener('click', () => {
    window.location.href = '/';
});

// Email form verification
const emailInput = document.querySelector('input[type="email"]');
const errorMessage = document.querySelector('.error-message');

emailInput.addEventListener('invalid', (event) => {
  event.preventDefault(); // Prevents the form from submitting
  errorMessage.style.display = 'block';
});

emailInput.addEventListener('input', () => {
  if (emailInput.validity.valid) {
    errorMessage.style.display = 'none';
  }
});
    // Handle alert messages (pop up, hover, and fade out)
document.addEventListener('DOMContentLoaded', () => {
    const messages = document.querySelectorAll('.messages p'); // Target each message inside .messages
    messages.forEach((message) => {
        // Add a hover effect (optional styling is in CSS)
        message.addEventListener('mouseenter', () => {
            message.style.opacity = 0.9;
        });
        message.addEventListener('mouseleave', () => {
            message.style.opacity = 1;
        });

        // Automatically fade out the message after 5 seconds
        setTimeout(() => {
            message.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            message.style.opacity = 0;
            message.style.transform = 'translateY(-10px)'; // Slide upward
        }, 5000);

        // Remove the message from the DOM after fade-out
        setTimeout(() => {
            message.remove();
        }, 5500);

        // Allow manual dismissal by clicking the message
        message.addEventListener('click', () => {
            message.remove();
        });
    });
});
