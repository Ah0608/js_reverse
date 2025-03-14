const CryptJs = require('crypto-js');

function encryptApiKey() {
    var e = 'a2c903cc-b31e-4547-9299-b6d07b7631ab'
        , t = e.split("")
        , r = t.splice(0, 8);
    return e = t.concat(r).join("")
}

function encryptTime(e) {
    d = 1111111111111

    var t = (1 * e + d).toString().split("")
        , r = parseInt(10 * Math.random(), 10)
        , n = parseInt(10 * Math.random(), 10)
        , o = parseInt(10 * Math.random(), 10);
    return t.concat([r, n, o]).join("")
}

function comb(e, t) {
    var r = "".concat(e, "|").concat(t);
    return CryptJs.enc.Base64.stringify(CryptJs.enc.Utf8.parse(r));
}

function getApiKey() {
    var e = (new Date).getTime()
        , t = encryptApiKey();
    return e = encryptTime(e),
        comb(t, e)
}

console.log(getApiKey())