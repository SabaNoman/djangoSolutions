console.log('JavaScript is working, yaayyyy!!!!')

function validateForm() {
    var fullName = document.getElementById('fullName').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;
    var message = document.getElementById('message').value;

    // Reset previous errors
    document.getElementById('nameError').innerText = '';
    document.getElementById('emailError').innerText = '';
    document.getElementById('phoneError').innerText = '';
    document.getElementById('messageError').innerText = '';

    // Validation logic
    if (fullName.trim() === '') {
        document.getElementById('nameError').innerText = 'Name is required';
        return false;
    }

    // Add email validation
    if (email.trim() === '') {
        document.getElementById('emailError').innerText = 'Email is required';
        return false;
    }

    // Add phone number validation
    var phoneRegex = /^[0-9]{10,11}$/;
    if (!phone.match(phoneRegex)) {
        document.getElementById('phoneError').innerText = 'Invalid phone number format';
        return false;
    }
    if (message.trim() === '') {
        document.getElementById('messageError').innerText = 'Message is required';
        return false;
    }
    return true; // Form submission will occur only if all validations pass
}