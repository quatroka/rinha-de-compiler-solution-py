import json
from src.kinds import *


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
            return Let("Let", identify_type(name), value, next, Loc(**location))

        case {"kind": "Function", "parameters": parameters, "value": value, "location": location}:
            return Function("Function", list(map(identify_type, parameters)), value, Loc(**location))

        case {"kind": "If", "condition": condition, "then": then, "otherwise": otherwise, "location": location}:
            return If("If", condition, then, otherwise, location)

        case {"kind": "Call", "callee": callee, "arguments": arguments, "location": location}:
            return Call("Call", callee['text'], arguments, Loc(**location))

        case {"kind": "Var", "text": text, "location": location}:
            return Var("Var", text, Loc(**location))

        case {"kind": "Binary", "lhs": lhs, "op": op, "rhs": rhs, "location": location}:
            return Binary("Binary", lhs, op, rhs, Loc(**location))

        case {"kind": "Int", "value": value, "location": location}:
            return Int("Int", value, Loc(**location))
        
        case {"kind": "Str", "value": value, "location": location}:
            return Str("Str", value, Loc(**location))
        
        case {"kind": "Bool", "value": value, "location": location}:
            return Bool("Bool", value, Loc(**location))

        case {"kind": "Print", "value": value, "location": location}:
            return PrintFunction("Print", value, Loc(**location))
        
        case {"kind": "Tuple", "first": first, "second": second, "location": location}:
            return Tuple("Tuple", first, second, Loc(**location))
        
        case {"kind": "First", "value": value, "location": location}:
            return FirstFunction("First", value, Loc(**location))
        
        case {"kind": "Second", "value": value, "location": location}:
            return SecondFunction("Second", value, Loc(**location))
        
        case {"text": text, "location": location}:
            return Parameter(text, Loc(**location))

    return node


def read_node(ast: dict | list, context: dict):
    match identify_type(ast):
        case File(name, expression, location):
            # print(f"Start reading file: {name}")
            read_node(expression, context)
        case Let(kind, name, value, next, location):
            # print(f"Reading/Setting Let: {name}")
            node = read_node(value, context)
            context[name.text] = node
            # print(f"Context Variables: {context_variables}")
            # print(f"\nReading Next Command: {next}")
            return read_node(next, context)
        case Function(kind, parameters, value, location):
            # print(f"""Reading Function {value} with parameters: {",".join(p['text'] for p in parameters)}""")
            return (parameters, value)
        case If(kind, condition, them, otherwise, location):
            # print(f"Reading If with condition {condition}")
            condition_result = read_node(condition, context)
            return read_node(them, context) if condition_result else read_node(otherwise, context)
        case Binary(kind, lhs, op, rhs):
            # print(f"Reading binary lhs {lhs}")
            lhs = read_node(lhs, context)

            # print(f"Reading rhs {rhs}")
            rhs = read_node(rhs, context)

            # print(f"Reading op {op}")
            return BinaryOp[op](lhs, rhs)
        case Call(kind, callee, arguments, location):
            # print(f"\nReading call '{callee}' with arguments {arguments}")
            method = context[callee]
            method_context = {**context}
            # print(f"\nMethod context: {method_context}\n")
            for argument, parameter in zip(arguments, method[0]):
                # print(f'====> {type(argument)} {argument} ||| {type(parameter)} {parameter}')
                method_context[parameter.text] = read_node(argument, method_context)
            # print(f"\nMethod context: {method_context}\n")
            return read_node(method[1], method_context)
        case Var(kind, text, location):
            # print(f"Reading Var: {text}")
            return context[text]
        case PrintFunction(kind, value, location):
            # print(f"Reading PrintFunction with value: {value}")
            node = read_node(value, context)
            print(node)
        case FirstFunction(kind, value, location):
            node = read_node(value, context)
            if isinstance(node, tuple):
                return read_node(node[0], context)
            return read_node(node, context)
        case SecondFunction(kind, value, location):
            node = read_node(value, context)
            if isinstance(node, tuple):
                return read_node(node[1], context)
            return read_node(node, context)
        case Int(kind, value, location):
            return value
        case Str(kind, value, location):
            return value
        case Bool(kind, value, location):
            return value
        case Tuple(kind, first, second, location):
            return (first, second,)


def process_file(filepath: str) -> None:
    with open(filepath) as file:
        ast = json.load(file)
    context_variables = {}
    read_node(ast, context_variables)
