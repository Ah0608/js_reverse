const CryptoJS = require("crypto-js");

function u(e) {
    var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "XwKsGlMcdPMEhR1B"
      , i = CryptoJS.enc.Utf8.parse(t)
      , r = CryptoJS.enc.Utf8.parse(e)
      , o = CryptoJS.AES.encrypt(r, i, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return o.toString()
}