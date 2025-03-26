const crypto = require('crypto');

function md5_encrypt(t) {
    return crypto.createHash('md5').update(t).digest("hex");
}

i = function (e, t, c, a) {
    var s = e.indexOf("?");
    s > 0 && (e = e.substring(0, s));
    var i = e + JSON.stringify(t) + c;
    return a && (i += a),
        md5_encrypt(i)
}


function get_signature(url, params, appcode) {
    const l = md5_encrypt(appcode).substring(0, 16);
    console.log(l);
    return i(url, params, l, "");
}

// console.log(get_signature("/v1/domainList"));