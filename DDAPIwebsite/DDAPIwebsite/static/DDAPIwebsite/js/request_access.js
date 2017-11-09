/* request_access.js */

var email = document.getElementById("email");
var email_conf = document.getElementById("email_conf");

function validateEmail(){
    if(email.value !== email_conf.value) {
        email_conf.setCustomValidity("Emails Don't Match");
    }
    else {
        email_conf.setCustomValidity('');
    }
}

email.onchange = validateEmail;
email_conf.onkeyup = validateEmail;
