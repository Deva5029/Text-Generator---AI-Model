import os
import unittest    
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from WordCount.dict import WordCounter

TEST_FOLDER = os.path.join('tests')
TEST_FILES = os.path.join(TEST_FOLDER, 'test_files')
FILE_LIST = os.path.join(TEST_FOLDER, 'file_list.txt')
FILE1 = os.path.join(TEST_FILES, 'file1.txt')
FILE2 = os.path.join(TEST_FILES, 'file2.txt')
FILE3 = os.path.join(TEST_FILES, 'file3.txt')
FILE11 = os.path.join(TEST_FILES, 'subfolder', 'file11.txt')


class TestWordCounter(unittest.TestCase):
    parameters = {
    '-s': False,
    '-f': False,
    '-p': "",
    '-pa': 0,
    '-pb': 0,
    'Path': TEST_FILES,
    '-csv': False
    }
    word_counter = WordCounter(parameters)


    def test_collect_files(self):
        self.word_counter.collect_files()
        self.assertEqual(len(self.word_counter.files), 3)
        self.assertIn(FILE1, self.word_counter.files)
        self.assertIn(FILE2, self.word_counter.files)
        self.assertIn(FILE3, self.word_counter.files)

    def test_get_phrase_frequency(self):
        self.word_counter.collect_files()
        self.word_counter.get_phrase_frequency(' test', count_before=0, count_after=0)
        self.assertEqual(self.word_counter.phrase_frequency_dict, {' test': 3})

    def test_get_phrase_frequency2(self):
        parameters = {'-s': False, '-f': False, '-p': None, '-pa': 0, '-pb': 0, 'Path': TEST_FILES, '-csv': False}
        wc = WordCounter(parameters)
        wc.files = [FILE11]
        wc.get_words()
        wc.get_phrase_frequency('test subfolder for tests')
        expected_dict = {' test subfolder for tests': 1}
        self.assertDictEqual(wc.phrase_frequency_dict, expected_dict)

    def test_get_words(self):
        self.word_counter.collect_files()
        self.word_counter.get_words()
        self.assertEqual(len(self.word_counter.words), 15)

    def test_get_words2(self):
        parameters = {'-s': False, '-f': False, '-p': None, '-pa': 0, '-pb': 0, 'Path': TEST_FILES, '-csv': False}
        wc = WordCounter(parameters)
        wc.files = [FILE1, FILE2]
        wc.get_words()
        expected_words = ["test", "word", "frequency", "count", "this", "test", "word", "frequency", "count", "this"]
        self.assertCountEqual(wc.words, expected_words)

    def test_get_words_dict(self):
        self.word_counter.collect_files()
        self.word_counter.get_words_dict()
        self.assertEqual(self.word_counter.words_dict, {'test': 3, 'word': 3, 'frequency': 3, 'count': 3, 'this': 3})

    def test_get_words_dict2(self):
        parameters = {'-s': False, '-f': False, '-p': None, '-pa': 0, '-pb': 0, 'Path': TEST_FILES, '-csv': False}
        wc = WordCounter(parameters)
        wc.files = [FILE1, FILE2, FILE3]
        wc.get_words()
        wc.get_words_dict()
        expected_dict = {'test': 3, 'word': 3, 'frequency': 3, 'count': 3, 'this': 3}
        self.assertDictEqual(wc.words_dict, expected_dict)    

    def test_invalid_parameters(self):
        with self.assertRaises(TypeError):
            self.word_counter('invalid')

    def test_collect_files_with_subfolders(self):
        parameters = {'-s': True, '-f': False, '-p': None, '-pa': 0, '-pb': 0, 'Path': TEST_FILES, '-csv': False}
        wc = WordCounter(parameters)
        wc.collect_files()
        expected_files = [FILE1, FILE2, FILE3, FILE11]
        self.assertCountEqual(wc.files, expected_files)

    def test_collect_files_without_subfolders(self):
        parameters = {'-s': False, '-f': False, '-p': None, '-pa': 0, '-pb': 0, 'Path': TEST_FILES, '-csv': False}
        wc = WordCounter(parameters)
        wc.collect_files()
        expected_files = [FILE1, FILE2,FILE3]
        self.assertCountEqual(wc.files, expected_files)

    def test_collect_files_with_file_list(self):
        parameters = {'-s': False, '-f': True, '-p': None, '-pa': 0, '-pb': 0, 'Path': FILE_LIST, '-csv': False}
        wc = WordCounter(parameters)
        wc.collect_files()
        expected_files = [FILE1, FILE2]
        self.assertCountEqual(wc.files, expected_files)

if __name__ == '__main__':
    unittest.main()
