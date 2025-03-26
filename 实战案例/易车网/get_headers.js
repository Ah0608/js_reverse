const CryptoJS = require("crypto-js");

function get_sign(cid,params,ts){
    r =  "cid=" + cid + "&param=" + params + "19DDD1FBDFF065D3A4DA777D2D7A81EC" + ts
    return CryptoJS.MD5(r).toString()
}
