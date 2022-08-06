from attributes_doc import get_attributes_doc


class TestGetAttributesDoc(object):
    def test__no_doc_strings__no_doc_attributes(self):
        # arrange
        class Foo1(object):
            a = 1
            b = 2

        # act
        result = get_attributes_doc(Foo1)

        # assert
        assert result == {}

    def test__cls_with_doc_string__no_doc_attributes_for_fields(self):
        # arrange
        class Foo2(object):
            """Foo Doc"""

            a = 1
            b = 2

        # act
        result = get_attributes_doc(Foo2)

        # assert
        assert result == {}

    def test__cls_and_one_attr_with_doc_string__expected_doc_attributes_for_cls_and_one_field(
        self,
    ):
        # arrange
        class Foo3(object):
            """Foo Doc"""

            a = 1
            """a Doc"""

            b = 3

        # act
        result = get_attributes_doc(Foo3)

        # assert
        assert result == {"a": "a Doc"}

    def test__multiple_assignment__expected_one_doc_string_for_all_fields(self):
        # arrange
        class Foo4(object):
            a = b = 1
            """a Doc"""

            c = 3

        # act
        result = get_attributes_doc(Foo4)

        # assert
        assert result == {"a": "a Doc", "b": "a Doc"}

    def test__derived_classes(self):
        # arrange
        class Bar(object):
            a = 1
            """a Doc"""

            b = 2
            """b Doc"""

            c = 3
            """c Doc"""

        class BarChild(Bar):
            a = 5
            """a Doc 2"""

            c = 3

        # act
        result = get_attributes_doc(BarChild)

        # assert
        assert result == {"a": "a Doc 2", "b": "b Doc", "c": "c Doc"}
