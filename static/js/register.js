"use strict";

document.querySelector('#register-button').addEventListener('click', (evt) => {
    // preventDefault will prevent the default behavior so be flexible with the functionality
    evt.preventDefault();

    const formData = {
        firstname:$('#firstname').val(),
        lastname:$('#lastname').val(),
        email: $('#email').val(),
        password: $('#password').val()
    };

    $.post('/register_user', formData, (res) => {
        if (res === 'Sorry. This login email already exists. Please try a different email address to register, or login to your exisiting account.') {
            Toastify({
                text: "Sorry. This login email already exists. Please try a different email address to register, or login to your exisiting account.",
                duration: 2000,
                backgroundColor: "linear-gradient(to right, #FB5607, #D8DBE2)"
                }).showToast();
            setTimeout(() => {window.location.href='/'}, 3000);
        }

        else if(res === 'Account succesfully created. Please proceed and log in to your account.'){
            Toastify({
                text: "Account succesfully created. Please proceed and log in to your account.",
                duration: 2000,
                backgroundColor: "linear-gradient(to right, #FB5607, #D8DBE2)"
                }).showToast();
            setTimeout(() => {window.location.href='/'}, 3000);
        }
    })
});