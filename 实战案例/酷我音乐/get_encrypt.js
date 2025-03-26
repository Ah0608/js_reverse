const m = 'Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324'
const crypto = require('crypto');

function f(t, e) {
    if (null == e || e.length <= 0)
        return null;
    for (var n = "", i = 0; i < e.length; i++)
        n += e.charCodeAt(i).toString();
    var o = Math.floor(n.length / 5)
        , r = parseInt(n.charAt(o) + n.charAt(2 * o) + n.charAt(3 * o) + n.charAt(4 * o) + n.charAt(5 * o))
        , c = Math.ceil(e.length / 2)
        , l = Math.pow(2, 31) - 1;
    if (r < 2)
        return null;
    var d = Math.round(1e9 * Math.random()) % 1e8;
    for (n += d; n.length > 10;)
        n = (parseInt(n.substring(0, 10)) + parseInt(n.substring(10, n.length))).toString();
    n = (r * n + c) % l;
    var f = ""
        , h = "";
    for (i = 0; i < t.length; i++)
        h += (f = parseInt(t.charCodeAt(i) ^ Math.floor(n / l * 255))) < 16 ? "0" + f.toString(16) : f.toString(16),
            n = (r * n + c) % l;
    for (d = d.toString(16); d.length < 8;)
        d = "0" + d;
    return h += d
}

function get_e(t, cookies) {
    var e = cookies
        , n = e.indexOf(t + "=");
    if (-1 != n) {
        n = n + t.length + 1;
        var o = e.indexOf(";", n);
        return -1 == o && (o = e.length),
            unescape(e.substring(n, o))
    }
    console.log('需要传cookies')
    return null
}

function get_secret(cookies) {
    e = get_e(m, cookies)
    console.log(e)
    console.log(m)
    return f(e, m)
}

function generateRandomBytes() {
    const buffer = crypto.randomBytes(16);
    return new Uint8Array(buffer);
}

function aaa() {
    return generateRandomBytes();
}

function bbb(e, t) {
    for (var n = [], i = 0; i < 256; ++i)
        n[i] = (i + 256).toString(16).substr(1);
    var i = t || 0
        , r = n;
    return [r[e[i++]], r[e[i++]], r[e[i++]], r[e[i++]], "-", r[e[i++]], r[e[i++]], "-", r[e[i++]], r[e[i++]], "-", r[e[i++]], r[e[i++]], "-", r[e[i++]], r[e[i++]], r[e[i++]], r[e[i++]], r[e[i++]], r[e[i++]]].join("")
}

var r, o, l = aaa, c = bbb, d = 0, h = 0;

function get_reqid(e, t, n) {
    var i = t && n || 0
        , b = t || []
        , f = (e = e || {}).node || r
        , v = void 0 !== e.clockseq ? e.clockseq : o;
    if (null == f || null == v) {
        var m = l();
        null == f && (f = r = [1 | m[0], m[1], m[2], m[3], m[4], m[5]]),
        null == v && (v = o = 16383 & (m[6] << 8 | m[7]))
    }
    var y = void 0 !== e.msecs ? e.msecs : (new Date).getTime()
        , w = void 0 !== e.nsecs ? e.nsecs : h + 1
        , dt = y - d + (w - h) / 1e4;
    if (dt < 0 && void 0 === e.clockseq && (v = v + 1 & 16383),
    (dt < 0 || y > d) && void 0 === e.nsecs && (w = 0),
    w >= 1e4)
        throw new Error("uuid.v1(): Can't create more than 10M uuids/sec");
    d = y,
        h = w,
        o = v;
    var A = (1e4 * (268435455 & (y += 122192928e5)) + w) % 4294967296;
    b[i++] = A >>> 24 & 255,
        b[i++] = A >>> 16 & 255,
        b[i++] = A >>> 8 & 255,
        b[i++] = 255 & A;
    var x = y / 4294967296 * 1e4 & 268435455;
    b[i++] = x >>> 8 & 255,
        b[i++] = 255 & x,
        b[i++] = x >>> 24 & 15 | 16,
        b[i++] = x >>> 16 & 255,
        b[i++] = v >>> 8 | 128,
        b[i++] = 255 & v;
    for (var T = 0; T < 6; ++T)
        b[i + T] = f[T];
    return t || c(b)
}
