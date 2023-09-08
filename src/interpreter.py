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
            return Call("Call", callee["text"], arguments, Loc(**location))

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
            read_node(expression, context)
        case Let(kind, name, value, next, location):
            node = read_node(value, context)
            context[name.text] = node
            return read_node(next, context)
        case If(kind, condition, them, otherwise, location):
            condition_result = read_node(condition, context)
            return read_node(them, context) if condition_result else read_node(otherwise, context)
        case Binary(kind, lhs, op, rhs):
            lhs = read_node(lhs, context)

            rhs = read_node(rhs, context)

            return BinaryOp[op](lhs, rhs)
        case Call(kind, callee, arguments, location):
            method = context[callee]
            method_context = {**context}
            for argument, parameter in zip(arguments, method.parameters):
                method_context[parameter.text] = read_node(argument, method_context)
            return read_node(method.value, method_context)
        case Var(kind, text, location):
            return context[text]
        case PrintFunction(kind, value, location):
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
        case Int(kind, value, location) | Str(kind, value, location) | Bool(kind, value, location):
            return value
        case Tuple(kind, first, second, location):
            return (
                first,
                second,
            )
        case Function(kind, parameters, value, location):
            return Function(kind, parameters, value, location)
        case _:
            return ast


def process_file(filepath: str) -> None:
    with open(filepath) as file:
        ast = json.load(file)
    context_variables = {}
    read_node(ast, context_variables)
