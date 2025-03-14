import { parse } from "@babel/parser";
import * as types from "@babel/types";
import CodeGenerator from '@babel/generator';
import fs from "fs";
import {traverse} from "@babel/core";


const code = fs.readFileSync("code1.js", "utf-8");
let ast = parse(code);

traverse(ast, {
  "UnaryExpression|BinaryExpression|ConditionalExpression|CallExpression": (
    path
  ) => {
    const { confident, value } = path.evaluate();
    console.log({ confident, value });
    if (value == Infinity || value == -Infinity) return;
    confident && path.replaceWith(types.valueToNode(value));
  },
});

const  output = CodeGenerator.default(ast,{
    retainLines:true
});
console.log(output);