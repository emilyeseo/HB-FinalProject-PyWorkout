"use strict";

document.querySelector('#send-txt-button').addEventListener('click', (evt) => {
    evt.preventDefault();

    console.log(evt)

    let url = "/send-sms";
    let exercises = $(".exercise_name");

    let exercise_names = []
    for (let exercise of exercises){
        exercise_names.push(exercise.innerHTML)
    } 

    $.post(url, {"names":exercise_names}, (res) => {
        if (res === 'success'){
            console.log(res)
        }
    })
});