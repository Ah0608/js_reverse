const CryptoJS = require("crypto-js");

function get_token(arguments) {
    for (var t = Math.round((new Date).getTime() / 1000).toString(), e = arguments.length, r = new Array(e), i = 0; i < e; i++)
        r[i] = arguments[i];
    r.push(t);
    console.log(r);
    var o = CryptoJS.SHA1(r.join(",")).toString(CryptoJS.enc.Hex)
        , c = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse([o, t].join(",")));
    return c
}

arguments = ["/api/movie", 0]
console.log(get_token(arguments));