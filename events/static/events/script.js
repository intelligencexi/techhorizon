// Redirect to home when the header is clicked
const heading = document.getElementById('tech-horizon');
heading.addEventListener('click', () => {
    window.location.href = '/';
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

// Get the select element and its associated error message
const interestInput = document.querySelector('select[name="interest"]');
const interestError = document.getElementById('interest-error');

// Function to validate the select field
function validateInterest() {
    if (!interestInput.value) {
        interestError.style.display = 'block';
        return false;
    } else {
        interestError.style.display = 'none';
        return true;
    }
}

// Validate when the form is submitted
document.getElementById('registration-form').addEventListener('submit', (event) => {
    const isInterestValid = validateInterest();

    // Prevent submission if interest is invalid
    if (!isInterestValid) {
        event.preventDefault();
    }
});

// Hide error when the user selects a valid option
interestInput.addEventListener('change', () => {
    validateInterest();
});
    

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registration-form');

    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent the default form submission

        const formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
            .then(response => {
                if (response.ok) {
                    // Handle successful submission (e.g., redirect or show a success message)
                    window.location.reload(); // Reload the page
                } else if (response.status === 403) {
                    // Handle CSRF token error
                    alert('Session expired. Reloading the page to refresh CSRF token.');
                    window.location.reload(); // Reload the page
                } else {
                    // Handle other errors
                    alert('An error occurred. Please try again.');
                }
            })
            .catch(() => {
                alert('An unexpected error occurred. Please try again.');
            });
    });
});