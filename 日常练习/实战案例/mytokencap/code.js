function wordsToBytes(t) {
    for (var e = [], n = 0; n < 32 * t.length; n += 8)
        e.push(t[n >>> 5] >>> 24 - n % 32 & 255);
    return e
}

function stringToBytes_1(t) {
    for (var e = [], n = 0; n < t.length; n++)
        e.push(255 & t.charCodeAt(n));
    return e
}

function bytesToWords(t) {
    for (var e = [], n = 0, r = 0; n < t.length; n++,
        r += 8)
        e[r >>> 5] |= t[n] << 24 - r % 32;
    return e
}

function stringToBytes_2(t) {
    return stringToBytes_1(unescape(encodeURIComponent(t)))
}

function rotl(t, e) {
    return t << e | t >>> 32 - e
}

function endian(t) {
    if (t.constructor == Number)
        return 16711935 & rotl(t, 8) | 4278255360 & rotl(t, 24);
    for (var e = 0; e < t.length; e++)
        t[e] = endian(t[e]);
    return t
}

function bytesToHex(t) {
    for (var e = [], n = 0; n < t.length; n++)
        e.push((t[n] >>> 4).toString(16)),
            e.push((15 & t[n]).toString(16));
    return e.join("")
}

s._ff = function (t, e, n, r, o, i, s) {
    var a = t + (e & n | ~e & r) + (o >>> 0) + s;
    return (a << i | a >>> 32 - i) + e
}

s._gg = function (t, e, n, r, o, i, s) {
    var a = t + (e & r | n & ~r) + (o >>> 0) + s;
    return (a << i | a >>> 32 - i) + e
}

s._hh = function (t, e, n, r, o, i, s) {
    var a = t + (e ^ n ^ r) + (o >>> 0) + s;
    return (a << i | a >>> 32 - i) + e
}

s._ii = function (t, e, n, r, o, i, s) {
    var a = t + (n ^ (e | ~r)) + (o >>> 0) + s;
    return (a << i | a >>> 32 - i) + e
}

function s(t, n) {
    console.log(t)
    t.constructor == String ? t = n && "binary" === n.encoding ? stringToBytes_1(t) : stringToBytes_2(t) : o(t) ? t = Array.prototype.slice.call(t, 0) : Array.isArray(t) || t.constructor === Uint8Array || (t = t.toString());
    for (var a = bytesToWords(t), u = 8 * t.length, c = 1732584193, l = -271733879, f = -1732584194, h = 271733878, p = 0; p < a.length; p++)
        a[p] = 16711935 & (a[p] << 8 | a[p] >>> 24) | 4278255360 & (a[p] << 24 | a[p] >>> 8);
    a[u >>> 5] |= 128 << u % 32,
        a[14 + (u + 64 >>> 9 << 4)] = u;
    var d = s._ff
        , g = s._gg
        , y = s._hh
        , v = s._ii;
    for (p = 0; p < a.length; p += 16) {
        var m = c
            , b = l
            , w = f
            , O = h;
        c = d(c, l, f, h, a[p + 0], 7, -680876936),
            h = d(h, c, l, f, a[p + 1], 12, -389564586),
            f = d(f, h, c, l, a[p + 2], 17, 606105819),
            l = d(l, f, h, c, a[p + 3], 22, -1044525330),
            c = d(c, l, f, h, a[p + 4], 7, -176418897),
            h = d(h, c, l, f, a[p + 5], 12, 1200080426),
            f = d(f, h, c, l, a[p + 6], 17, -1473231341),
            l = d(l, f, h, c, a[p + 7], 22, -45705983),
            c = d(c, l, f, h, a[p + 8], 7, 1770035416),
            h = d(h, c, l, f, a[p + 9], 12, -1958414417),
            f = d(f, h, c, l, a[p + 10], 17, -42063),
            l = d(l, f, h, c, a[p + 11], 22, -1990404162),
            c = d(c, l, f, h, a[p + 12], 7, 1804603682),
            h = d(h, c, l, f, a[p + 13], 12, -40341101),
            f = d(f, h, c, l, a[p + 14], 17, -1502002290),
            c = g(c, l = d(l, f, h, c, a[p + 15], 22, 1236535329), f, h, a[p + 1], 5, -165796510),
            h = g(h, c, l, f, a[p + 6], 9, -1069501632),
            f = g(f, h, c, l, a[p + 11], 14, 643717713),
            l = g(l, f, h, c, a[p + 0], 20, -373897302),
            c = g(c, l, f, h, a[p + 5], 5, -701558691),
            h = g(h, c, l, f, a[p + 10], 9, 38016083),
            f = g(f, h, c, l, a[p + 15], 14, -660478335),
            l = g(l, f, h, c, a[p + 4], 20, -405537848),
            c = g(c, l, f, h, a[p + 9], 5, 568446438),
            h = g(h, c, l, f, a[p + 14], 9, -1019803690),
            f = g(f, h, c, l, a[p + 3], 14, -187363961),
            l = g(l, f, h, c, a[p + 8], 20, 1163531501),
            c = g(c, l, f, h, a[p + 13], 5, -1444681467),
            h = g(h, c, l, f, a[p + 2], 9, -51403784),
            f = g(f, h, c, l, a[p + 7], 14, 1735328473),
            c = y(c, l = g(l, f, h, c, a[p + 12], 20, -1926607734), f, h, a[p + 5], 4, -378558),
            h = y(h, c, l, f, a[p + 8], 11, -2022574463),
            f = y(f, h, c, l, a[p + 11], 16, 1839030562),
            l = y(l, f, h, c, a[p + 14], 23, -35309556),
            c = y(c, l, f, h, a[p + 1], 4, -1530992060),
            h = y(h, c, l, f, a[p + 4], 11, 1272893353),
            f = y(f, h, c, l, a[p + 7], 16, -155497632),
            l = y(l, f, h, c, a[p + 10], 23, -1094730640),
            c = y(c, l, f, h, a[p + 13], 4, 681279174),
            h = y(h, c, l, f, a[p + 0], 11, -358537222),
            f = y(f, h, c, l, a[p + 3], 16, -722521979),
            l = y(l, f, h, c, a[p + 6], 23, 76029189),
            c = y(c, l, f, h, a[p + 9], 4, -640364487),
            h = y(h, c, l, f, a[p + 12], 11, -421815835),
            f = y(f, h, c, l, a[p + 15], 16, 530742520),
            c = v(c, l = y(l, f, h, c, a[p + 2], 23, -995338651), f, h, a[p + 0], 6, -198630844),
            h = v(h, c, l, f, a[p + 7], 10, 1126891415),
            f = v(f, h, c, l, a[p + 14], 15, -1416354905),
            l = v(l, f, h, c, a[p + 5], 21, -57434055),
            c = v(c, l, f, h, a[p + 12], 6, 1700485571),
            h = v(h, c, l, f, a[p + 3], 10, -1894986606),
            f = v(f, h, c, l, a[p + 10], 15, -1051523),
            l = v(l, f, h, c, a[p + 1], 21, -2054922799),
            c = v(c, l, f, h, a[p + 8], 6, 1873313359),
            h = v(h, c, l, f, a[p + 15], 10, -30611744),
            f = v(f, h, c, l, a[p + 6], 15, -1560198380),
            l = v(l, f, h, c, a[p + 13], 21, 1309151649),
            c = v(c, l, f, h, a[p + 4], 6, -145523070),
            h = v(h, c, l, f, a[p + 11], 10, -1120210379),
            f = v(f, h, c, l, a[p + 2], 15, 718787259),
            l = v(l, f, h, c, a[p + 9], 21, -343485551),
            c = c + m >>> 0,
            l = l + b >>> 0,
            f = f + w >>> 0,
            h = h + O >>> 0
    }
    return endian([c, l, f, h])
}

function a(t, n) {
    var r = wordsToBytes(s(t, n));
    return bytesToHex(r)
}

function get_params() {
    var t = Date.now().toString()
    return {
        code: a(t + "9527" + t.substr(0, 6)),
        timestamp: t,
        platform: "web_pc",
        v: "0.1.0",
    }
}


console.log(get_params())