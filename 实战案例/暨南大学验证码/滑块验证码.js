

function jsonp(){
    h = "__JSONP"
    f = Math.random().toString(36).slice(2, 9)
    a = null
    i = 0
    d = a || h + ("_" + f) + ("_" + i++)
    return d

}
console.log(jsonp())
