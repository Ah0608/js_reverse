const CryptoJS = require("crypto-js");


function l(t, e) {
    return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
}

function u(t) {
    for (var e = Object.keys(t).sort(l), n = "", a = 0; a < e.length; a++)
        if (void 0 !== t[e[a]])
            if (t[e[a]] && t[e[a]] instanceof Object || t[e[a]] instanceof Array) {
                var i = JSON.stringify(t[e[a]]);
                n += e[a] + i
            } else
                n += e[a] + t[e[a]];
    return n
}

function s(e) {
    const hash = CryptoJS.MD5(e);
    return hash.toString(CryptoJS.enc.Hex);
}

function get_sign(t) {
    for (var e in t)
        "" !== t[e] && void 0 !== t[e] || delete t[e];
    var n = "B3978D054A72A7002063637CCDF6B2E5" + u(t);
    return s(n).toLocaleLowerCase()
}

function decrypt_text(t) {
    var e = CryptoJS.enc.Utf8.parse('EB444973714E4A40876CE66BE45D5930')
        , n = CryptoJS.enc.Utf8.parse('B5A8904209931867')
        , a = CryptoJS.AES.decrypt(t, e, {
        iv: n,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return a.toString(CryptoJS.enc.Utf8)
}

data = {
    "ts": 1741245788891,
    "pageNo": 2,
    "pageSize": 20,
    "total": 2791,
    "AREACODE": "",
    "M_PROJECT_TYPE": "",
    "KIND": "GCJS",
    "GGTYPE": "1",
    "PROTYPE": "",
    "timeType": "6",
    "BeginTime": "2024-09-06 00:00:00",
    "EndTime": "2025-03-06 23:59:59",
    "createTime": ""
}
console.log(get_sign(data))
