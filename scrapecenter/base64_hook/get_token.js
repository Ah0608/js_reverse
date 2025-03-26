const Base64 = require('js-base64');

let form_date = {
    "username": "admin",
    "password": "admin"
}

function getToken() {
    var e = Base64.encode(JSON.stringify(form_date));
    console.log(e)
}

getToken()