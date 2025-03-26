const crypto = require('crypto');

function _(e) {
    return crypto.createHash("md5").update(e.toString()).digest("hex")
}

function T(e) {
    return crypto.createHash("md5").update(e).digest()
}

function sign(ts, str) {
    encode_str = `client=fanyideskweb&mysticTime=${ts}&product=webfanyi&key=${str}`
    return _(encode_str)
}

function getresult(encodestr) {
    const o = Buffer.alloc(16, T('ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'))
        , n = Buffer.alloc(16, T('ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'))
        , r = crypto.createDecipheriv("aes-128-cbc", o, n);
    let s = r.update(encodestr, "base64", "utf-8");
    return s += r.final("utf-8"), s
}

console.log(getresult("Z21kD9ZK1ke6ugku2ccWu4n6eLnvoDT0YgGi0y3g-v0B9sYqg8L9D6UERNozYOHqkd_1S5wwFUZhCNbiz2-VrlMHA1nzVzituxNpy_foTHy0O0L-lbV0J344esUU45QedjjS5Tyr3rzDdOFRXLeKSHiO2YMukPJq26h-kVIOvQ08RcJR5yvLMitIBejdhR6TUT_lItMyFlPUsgTzarHayjJtuoMDl46Sb1mAz8du8YGFNiHmeHiNuDxgNqyCu6Plq5bOmVSKEtlI4zomaWw4MRUl_ugXsDbonk-P_-CgeQEujLS7k1eodqlF_wxIORjq61lGRfzMtf0IH_-ja64GrkxIBbVD2yR_J2VGy25NIHuvItjYuQ9DAE11XL5RGZcpjkVACHzj6iK7_v91D4NJ4tiEEc-xcO8c9xH-nQ5ZCR3YLzSom-YoR7UDip1432um7nnZfFnixCPjDJ1YRIdqDajaDQjSbX-OQESkl6nmHYVxQ_Tc85484fPoQyw4yxRtcvkZa09dS_WyRFp6G7TykofLlBwIQHQ7kfsCyy-xv4UTktHq4oi8-svlSMvD93u21ctxbI3CSCxzmIbOGic3BFPlZHMq0WWGK2J7jsKfN2oyecCqEMne9B947ZQ4cQevWHDLxTfWVlhq1J48Jwx-QDOaMCyhXn7uOiY5W7jVBkegOP17W6Vm59fhENeB_8eDkSh0_U9mdlvM0k1BX9tPTHBDO4MCnyh3MfhtUtyCAvipOoOqUyuE8iPL1XNZ5YQd"))