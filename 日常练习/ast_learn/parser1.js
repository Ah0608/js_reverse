import { parse }from "@babel/parser";
import CodeGenerator from '@babel/generator';
import fs from "fs";

const code = fs.readFileSync("code.js","utf-8");
let ast = parse(code,{
  sourceType: "module",
});

const  output = CodeGenerator.default(ast,{
    retainLines:true
});

// console.log(ast)
console.log(output)
