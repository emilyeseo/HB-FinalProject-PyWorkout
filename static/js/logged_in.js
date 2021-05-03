"use strict";

document.querySelector('#login-button').addEventListener('click', (evt) => {
    // preventDefault will prevent the default behavior so be flexible with the functionality
    evt.preventDefault();

    const formData = {
        email: $('#email').val(),
        password: $('#password').val()
    };

    $.post('/login', formData, (res) => {
        if (res === 'successfully logged in') {
            Toastify({
                text: "successfully logged in",
                duration: 2000,
                backgroundColor: "linear-gradient(to right, #FB5607, #D8DBE2)"
                }).showToast();
            setTimeout(() => {window.location.href='/create_workout_plan_form'}, 3000);
        }
        else if (res === 'Wrong password. Try again.') {
            Toastify({
                text: 'Wrong password. Try again.',
                duration: 2000,
                backgroundColor: "linear-gradient(to right, #FB5607, #D8DBE2)"
                }).showToast();
                setTimeout(() => {window.location.href='/'}, 3000);
        }
    })
});