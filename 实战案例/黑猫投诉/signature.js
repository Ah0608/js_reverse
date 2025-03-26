const CryptoJS = require('crypto-js')

const d = "$d6eb7ff91ee257475%"

function rs() {
    e = false
    t = 16
    var i = ""
        , n = t
        ,
        o = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
    e && (n = Math.round(Math.random() * (r - t)) + t);
    for (var a = 0; a < n; a++) {
        i += o[Math.round(Math.random() * (o.length - 1))]
    }
    return i
}

function getSignature(ts, rs, sid, tab_type, page_size, page_num) {
    return CryptoJS.SHA256([ts, rs, d, sid, tab_type, page_size, page_num].sort().join("")).toString()
}
