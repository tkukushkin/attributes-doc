import pytest

from attributes_doc import attributes_doc, enum_doc


enum = pytest.importorskip("enum")


class TestEnumDoc(object):
    def test__no_doc_strings__no_doc_attributes(self):
        # act
        @attributes_doc
        @enum_doc
        class Foo1(enum.Enum):
            a = 1
            b = 2

        # assert
        assert Foo1.a.__doc__ == Foo1.__doc__
        assert not hasattr(Foo1, "__doc_a__")
        assert Foo1.b.__doc__ == Foo1.__doc__
        assert not hasattr(Foo1, "__doc_b__")

    def test__cls_with_doc_string__no_doc_attributes_for_fields(self):
        # act
        @attributes_doc
        @enum_doc
        class Foo2(enum.Enum):
            """Foo2 Doc"""

            a = 1
            b = 2

        # assert
        assert Foo2.__doc__ == "Foo2 Doc"
        assert Foo2.a.__doc__ == "Foo2 Doc"
        assert not hasattr(Foo2, "__doc_a__")
        assert Foo2.b.__doc__ == "Foo2 Doc"
        assert not hasattr(Foo2, "__doc_b__")

    def test__cls_and_one_attr_with_doc_string__expected_doc_attributes_for_cls_and_one_field(
        self,
    ):
        # act
        @attributes_doc
        @enum_doc
        class Foo3(enum.Enum):
            """Foo3 Doc"""

            a = 1
            """a Doc"""

            b = 3

        # assert
        assert Foo3.__doc__ == "Foo3 Doc"
        assert Foo3.a.__doc__ == "a Doc"
        assert Foo3.__doc_a__ == "a Doc"
        assert Foo3.b.__doc__ == "Foo3 Doc"
        assert not hasattr(Foo3, "__doc_b__")

    def test__multiple_assignment__expected_one_doc_string_for_all_fields(self):
        # act
        @attributes_doc
        @enum_doc
        class Foo4(enum.Enum):
            a = b = 1
            """a Doc"""

            c = 3

        # assert
        assert Foo4.a.__doc__ == "a Doc"
        assert Foo4.__doc_a__ == "a Doc"
        assert Foo4.b.__doc__ == "a Doc"
        assert Foo4.__doc_b__ == "a Doc"
        assert Foo4.c.__doc__ == Foo4.__doc__
        assert not hasattr(Foo4, "__doc_c__")
