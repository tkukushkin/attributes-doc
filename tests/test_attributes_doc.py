from attributes_doc import attributes_doc, getdoc


class TestAttributesDoc(object):
    def test__no_doc_strings__no_doc_attributes(self):
        # act
        @attributes_doc
        class Foo1(object):
            a = 1
            b = 2

        # assert
        assert not hasattr(Foo1, "__doc_a__")
        assert not hasattr(Foo1, "__doc_b__")

    def test__cls_with_doc_string__no_doc_attributes_for_fields(self):
        # act
        @attributes_doc
        class Foo2(object):
            """Foo Doc"""

            a = 1
            b = 2

        # assert
        assert Foo2.__doc__ == "Foo Doc"
        assert not hasattr(Foo2, "__doc_a__")
        assert getdoc(Foo2, "a") is None
        assert not hasattr(Foo2, "__doc_b__")
        assert getdoc(Foo2, "b") is None

    def test__cls_and_one_attr_with_doc_string__expected_doc_attributes_for_cls_and_one_field(
        self,
    ):
        # act
        @attributes_doc
        class Foo3(object):
            """Foo Doc"""

            a = 1
            """a Doc"""

            b = 3

        # assert
        assert Foo3.__doc__ == "Foo Doc"
        assert Foo3.__doc_a__ == "a Doc"
        assert getdoc(Foo3, "a") == "a Doc"
        assert not hasattr(Foo3, "__doc_b__")
        assert getdoc(Foo3, "b") is None

    def test__multiple_assignment__expected_one_doc_string_for_all_fields(self):
        # act
        @attributes_doc
        class Foo4(object):
            a = b = 1
            """a Doc"""

            c = 3

        # assert
        assert Foo4.__doc_a__ == "a Doc"
        assert getdoc(Foo4, "a") == "a Doc"
        assert Foo4.__doc_b__ == "a Doc"
        assert getdoc(Foo4, "b") == "a Doc"
        assert not hasattr(Foo4, "__doc_c__")
        assert getdoc(Foo4, "c") is None
