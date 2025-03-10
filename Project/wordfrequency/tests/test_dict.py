import io
import unittest
from unittest.mock import patch
import unittest    
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from WordCount.dict import WordCounter, generateHelpText, processArgv


class TestWordCounter(unittest.TestCase):
    def setUp(self):
        self.parameters = {
            '-s': True,
            '-f': False,
            '-p': '',
            '-pa': 0,
            '-pb': 0,
            #'Path': 'path/to/test/folder',
            'Path': './tests',
            '-csv': False
        }
        self.word_counter = WordCounter(self.parameters)

    def test_init(self):
        # Test if TypeError is raised when parameters is not a dict
        with self.assertRaises(TypeError):
            WordCounter(list(self.parameters))

    def test_collect_files(self):
        # Test if files are collected correctly
        self.word_counter.collect_files()
        self.assertGreater(len(self.word_counter.files), 0)

    def test_get_phrase_frequency(self):
        # Test if phrase frequency is calculated correctly
        self.word_counter.get_phrase_frequency('word', 1, 2)
        self.assertIn('word', self.word_counter.phrase_frequency_dict)

    def test_get_words(self):
        # Test if words are collected correctly
        self.word_counter.get_words()
        self.assertGreater(len(self.word_counter.words), 0)

class TestGenerateHelpText(unittest.TestCase):
    def test_generateHelpText_with_error_code_0(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            generateHelpText(0)
            self.assertEqual(fake_stdout.getvalue(), "USAGE: py dict.py [-pa <int>] [-pb <int>] [-p <phrase>] [-s <foldername> | -f <filename> | -h  ]\n-pa <int>    Count word after phrase\n-pb <int>    Count word before phrase\n-p <phrase>  Phrase\n")

    def test_generateHelpText_with_error_code_1(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            generateHelpText(1)
            self.assertEqual(fake_stdout.getvalue(), "Invalid format of input file path\n")

    def test_generateHelpText_with_error_code_7(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            generateHelpText(7)
            self.assertEqual(fake_stdout.getvalue(), "Numbers must be greater than zero\n")

    def test_processArgv_with_no_arg(self):
        with patch('sys.argv', ['dict.py']), self.assertRaises(SystemExit) as cm:
            processArgv()
        self.assertEqual(cm.exception.code, 6)

    def test_processArgv_with_wrong_parameter(self):
        with patch('sys.argv', ['dict.py','-a', '-s', '-f', '-p', '-pa', '-pb', '-wrong']), self.assertRaises(SystemExit) as cm:
            processArgv()
        self.assertEqual(cm.exception.code, 8)

if __name__ == '__main__':
    unittest.main()
