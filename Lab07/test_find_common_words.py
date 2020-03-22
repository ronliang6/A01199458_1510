import io
from unittest import TestCase
from unittest.mock import patch
import file_io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["The_Name_of_the_Wind.txt"])
    def test_find_common_words_file_non_existent(self, _, output):
        file_io.find_common_words()
        expected = """The file cannot be found.\n"""
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["alice.txt"])
    def test_find_common_words_alice(self, _, output):
        file_io.find_common_words()
        expected = """the - 1818
and - 940
to - 805
a - 690
of - 628
it - 580
she - 553
i - 542
you - 469
said - 457
"""
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["moby_dick.txt"])
    def test_find_common_words_moby_dick(self, _, output):
        file_io.find_common_words()
        expected = """the - 14613
of - 6725
and - 6502
a - 4797
to - 4701
in - 4222
that - 3067
his - 2522
it - 2412
i - 2117
"""
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["newfile.txt"])
    def test_find_common_words_one_word_file(self, _, output):
        file_io.find_common_words()
        expected = "hello - 1\n"
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["only_symbols.txt"])
    def test_find_common_words_file_only_symbols(self, _, output):
        file_io.find_common_words()
        expected = ""
        self.assertEqual(output.getvalue(), expected)

