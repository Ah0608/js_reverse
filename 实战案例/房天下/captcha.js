// function toChart16(e) {
//     for (var t = "", n = e.length, r = 0; r < n; r++) {
//         var a = e.charCodeAt(r).toString(16)
//             , o = a.length;
//         if (o < 4) {
//             for (var i = 4 - o, s = "", c = 0; c < i; c++)
//                 s += "0";
//             a = s + a
//         } else
//             4 < o && console.log("More than four", a);
//         t += a
//     }
//     return t
// }
//
// function baseCompress(e, t, n) {
//     if (null === e)
//         return "";
//     for (var r, a, o, i, s = {}, c = {}, l = "", d = 2, u = 3, g = 2, h = [], f = 0, v = 0, m = 0; m < e.length; m += 1)
//         if (o = e.charAt(m),
//         Object.prototype.hasOwnProperty.call(s, o) || (s[o] = u++,
//             c[o] = !0),
//             i = l + o,
//             Object.prototype.hasOwnProperty.call(s, i))
//             l = i;
//         else {
//             if (Object.prototype.hasOwnProperty.call(c, l)) {
//                 if (l.charCodeAt(0) < 256) {
//                     for (r = 0; r < g; r++)
//                         f <<= 1,
//                             v === t - 1 ? (v = 0,
//                                 h.push(n(f)),
//                                 f = 0) : v++;
//                     for (a = l.charCodeAt(0),
//                              r = 0; r < 8; r++)
//                         f = f << 1 | 1 & a,
//                             v === t - 1 ? (v = 0,
//                                 h.push(n(f)),
//                                 f = 0) : v++,
//                             a >>= 1
//                 } else {
//                     for (a = 1,
//                              r = 0; r < g; r++)
//                         f = f << 1 | a,
//                             v === t - 1 ? (v = 0,
//                                 h.push(n(f)),
//                                 f = 0) : v++,
//                             a = 0;
//                     for (a = l.charCodeAt(0),
//                              r = 0; r < 16; r++)
//                         f = f << 1 | 1 & a,
//                             v === t - 1 ? (v = 0,
//                                 h.push(n(f)),
//                                 f = 0) : v++,
//                             a >>= 1
//                 }
//                 0 === --d && (d = Math.pow(2, g),
//                     g++),
//                     delete c[l]
//             } else
//                 for (a = s[l],
//                          r = 0; r < g; r++)
//                     f = f << 1 | 1 & a,
//                         v === t - 1 ? (v = 0,
//                             h.push(n(f)),
//                             f = 0) : v++,
//                         a >>= 1;
//             0 === --d && (d = Math.pow(2, g),
//                 g++),
//                 s[i] = u++,
//                 l = String(o)
//         }
//     if ("" !== l) {
//         if (Object.prototype.hasOwnProperty.call(c, l)) {
//             if (l.charCodeAt(0) < 256) {
//                 for (r = 0; r < g; r++)
//                     f <<= 1,
//                         v === t - 1 ? (v = 0,
//                             h.push(n(f)),
//                             f = 0) : v++;
//                 for (a = l.charCodeAt(0),
//                          r = 0; r < 8; r++)
//                     f = f << 1 | 1 & a,
//                         v === t - 1 ? (v = 0,
//                             h.push(n(f)),
//                             f = 0) : v++,
//                         a >>= 1
//             } else {
//                 for (a = 1,
//                          r = 0; r < g; r++)
//                     f = f << 1 | a,
//                         v == t - 1 ? (v = 0,
//                             h.push(n(f)),
//                             f = 0) : v++,
//                         a = 0;
//                 for (a = l.charCodeAt(0),
//                          r = 0; r < 16; r++)
//                     f = f << 1 | 1 & a,
//                         v == t - 1 ? (v = 0,
//                             h.push(n(f)),
//                             f = 0) : v++,
//                         a >>= 1
//             }
//             0 === --d && (d = Math.pow(2, g),
//                 g++),
//                 delete c[l]
//         } else
//             for (a = s[l],
//                      r = 0; r < g; r++)
//                 f = f << 1 | 1 & a,
//                     v == t - 1 ? (v = 0,
//                         h.push(n(f)),
//                         f = 0) : v++,
//                     a >>= 1;
//         0 == --d && (d = Math.pow(2, g),
//             g++)
//     }
//     for (a = 2,
//              r = 0; r < g; r++)
//         f = f << 1 | 1 & a,
//             v == t - 1 ? (v = 0,
//                 h.push(n(f)),
//                 f = 0) : v++,
//             a >>= 1;
//     for (; ;) {
//         if (f <<= 1,
//         v === t - 1) {
//             h.push(n(f));
//             break
//         }
//         v++
//     }
//     return h.join("")
// }
//
// function get_i() {
//     const r = [
//         32588,
//         71601,
//         "CSS1Compat",
//         "",
//         0,
//         0,
//         0,
//         0,
//         1920,
//         267,
//         1920,
//         1040,
//         "zh-CN",
//         "zh-CN,zh",
//         -1,
//         1,
//         24,
//         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
//         1,
//         1,
//         1920,
//         1080,
//         1920,
//         1040,
//         1,
//         1,
//         1,
//         -1,
//         "Win32",
//         0,
//         -8,
//         -1,
//         -1,
//         "PDFViewer,internal-pdf-viewer,ChromePDFViewer,internal-pdf-viewer,ChromiumPDFViewer,internal-pdf-viewer,MicrosoftEdgePDFViewer,internal-pdf-viewer,WebKitbuilt-inPDF,internal-pdf-viewer",
//         0,
//         -1,
//         1,
//         4,
//         -1,
//         1740982328899,
//         "0,0,1,0,0,0,0,9,268,3,9,9,15,934,934,968,7039,7040,7040,0",
//         300
//     ]
//     const e = decodeURIComponent(r.join("!!"));
//     const t = String.fromCharCode
//     console.log(e)
//     return baseCompress(e, 16, function (e) {
//         return toChart16(t(e))
//     })
// }

const t = String.fromCharCode

x = {
    compress: function (e) {
        return x.baseCompress(e, 16, function (e) {
            return x.toChart16(t(e))
        })
    },
    baseCompress: function (e, t, n) {
        if (null === e)
            return "";
        for (var r, a, o, i, s = {}, c = {}, l = "", d = 2, u = 3, g = 2, h = [], f = 0, v = 0, m = 0; m < e.length; m += 1)
            if (o = e.charAt(m),
            Object.prototype.hasOwnProperty.call(s, o) || (s[o] = u++,
                c[o] = !0),
                i = l + o,
                Object.prototype.hasOwnProperty.call(s, i))
                l = i;
            else {
                if (Object.prototype.hasOwnProperty.call(c, l)) {
                    if (l.charCodeAt(0) < 256) {
                        for (r = 0; r < g; r++)
                            f <<= 1,
                                v === t - 1 ? (v = 0,
                                    h.push(n(f)),
                                    f = 0) : v++;
                        for (a = l.charCodeAt(0),
                                 r = 0; r < 8; r++)
                            f = f << 1 | 1 & a,
                                v === t - 1 ? (v = 0,
                                    h.push(n(f)),
                                    f = 0) : v++,
                                a >>= 1
                    } else {
                        for (a = 1,
                                 r = 0; r < g; r++)
                            f = f << 1 | a,
                                v === t - 1 ? (v = 0,
                                    h.push(n(f)),
                                    f = 0) : v++,
                                a = 0;
                        for (a = l.charCodeAt(0),
                                 r = 0; r < 16; r++)
                            f = f << 1 | 1 & a,
                                v === t - 1 ? (v = 0,
                                    h.push(n(f)),
                                    f = 0) : v++,
                                a >>= 1
                    }
                    0 === --d && (d = Math.pow(2, g),
                        g++),
                        delete c[l]
                } else
                    for (a = s[l],
                             r = 0; r < g; r++)
                        f = f << 1 | 1 & a,
                            v === t - 1 ? (v = 0,
                                h.push(n(f)),
                                f = 0) : v++,
                            a >>= 1;
                0 === --d && (d = Math.pow(2, g),
                    g++),
                    s[i] = u++,
                    l = String(o)
            }
        if ("" !== l) {
            if (Object.prototype.hasOwnProperty.call(c, l)) {
                if (l.charCodeAt(0) < 256) {
                    for (r = 0; r < g; r++)
                        f <<= 1,
                            v === t - 1 ? (v = 0,
                                h.push(n(f)),
                                f = 0) : v++;
                    for (a = l.charCodeAt(0),
                             r = 0; r < 8; r++)
                        f = f << 1 | 1 & a,
                            v === t - 1 ? (v = 0,
                                h.push(n(f)),
                                f = 0) : v++,
                            a >>= 1
                } else {
                    for (a = 1,
                             r = 0; r < g; r++)
                        f = f << 1 | a,
                            v == t - 1 ? (v = 0,
                                h.push(n(f)),
                                f = 0) : v++,
                            a = 0;
                    for (a = l.charCodeAt(0),
                             r = 0; r < 16; r++)
                        f = f << 1 | 1 & a,
                            v == t - 1 ? (v = 0,
                                h.push(n(f)),
                                f = 0) : v++,
                            a >>= 1
                }
                0 === --d && (d = Math.pow(2, g),
                    g++),
                    delete c[l]
            } else
                for (a = s[l],
                         r = 0; r < g; r++)
                    f = f << 1 | 1 & a,
                        v == t - 1 ? (v = 0,
                            h.push(n(f)),
                            f = 0) : v++,
                        a >>= 1;
            0 == --d && (d = Math.pow(2, g),
                g++)
        }
        for (a = 2,
                 r = 0; r < g; r++)
            f = f << 1 | 1 & a,
                v == t - 1 ? (v = 0,
                    h.push(n(f)),
                    f = 0) : v++,
                a >>= 1;
        for (; ;) {
            if (f <<= 1,
            v === t - 1) {
                h.push(n(f));
                break
            }
            v++
        }
        return h.join("")
    },
    toChart16: function (e) {
        for (var t = "", n = e.length, r = 0; r < n; r++) {
            var a = e.charCodeAt(r).toString(16)
                , o = a.length;
            if (o < 4) {
                for (var i = 4 - o, s = "", c = 0; c < i; c++)
                    s += "0";
                a = s + a
            } else
                4 < o && console.log("More than four", a);
            t += a
        }
        return t
    }
}

function get_ii() {
    var n = {
        "textLength": 32600,
        "HTMLLength": 98089,
        "documentMode": "CSS1Compat",
        "browserLanguage": "zh-CN",
        "browserLanguages": "zh-CN,zh",
        "devicePixelRatio": 1,
        "colorDepth": 24,
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "cookieEnabled": 1,
        "netEnabled": 1,
        "innerWidth": 1920,
        "innerHeight": 400,
        "outerWidth": 1920,
        "outerHeight": 1040,
        "screenWidth": 1920,
        "screenHeight": 1080,
        "screenAvailWidth": 1920,
        "screenAvailHeight": 1040,
        "screenLeft": 0,
        "screenTop": 0,
        "screenAvailLeft": 0,
        "screenAvailTop": 0,
        "localStorageEnabled": 1,
        "sessionStorageEnabled": 1,
        "indexedDBEnabled": 1,
        "platform": "Win32",
        "doNotTrack": 0,
        "timezone": -8,
        "plugins": "PDFViewer,internal-pdf-viewer,ChromePDFViewer,internal-pdf-viewer,ChromiumPDFViewer,internal-pdf-viewer,MicrosoftEdgePDFViewer,internal-pdf-viewer,WebKitbuilt-inPDF,internal-pdf-viewer",
        "maxTouchPoints": 0,
        "flashEnabled": -1,
        "javaEnabled": 1,
        "hardwareConcurrency": 4,
        "webdriver": "",
        "performanceTiming": "0,0,1,23,0,0,136,0,57,2,7,7,10,540,540,583,995,995,995,0",
        "timestamp": 1741093639411
    }
    n.timestamp = (new Date).getTime(),
        n.cwidth = 300;
    var r = [];
    return ["textLength", "HTMLLength", "documentMode"].concat('webdriver').concat(["screenLeft", "screenTop", "screenAvailLeft", "screenAvailTop", "innerWidth", "innerHeight", "outerWidth", "outerHeight", "browserLanguage", "browserLanguages", "systemLanguage", "devicePixelRatio", "colorDepth", "userAgent", "cookieEnabled", "netEnabled", "screenWidth", "screenHeight", "screenAvailWidth", "screenAvailHeight", "localStorageEnabled", "sessionStorageEnabled", "indexedDBEnabled", "CPUClass", "platform", "doNotTrack", "timezone", "canvas2DFP", "canvas3DFP", "plugins", "maxTouchPoints", "flashEnabled", "javaEnabled", "hardwareConcurrency", "jsFonts", "timestamp", "performanceTiming", "cwidth"]).map(function (e) {
        var t = n[e];
        r.push(void 0 === t ? -1 : t)
    }),
        encodeURIComponent(r.join("!!"))
}

function get_i() {
    return x.compress(get_ii())
}

function C(e) {
    return "number" != typeof e ? e : 32767 < e ? e = 32767 : e < -32767 ? e = -32767 : Math.round(e)
}

function get_e(e) {
    var t = 0
        , n = 0
        , r = 0
        , a = 0
        , o = 0
        , i = []
        , y = 300;
    if (e.length <= 0)
        return [];
    for (var s = e.length, c = s < y ? 0 : s - y; c < s; c += 1) {
        var l = e[c]
            , d = l.e;
        "scroll" === d ? i.push([d, [l.x - r, l.y - a], C(o ? l.t - o : 0)], r = l.x, a = l.y, o = l.t) : -1 < ["mousedown", "mousemove", "mouseup"].indexOf(d) ? (i.push([d, [l.x - t, l.y - n], C(o ? l.t - o : 0)]),
            t = l.x,
            n = l.y,
            o = l.t) : -1 < ["blur", "focus", "unload"].indexOf(d) && (i.push([d, C(o ? l.x - o : 0)]),
            o = l.x)
    }
    return i
}

function get_tt(e) {
    const E = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-:@~*,.()[]/|";
    function g(e, t) {
        for (var n = e.toString(2), r = "", a = n.length + 1; a <= t; a += 1)
            r += "0";
        return r + n
    }

    function d(e, t) {
        for (var n = [], r = 0, a = e.length; r < a; r += 1)
            n.push(t(e[r]));
        return n
    }

    function u(e, t) {
        var n = function (e) {
            for (var t = (e = d(e, function (e) {
                return e = Math.min(32767, e),
                    e = Math.max(-32767, e)
            })).length, n = 0, r = []; n < t;) {
                for (var a = 1, o = e[n], i = Math.abs(o); !(t <= n + a) && e[n + a] === o && !(127 <= i || 127 <= a);)
                    a += 1;
                1 < a ? r.push((o < 0 ? 49152 : 32768) | a << 7 | i) : r.push(o),
                    n += a
            }
            return r
        }(e)
            , a = []
            , o = [];
        d(n, function (e) {
            var t, n, r = Math.ceil((t = Math.abs(e) + 1,
                n = 16,
                0 === t ? 0 : Math.log(t) / Math.log(n)));
            0 === r && (r = 1),
                a.push(g(r - 1, 2)),
                o.push(g(Math.abs(e), 4 * r))
        });
        var r, i, s = a.join(""), c = o.join(""), l = t ? d((r = function (e) {
            return 0 !== e && e >> 15 != 1
        }
            ,
            i = [],
            d(n, function (e) {
                r(e) && i.push(e)
            }),
            i), function (e) {
            return e < 0 ? "1" : "0"
        }).join("") : "";
        return g(32768 | n.length, 16) + s + c + l
    }

    var h = {
        mousemove: 0,
        mousedown: 1,
        mouseup: 2,
        scroll: 3,
        focus: 4,
        blur: 5,
        unload: 6,
        unknown: 7
    };
    return function (e) {
        for (var t = [], n = [], r = [], a = [], o = 0, i = e.length; o < i; o += 1) {
            var s = e[o]
                , c = s.length;
            t.push(s[0]),
                n.push(2 === c ? s[1] : s[2]),
            3 === c && (r.push(Math.round(s[1][0])),
                a.push(Math.round(s[1][1])))
        }
        var l = function (e) {
            for (var t = [], n = e.length, r = 0; r < n;) {
                for (var a = e[r], o = 0; !(16 <= o);) {
                    var i = r + o + 1;
                    if (n <= i)
                        break;
                    if (e[i] !== a)
                        break;
                    o += 1
                }
                r = r + 1 + o;
                var s = h[a];
                0 !== o ? (t.push(8 | s),
                    t.push(o - 1)) : t.push(s)
            }
            for (var c = g(32768 | n, 16), l = "", d = 0, u = t.length; d < u; d += 1)
                l += g(t[d], 4);
            return c + l
        }(t) + u(n, !1) + u(r, !0) + u(a, !0)
            , d = l.length;
        return d % 6 != 0 && (l += g(0, 6 - d % 6)),
            function (e) {
                for (var t = "", n = e.length / 6, r = 0; r < n; r += 1)
                    t += E.charAt(parseInt(e.slice(6 * r, 6 * (r + 1)), 2));
                return t
            }(l)
    }(e)
}

function get_t(track) {
    return get_tt(get_e(track))
}
