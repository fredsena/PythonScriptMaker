import unittest

from Utils.StringBuilder import StringBuilder


class StringBuilderTests(unittest.TestCase):
    def test_append_WhenTextIsAppended_ReturnText(self):
        builder = StringBuilder()
        builder.append('test')
        self.assertEqual('test', builder.to_string())

    def test_append_WhenTextsAreAppended_ReturnTexts(self):
        builder = StringBuilder()
        builder.append('test1')
        builder.append('test2')
        self.assertEqual('test1test2', builder.to_string())

    def test_append_line_WhenTextIsLineAppended_ReturnText(self):
        builder = StringBuilder()
        builder.append_line('test1')
        builder.append_line('test2')
        self.assertEqual('test1\r\ntest2\r\n', builder.to_string())

    def test_replace_WhenTextIsReplaced_ReturnReplacedText(self):
        builder = StringBuilder()
        builder.append('test1')
        builder.append('test2')
        builder.replace('test2', 'test3')
        self.assertEqual('test1test3', builder.to_string())

    def test_StringBuilder_WhenTextIsNotString_RaisesTypeError(self):
        with self.assertRaises(TypeError):
            builder = StringBuilder(10)

    def test_append_ZZZ_WhenTextsAreAppended_ReturnTexts(self):
        builder = StringBuilder('test1')
        test_data = ["t1"]

        for data in test_data:
            with self.subTest(data=data):
                builder.append(data)
                self.assertEqual(builder.to_string(), 'test1t1')


if __name__ == "__main__":
    unittest.main(verbosity=2)
