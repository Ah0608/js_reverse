const crypto = require('crypto');

function getHash(ua,url) {
    day = new Date().getDate()
    str = ua + day + url;
    const hash = crypto.createHash('sha256')
    hash.update(str);
    return hash.digest('hex');
}
