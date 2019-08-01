import ast
import inspect
import textwrap
from typing import Dict, Type, TypeVar


__all__ = ['get_attributes_doc', 'attributes_doc']

T = TypeVar('T')


class FStringFound(Exception):
    pass


def get_attributes_doc(cls):
    # type: (type) -> Dict[str, str]
    source = inspect.getsource(cls)
    source = textwrap.dedent(source)
    module = ast.parse(source)
    cls_ast = module.body[0]
    result = {}  # type: Dict[str, str]
    for stmt1, stmt2 in zip(cls_ast.body, cls_ast.body[1:]):
        if (
                not isinstance(stmt1, (ast.AnnAssign, ast.Assign))
                or not isinstance(stmt2, ast.Expr)
        ):
            continue
        doc_expr_value = stmt2.value
        if isinstance(doc_expr_value, ast.JoinedStr):
            raise FStringFound
        if isinstance(doc_expr_value, ast.Str):
            if isinstance(stmt1, ast.AnnAssign):
                attr_names = [stmt1.target.id]
            else:
                attr_names = [target.id for target in stmt1.targets]
            for attr_name in attr_names:
                result[attr_name] = doc_expr_value.s
    return result


def attributes_doc(cls):
    # type: (Type[T]) -> Type[T]
    for attr_name, attr_doc in get_attributes_doc(cls).items():
        setattr(cls, f'__doc_{attr_name}__', attr_doc)
    return cls
