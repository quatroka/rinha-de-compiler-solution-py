from collections import OrderedDict
import json
from src.kinds import *

def cache(cache, max_size = 1_000_000):
    def decorator(fn):
        
        def wrapper(*args):
            key = str(args)
            if key in cache:
                return cache[key]

            result = fn(*args)

            if len(cache) < max_size:
                cache[key] = result
            else:
                del cache[next(iter(cache))]

            return result

        return wrapper
    return decorator


def identify_type(node: dict | list | str):
    match node:
        case {"name": name, "expression": expression, "location": location}:
            return File(name, identify_type(expression), Loc(**location))

        case {"kind": "Let", "location": location, "name": name, "value": value, "next": next}:
            return Let("Let", Loc(**location), identify_type(name), identify_type(value), identify_type(next))

        case {"kind": "Function", "location": location, "parameters": parameters, "value": value}:
            return Function("Function", Loc(**location), list(map(identify_type, parameters)), identify_type(value))

        case {"kind": "If", "location": location, "condition": condition, "then": then, "otherwise": otherwise}:
            return If("If", Loc(**location), identify_type(condition), identify_type(then), identify_type(otherwise))

        case {"kind": "Call", "location": location, "callee": callee, "arguments": arguments}:
            return Call("Call", Loc(**location), callee["text"], list(map(identify_type, arguments)))

        case {"kind": "Var", "location": location, "text": text}:
            return Var("Var", Loc(**location), text)

        case {"kind": "Binary", "location": location, "lhs": lhs, "op": op, "rhs": rhs}:
            return Binary("Binary", Loc(**location), identify_type(lhs), op, identify_type(rhs))

        case {"kind": "Int", "location": location, "value": value}:
            return Int("Int", Loc(**location), value)

        case {"kind": "Str", "location": location, "value": value}:
            return Str("Str", Loc(**location), value)

        case {"kind": "Bool", "location": location, "value": value}:
            return Bool("Bool", Loc(**location), value)

        case {"kind": "Print", "location": location, "value": value}:
            return PrintFunction("Print", Loc(**location), identify_type(value))

        case {"kind": "Tuple", "location": location, "first": first, "second": second}:
            return Tuple("Tuple", Loc(**location), identify_type(first), identify_type(second))

        case {"kind": "First", "location": location, "value": value}:
            return FirstFunction("First", Loc(**location), identify_type(value))

        case {"kind": "Second", "location": location, "value": value}:
            return SecondFunction("Second", Loc(**location), identify_type(value))

        case {"text": text, "location": location}:
            return Parameter(text, Loc(**location))

@cache(cache = OrderedDict())
def read_node(ast: dict | list, context: dict):
    match ast:
        case File(_, expression, _):
            read_node(expression, context)

        case Let(_, _, name, value, next):
            node = read_node(value, context)
            context[name.text] = node
            return read_node(next, context)

        case If(_, _, condition, them, otherwise):
            condition_result = read_node(condition, context)
            return read_node(them, context) if condition_result else read_node(otherwise, context)

        case Binary(_, _, lhs, op, rhs):
            lhs = read_node(lhs, context)
            rhs = read_node(rhs, context)
            return BinaryOp[op](lhs, rhs)

        case Call(_, _, callee, arguments):
            method = context[callee]
            method_context = {**context}
            for argument, parameter in zip(arguments, method.parameters):
                method_context[parameter.text] = read_node(argument, method_context)
            return read_node(method.value, method_context)

        case Var(_, _, text):
            return context[text]

        case PrintFunction(_, _, value):
            node = read_node(value, context)
            print(node)

        case FirstFunction(_, _, value):
            node = read_node(value, context)
            if isinstance(node, tuple):
                return read_node(node[0], context)
            return read_node(node, context)

        case SecondFunction(_, _, value):
            node = read_node(value, context)
            if isinstance(node, tuple):
                return read_node(node[1], context)
            return read_node(node, context)

        case Int(_, _, value) | Str(_, _, value) | Bool(_, _, value):
            return value

        case Tuple(_, _, first, second):
            return (
                first,
                second,
            )

        case Function(kind, location, parameters, value):
            return Function(kind, location, parameters, value)

        case _:
            return ast


def process_file(filepath: str) -> None:
    with open(filepath) as file:
        ast = json.load(file)
    context_variables = {}
    tree = identify_type(ast)
    read_node(tree, context_variables)
