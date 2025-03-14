const base64 = require('js-base64');
const _0x189cbb = require('crypto-js')


function idEncrype(_0x177944) {
    var _0x11a046 = 'ef34#teuq0btua#(-57w1q5o5--j@98xygimlyfxs*-!i-0-mb'
    var _0x2c4f17 = _0x11a046 + _0x177944['toString']();
    return base64['encode'](_0x2c4f17);
}


function get_token() {
    for (var _0x5da681 = Math['round'](new Date()['getTime']() / 0x3e8)['toString'](), _0x2a83dd = arguments['length'], _0x31a891 = new Array(_0x2a83dd), _0x596a02 = 0x0; _0x596a02 < _0x2a83dd; _0x596a02++)
        _0x31a891[_0x596a02] = arguments[_0x596a02];
    _0x31a891['push'](_0x5da681);
    var _0xf7c3c7 = _0x189cbb['SHA1'](_0x31a891['join'](','))['toString'](_0x189cbb['enc']['Hex'])
        , _0x3c8435 = [_0xf7c3c7, _0x5da681]['join'](',')
        , _0x104b5b = base64['encode'](_0x3c8435);
    return _0x104b5b;
}

