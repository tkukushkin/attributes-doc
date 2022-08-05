import pytest
from attributes_doc import enum_doc

enum = pytest.importorskip("enum")


class TestEnumDoc(object):
    def test__no_doc_strings__no_doc_attributes(self):
        # act
        @enum_doc
        class Foo(enum.Enum):
            a = 1
            b = 2

        # assert
        assert Foo.a.__doc__ == Foo.__doc__
        assert Foo.b.__doc__ == Foo.__doc__

    def test__cls_with_doc_string__no_doc_attributes_for_fields(self):
        # act
        @enum_doc
        class Foo(enum.Enum):
            """Foo Doc"""

            a = 1
            b = 2

        # assert
        assert Foo.__doc__ == "Foo Doc"
        assert Foo.a.__doc__ == "Foo Doc"
        assert Foo.b.__doc__ == "Foo Doc"

    def test__cls_and_one_attr_with_doc_string__expected_doc_attributes_for_cls_and_one_field(
        self,
    ):
        # act
        @enum_doc
        class Foo(enum.Enum):
            """Foo Doc"""

            a = 1
            """a Doc"""

            b = 3

        # assert
        assert Foo.__doc__ == "Foo Doc"
        assert Foo.a.__doc__ == "a Doc"
        assert Foo.b.__doc__ == "Foo Doc"

    def test__multiple_assignment__expected_one_doc_string_for_all_fields(self):
        # act
        @enum_doc
        class Foo(enum.Enum):
            a = b = 1
            """a Doc"""

            c = 3

        # assert
        assert Foo.a.__doc__ == "a Doc"
        assert Foo.b.__doc__ == "a Doc"
        assert Foo.c.__doc__ == Foo.__doc__
