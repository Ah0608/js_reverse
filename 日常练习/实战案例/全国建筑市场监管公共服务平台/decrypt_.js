const CryptoJs = require("crypto-js")

f = {
    "words": [
        1148467306,
        964118391,
        624314466,
        2019968622
    ],
    "sigBytes": 16
}

m ={
    "words": [
        808530483,
        875902519,
        943276354,
        1128547654
    ],
    "sigBytes": 16
}

function decrypt_data(t) {
    var e = CryptoJs.enc.Hex.parse(t)
        , n = CryptoJs.enc.Base64.stringify(e)
        , a = CryptoJs.AES.decrypt(n, f, {
        iv: m,
        mode: CryptoJs.mode.CBC,
        padding: CryptoJs.pad.Pkcs7
    })
        , r = a.toString(CryptoJs.enc.Utf8);
    return r.toString()
}
