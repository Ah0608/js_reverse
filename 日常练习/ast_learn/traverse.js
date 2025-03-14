import {parse} from "@babel/parser";
import {traverse} from "@babel/core";
import CodeGenerator from '@babel/generator';

import fs from "fs";

const code = fs.readFileSync("code.js", "utf-8");
let ast = parse(code, {
    sourceType: "module",
});
traverse(ast, {
    NumericLiteral(path) {
        if (path.node.value === 3) {
            path.node.value = 5;
        }
    },
    StringLiteral(path) {
        if (path.node.value === "hello") {
            path.node.value = "hi";
        }
    },
});
const  output = CodeGenerator.default(ast,{
    retainLines:true
});

console.log(output);