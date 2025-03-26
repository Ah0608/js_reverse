function y(e) {
    var t, n, r = "0123456789abcdef", o = "";
    for (n = 0; n < e.length; n += 1)
        o += r.charAt((t = e.charCodeAt(n)) >>> 4 & 15) + r.charAt(15 & t);
    return o
}

function m(e) {
    return unescape(encodeURIComponent(e))
}

function d(e) {
    var t, n = [];
    for (t = 0,
             n[(e.length >> 2) - 1] = void 0; t < n.length; t += 1)
        n[t] = 0;
    var r = 8 * e.length;
    for (t = 0; t < r; t += 8)
        n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
    return n
}

function p(e) {
    var t, n = "", r = 32 * e.length;
    for (t = 0; t < r; t += 8)
        n += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
    return n
}

function i(e, t) {
    var n = (65535 & e) + (65535 & t);
    return (e >> 16) + (t >> 16) + (n >> 16) << 16 | 65535 & n
}

function a(e, t, n, r, o, a) {
    var u;
    return i((u = i(i(t, e), i(r, a))) << o | u >>> 32 - o, n)
}

function u(e, t, n, r, o, i, u) {
    return a(t & n | ~t & r, e, t, o, i, u)
}

function c(e, t, n, r, o, i, u) {
    return a(t & r | n & ~r, e, t, o, i, u)
}

function s(e, t, n, r, o, i, u) {
    return a(t ^ n ^ r, e, t, o, i, u)
}

function l(e, t, n, r, o, i, u) {
    return a(n ^ (t | ~r), e, t, o, i, u)
}

function f(e, t) {
    e[t >> 5] |= 128 << t % 32,
        e[(t + 64 >>> 9 << 4) + 14] = t;
    var n, r, o, a, f, p = 1732584193, d = -271733879, y = -1732584194, m = 271733878;
    for (n = 0; n < e.length; n += 16)
        r = p,
            o = d,
            a = y,
            f = m,
            p = u(p, d, y, m, e[n], 7, -680876936),
            m = u(m, p, d, y, e[n + 1], 12, -389564586),
            y = u(y, m, p, d, e[n + 2], 17, 606105819),
            d = u(d, y, m, p, e[n + 3], 22, -1044525330),
            p = u(p, d, y, m, e[n + 4], 7, -176418897),
            m = u(m, p, d, y, e[n + 5], 12, 1200080426),
            y = u(y, m, p, d, e[n + 6], 17, -1473231341),
            d = u(d, y, m, p, e[n + 7], 22, -45705983),
            p = u(p, d, y, m, e[n + 8], 7, 1770035416),
            m = u(m, p, d, y, e[n + 9], 12, -1958414417),
            y = u(y, m, p, d, e[n + 10], 17, -42063),
            d = u(d, y, m, p, e[n + 11], 22, -1990404162),
            p = u(p, d, y, m, e[n + 12], 7, 1804603682),
            m = u(m, p, d, y, e[n + 13], 12, -40341101),
            y = u(y, m, p, d, e[n + 14], 17, -1502002290),
            d = u(d, y, m, p, e[n + 15], 22, 1236535329),
            p = c(p, d, y, m, e[n + 1], 5, -165796510),
            m = c(m, p, d, y, e[n + 6], 9, -1069501632),
            y = c(y, m, p, d, e[n + 11], 14, 643717713),
            d = c(d, y, m, p, e[n], 20, -373897302),
            p = c(p, d, y, m, e[n + 5], 5, -701558691),
            m = c(m, p, d, y, e[n + 10], 9, 38016083),
            y = c(y, m, p, d, e[n + 15], 14, -660478335),
            d = c(d, y, m, p, e[n + 4], 20, -405537848),
            p = c(p, d, y, m, e[n + 9], 5, 568446438),
            m = c(m, p, d, y, e[n + 14], 9, -1019803690),
            y = c(y, m, p, d, e[n + 3], 14, -187363961),
            d = c(d, y, m, p, e[n + 8], 20, 1163531501),
            p = c(p, d, y, m, e[n + 13], 5, -1444681467),
            m = c(m, p, d, y, e[n + 2], 9, -51403784),
            y = c(y, m, p, d, e[n + 7], 14, 1735328473),
            d = c(d, y, m, p, e[n + 12], 20, -1926607734),
            p = s(p, d, y, m, e[n + 5], 4, -378558),
            m = s(m, p, d, y, e[n + 8], 11, -2022574463),
            y = s(y, m, p, d, e[n + 11], 16, 1839030562),
            d = s(d, y, m, p, e[n + 14], 23, -35309556),
            p = s(p, d, y, m, e[n + 1], 4, -1530992060),
            m = s(m, p, d, y, e[n + 4], 11, 1272893353),
            y = s(y, m, p, d, e[n + 7], 16, -155497632),
            d = s(d, y, m, p, e[n + 10], 23, -1094730640),
            p = s(p, d, y, m, e[n + 13], 4, 681279174),
            m = s(m, p, d, y, e[n], 11, -358537222),
            y = s(y, m, p, d, e[n + 3], 16, -722521979),
            d = s(d, y, m, p, e[n + 6], 23, 76029189),
            p = s(p, d, y, m, e[n + 9], 4, -640364487),
            m = s(m, p, d, y, e[n + 12], 11, -421815835),
            y = s(y, m, p, d, e[n + 15], 16, 530742520),
            d = s(d, y, m, p, e[n + 2], 23, -995338651),
            p = l(p, d, y, m, e[n], 6, -198630844),
            m = l(m, p, d, y, e[n + 7], 10, 1126891415),
            y = l(y, m, p, d, e[n + 14], 15, -1416354905),
            d = l(d, y, m, p, e[n + 5], 21, -57434055),
            p = l(p, d, y, m, e[n + 12], 6, 1700485571),
            m = l(m, p, d, y, e[n + 3], 10, -1894986606),
            y = l(y, m, p, d, e[n + 10], 15, -1051523),
            d = l(d, y, m, p, e[n + 1], 21, -2054922799),
            p = l(p, d, y, m, e[n + 8], 6, 1873313359),
            m = l(m, p, d, y, e[n + 15], 10, -30611744),
            y = l(y, m, p, d, e[n + 6], 15, -1560198380),
            d = l(d, y, m, p, e[n + 13], 21, 1309151649),
            p = l(p, d, y, m, e[n + 4], 6, -145523070),
            m = l(m, p, d, y, e[n + 11], 10, -1120210379),
            y = l(y, m, p, d, e[n + 2], 15, 718787259),
            d = l(d, y, m, p, e[n + 9], 21, -343485551),
            p = i(p, r),
            d = i(d, o),
            y = i(y, a),
            m = i(m, f);
    return [p, d, y, m]
}

function h(e) {
    var t;
    return p(f(d(t = m(e)), 8 * t.length))
}

function b(e, t, n) {
    return t ? n ? v(t, e) : y(v(t, e)) : n ? h(e) : y(h(e))
}

function get_params(username, password) {
    return {
        account: username,
        adeOrMedia: 0,
        password: b(b(password) + "daddy"),
        scene: 'nc_login',
        // sessionId: e.csessionid,
        // sig: e.sig,
        state: "1",
        token: ["FFFF0N00000000009594", new Date().getTime(), Math.random()].join(":"),
        nonce: Math.random().toString(16).slice(-9),
        xyz: b('/nr/user/login/loginByAccount?AppKey=joker&account=18723561304&adeOrMedia=0&password=e6908815aad7ba628e0625e5d9b144d8&scene=nc_login&sessionId=010B3TrWzwsdkM2Lqh18cIUwq5tm80RdSl6wI-unLzakfeYMgoVwbDfLwARYPPahdkxNTpXb1uXAqc03R8nK4sNlcmPjX5hpjlLVOwCYiopQmHVksu23RM-V-sPbI2_8fPnc-POmuwiYobyBCQwiHcSQ&sig=05XqrtZ0EaFgmmqIQes-s-CNoBuNEdlN9g8E_zzPUx0c8DSt_u-gHTE-ClzRLh6uLMRJlomfPqj-9WnmToYdepSq1_W1AzBwxRgDW4b-CxpMRc61lO4c5xF4cmdomh5dU6Z2mo5yfQKMXsZxTf7zQLCqPOdOVn4I2QCqb9lj_VMvYWyCq8dG8WJymR9nfLJZSkXYvH40laztnReSGPKZEjPorfHdYuQqPPXEMMBamh-DAociISJBpQ3OX9M_u9RKyPW0MZgn4sC28KvAkaJWGLR-0rN5nV1ufPy4JTFebr7n9JHEgD9E6e8jz2dVig5iK2PRkVLWbPjPgc_kP0-Qd1BHwr8H3KIm6Cd3cZBTasucOnLRrHH6_qxgjxsry8HeEG5ORcjwitO-J3e-8bhqu9Kg&state=1&token=FFFF0N00000000009594:1741155604767:0.3094253246741585&nonce=34beca13a')
    }
}

pwd = get_params("18723561304", "123456")
console.log(pwd)


