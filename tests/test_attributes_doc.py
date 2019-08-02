from attributes_doc import attributes_doc, get_attributes_doc


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

    def test__cls_and_one_attr_with_doc_string__expected_doc_attributes_for_cls_and_one_field(self):
        # arrange
        class Foo3(object):
            """Foo Doc"""

            a = 1
            """a Doc"""

            b = 3

        # act
        result = get_attributes_doc(Foo3)

        # assert
        assert result == {'a': 'a Doc'}

    def test__multiple_assignment__expected_one_doc_string_for_all_fields(self):
        # arrange
        class Foo4(object):
            a = b = 1
            """a Doc"""

            c = 3

        # act
        result = get_attributes_doc(Foo4)

        # assert
        assert result == {'a': 'a Doc', 'b': 'a Doc'}

    def test__nested_classes(self):
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
        assert result == {'a': 'a Doc 2', 'b': 'b Doc', 'c': 'c Doc'}


class TestAttributesDoc(object):

    def test__no_doc_strings__no_doc_attributes(self):
        # act
        @attributes_doc
        class Foo5(object):
            a = 1
            b = 2

        # assert
        assert not hasattr(Foo5, '__doc_a__')
        assert not hasattr(Foo5, '__doc_b__')

    def test__cls_with_doc_string__no_doc_attributes_for_fields(self):
        # act
        @attributes_doc
        class Foo6(object):
            """Foo Doc"""
            a = 1
            b = 2

        # assert
        assert Foo6.__doc__ == 'Foo Doc'
        assert not hasattr(Foo6, '__doc_a__')
        assert not hasattr(Foo6, '__doc_b__')

    def test__cls_and_one_attr_with_doc_string__expected_doc_attributes_for_cls_and_one_field(self):
        # act
        @attributes_doc
        class Foo7(object):
            """Foo Doc"""

            a = 1
            """a Doc"""

            b = 3

        # assert
        assert Foo7.__doc__ == 'Foo Doc'
        assert Foo7.__doc_a__ == 'a Doc'
        assert not hasattr(Foo7, '__doc_b__')

    def test__multiple_assignment__expected_one_doc_string_for_all_fields(self):
        # act
        @attributes_doc
        class Foo8(object):
            a = b = 1
            """a Doc"""

            c = 3

        # assert
        assert Foo8.__doc_a__ == 'a Doc'
        assert Foo8.__doc_b__ == 'a Doc'
        assert not hasattr(Foo8, '__doc_c__')
