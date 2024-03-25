// Example JavaScript code

// Function to validate the registration form
function validateRegistrationForm() {
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirm_password').value;

    // Simple validation (you can add more validation logic)
    if (username.trim() === '') {
        alert('Please enter a username.');
        return false;
    }

    if (email.trim() === '') {
        alert('Please enter an email address.');
        return false;
    }

    if (password.trim() === '') {
        alert('Please enter a password.');
        return false;
    }

    if (confirmPassword.trim() === '') {
        alert('Please confirm your password.');
        return false;
    }

    if (password !== confirmPassword) {
        alert('Passwords do not match.');
        return false;
    }

    return true;
}

// Function to perform some action after the page has loaded
function onPageLoad() {
    console.log('Page loaded.');
    // You can add additional actions here
}

// Call onPageLoad function when the DOM content is loaded
document.addEventListener('DOMContentLoaded', onPageLoad);
