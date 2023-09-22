from typing import Callable, Dict, List
from dataclasses import dataclass

# Term = Dict


@dataclass
class Loc:
    start: int
    end: int
    filename: str


@dataclass
class Term:
    kind: str
    location: Loc


@dataclass
class Parameter:
    text: str
    location: Loc


@dataclass
class Let(Term):
    name: Parameter
    value: Term
    next: Term


@dataclass
class Str(Term):
    value: str


@dataclass
class Bool(Term):
    value: bool


@dataclass
class Int(Term):
    value: int


def Add(x, y):
    if isinstance(x, bool):
        x = str(x).lower()
    if isinstance(y, bool):
        y = str(y).lower()
    if isinstance(x, str) or isinstance(y, str):
        return f"{str(x)}{str(y)}"
    return x + y
Sub = lambda x, y: x - y
Mul = lambda x, y: x * y
Div = lambda x, y: x / y
Rem = lambda x, y: x % y
Eq = lambda x, y: x == y
Neq = lambda x, y: x != y
Lt = lambda x, y: x < y
Gt = lambda x, y: x > y
Lte = lambda x, y: x <= y
Gte = lambda x, y: x >= y
And = lambda x, y: x and y
Or = lambda x, y: x or y
BinaryOp = {
    "Add": Add,
    "Sub": Sub,
    "Mul": Mul,
    "Div": Div,
    "Rem": Rem,
    "Eq": Eq,
    "Neq": Neq,
    "Lt": Lt,
    "Gt": Gt,
    "Lte": Lte,
    "Gte": Gte,
    "And": And,
    "Or": Or,
}


@dataclass
class File:
    name: str
    expression: Term
    location: Loc


@dataclass
class If(Term):
    condition: Term
    then: Term
    otherwise: Term


@dataclass
class Binary(Term):
    lhs: Term
    op: Callable
    rhs: Term


@dataclass
class Call(Term):
    callee: Term
    arguments: List[Term]


@dataclass
class Function(Term):
    parameters: List[Parameter]
    value: Term


@dataclass
class PrintFunction(Term):
    value: Term


@dataclass
class FirstFunction(Term):
    value: Term


@dataclass
class SecondFunction(Term):
    value: Term


@dataclass
class Tuple(Term):
    first: Term
    second: Term


@dataclass
class Var(Term):
    text: str
