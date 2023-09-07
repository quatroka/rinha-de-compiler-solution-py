import json
from kinds import *


def identify_type(node: dict | list | str):
    match node:
        case {"name": name, "expression": expression, "location": location}:
            return File(name, expression, Loc(**location))

        case {
            "kind": "Let",
            "name": name,
            "value": value,
            "next": next,
            "location": location,
        }:
            return Let("Let", name["text"], value, next, Loc(**location))

        case {"kind": "Function", "parameters": parameters, "value": value, "location": location}:
            return Function("Function", parameters, value, Loc(**location))

        case {"kind": "If", "condition": condition, "then": then, "otherwise": otherwise, "location": location}:
            return If("If", condition, then, otherwise, location)

        case {"kind": "Call", "callee": callee, "arguments": arguments, "location": location}:
            return Call("Call", callee, arguments, Loc(**location))

        case {"kind": "Var", "text": text, "location": location}:
            return Var("Var", text, Loc(**location))

        case {"kind": "Binary", "lhs": lhs, "op": op, "rhs": rhs, "location": location}:
            return Binary("Binary", lhs, op, rhs, Loc(**location))

        case {"kind": "Int", "value": value, "location": location}:
            return Int("Int", value, Loc(**location))
        
        case {"kind": "Str", "value": value, "location": location}:
            return Int("Int", value, Loc(**location))

        case {"kind": "Print", "value": value, "location": location}:
            return PrintFunction("Print", value, Loc(**location))


def read_node(ast: dict | list, context: dict):
    match identify_type(ast):
        case File(name, expression, location):
            # print(f"Start reading file: {name}")
            read_node(expression, context)
        case Let(kind, name, value, next, location):
            # print(f"Reading Let: {name}")
            node = read_node(value, context)
            context_variables[name] = node
            # print(f"Context Variables: {context_variables}")
            # print(f"\nReading Next Command: {next}")
            read_node(next, context)
        case Function(kind, parameters, value, location):
            print(f"""Reading Function with parameters: {",".join(p['text'] for p in parameters)}""")
            read_node(value, context)
        case If(kind, condition, them, otherwise, location):
            print(f"Reading If with condition {condition}")
            read_node(condition, context)
            print(f"Reading If with them {them}")
            read_node(them, context)
            print(f"Reading If with otherwise {otherwise}")
            read_node(otherwise, context)
        case Binary(kind, lhs, op, rhs):
            # print(f"Reading binary lhs {lhs}")
            lhs = read_node(lhs, context)

            # print(f"Reading rhs {rhs}")
            rhs = read_node(rhs, context)

            # print(f"Reading op {op}")
            return BinaryOp[op](lhs, rhs)
        case Call(kind, callee, arguments, location):
            print(f"Reading call with arguments {arguments}")
            read_node(callee, context)
            list(map(read_node, arguments))
        case Var(kind, text, location):
            # print(f"Reading Var: {text}")
            return context_variables[text]
        case PrintFunction(kind, value, location):
            # print(f"Reading PrintFunction with value: {value}")
            node = read_node(value, context)
            print(node)
        case Int(kind, value, location):
            return value
        case Str(kind, value, location):
            return value


with open("./files/simple4.rinha.json") as file:
    ast = json.load(file)

context_variables = {}

read_node(ast, context_variables)
