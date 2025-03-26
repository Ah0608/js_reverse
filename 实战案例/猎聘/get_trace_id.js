const crypto = require('crypto');


function m(length = 16) {
    const randomBytes = crypto.randomBytes(length);
    return new Uint8Array(randomBytes.buffer, randomBytes.byteOffset, length);
}

var _ = function (e) {
    var g = /^(?:[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}|00000000-0000-0000-0000-000000000000)$/i;
    for (var v = function (e) {
        return "string" == typeof e && g.test(e)
    }, y = [], b = 0; b < 256; ++b)
        y.push((b + 256).toString(16).substr(1));

    var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : 0
        ,
        n = (y[e[t + 0]] + y[e[t + 1]] + y[e[t + 2]] + y[e[t + 3]] + "-" + y[e[t + 4]] + y[e[t + 5]] + "-" + y[e[t + 6]] + y[e[t + 7]] + "-" + y[e[t + 8]] + y[e[t + 9]] + "-" + y[e[t + 10]] + y[e[t + 11]] + y[e[t + 12]] + y[e[t + 13]] + y[e[t + 14]] + y[e[t + 15]]).toLowerCase();
    if (!v(n))
        throw TypeError("Stringified UUID is invalid");
    return n
};

w = function (e={}, t, n) {
    var r = (e = e || {}).random || (e.rng || m)();
    if (r[6] = 15 & r[6] | 64,
        r[8] = 63 & r[8] | 128,
        t) {
        n = n || 0;
        for (var i = 0; i < 16; ++i)
            t[n + i] = r[i];
        return t
    }
    return _(r)
}
