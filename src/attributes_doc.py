import ast
import sys
import inspect
import textwrap
from typing import Dict, Type, TypeVar, Tuple


__all__ = ['get_attributes_doc', 'attributes_doc']

PY35 = sys.version_info[0:2] >= (3, 5)

T = TypeVar('T')

assign_stmts = (ast.Assign, )  # type: Tuple[Type[ast.stmt], ...]
if PY35:
    assign_stmts = (ast.Assign, ast.AnnAssign)


class FStringFound(Exception):
    pass


def get_attributes_doc(cls):
    # type: (type) -> Dict[str, str]
    result = {}  # type: Dict[str, str]
    for parent in reversed(cls.mro()):
        try:
            source = inspect.getsource(parent)
        except TypeError:
            continue
        source = textwrap.dedent(source)
        module = ast.parse(source)
        cls_ast = module.body[0]
        for stmt1, stmt2 in zip(cls_ast.body, cls_ast.body[1:]):  # type: ignore
            if (
                    not isinstance(stmt1, assign_stmts)
                    or not isinstance(stmt2, ast.Expr)
            ):
                continue
            doc_expr_value = stmt2.value
            if PY35 and isinstance(doc_expr_value, ast.JoinedStr):
                raise FStringFound
            if isinstance(doc_expr_value, ast.Str):
                if PY35 and isinstance(stmt1, ast.AnnAssign):
                    attr_names = [stmt1.target.id]  # type: ignore
                else:
                    attr_names = [target.id for target in stmt1.targets]  # type: ignore
                for attr_name in attr_names:
                    result[attr_name] = doc_expr_value.s
    return result


def attributes_doc(cls):
    # type: (Type[T]) -> Type[T]
    for attr_name, attr_doc in get_attributes_doc(cls).items():
        setattr(cls, '__doc_%s__' % attr_name, attr_doc)
    return cls
