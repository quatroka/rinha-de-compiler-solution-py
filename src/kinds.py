from typing import Callable, Dict, List
from dataclasses import dataclass

Term = Dict


@dataclass
class Loc:
    start: int
    end: int
    filename: str


@dataclass
class Parameter:
    text: str
    location: Loc


@dataclass
class Let:
    kind: str
    name: Parameter
    value: Term
    next: Term
    location: Loc


@dataclass
class Str:
    kind: str
    value: str
    location: Loc


@dataclass
class Bool:
    kind: str
    value: bool
    location: Loc


@dataclass
class Int:
    kind: str
    value: int
    location: Loc


Add = lambda x, y: x + y
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
class If:
    kind: str
    condition: Term
    then: Term
    otherwise: Term
    location: Loc


@dataclass
class Binary:
    kind: str
    lhs: Term
    op: Callable
    rhs: Term
    location: Loc


@dataclass
class Call:
    kind: str
    callee: Term
    arguments: List[Term]
    location: Loc


@dataclass
class Function:
    kind: str
    parameters: List[Term]
    value: Term
    location: Loc


@dataclass
class PrintFunction:
    kind: str
    value: Term
    location: Loc


@dataclass
class FirstFunction:
    kind: str
    value: Term
    location: Loc


@dataclass
class SecondFunction:
    kind: str
    value: Term
    location: Loc


@dataclass
class Tuple:
    kind: str
    first: Term
    second: Term
    location: Loc


@dataclass
class Parameter:
    text: str
    location: Loc


@dataclass
class Var:
    kind: str
    text: str
    loc: Loc


ValueTypes = Str | Int | Bool
PermittedTerms = Int | Str | Call | Binary | Function | Let | If | PrintFunction | FirstFunction | SecondFunction | Bool | Tuple | Var
