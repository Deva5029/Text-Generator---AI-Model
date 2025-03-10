## Name
WordCount

This project description can be found in the issue called Epics

This project features can be found in the issues starting with FEATURE _xxxx

This project user stories are regular issues 

The roadmap is presented by the milestones

# Project structure

```

esl_master/
│
├── ESL_Master/ 
│   ├── retrieve_dictionary_info /
│   │   ├── src/ 
│   │   │   ├── main.py 
│   │   │   └── ... 
│   │   ├── .gitignore 
│   │   ├── requirements.txt 
│   │   └── ... 
│   │ 
│   ├── retrieve_translations_based_on_document /
│   │   ├── src/ 
│   │   │   ├── main.py 
│   │   │   └── ... 
│   │   ├── .gitignore 
│   │   ├── requirements.txt 
│   │   └── ... 
│   │ 
│   ├── simplify_contextual_example /
│   │   ├── src/ 
│   │   │   ├── main.py 
│   │   │   └── ... 
│   │   ├── .gitignore 
│   │   ├── requirements.txt 
│   │   └── ... 
│   │ 
│   ├── retrieve_document_examples /
│   │   ├── src/ 
│   │   │   ├── main.py 
│   │   │   └── ... 
│   │   ├── .gitignore 
│   │   ├── requirements.txt 
│   │   └── ... 
│   │ 
│   ├── generate_contextual_examples /
│   │   ├── src/ 
│   │   │   ├── main.py 
│   │   │   └── ... 
│   │   ├── .gitignore 
│   │   ├── requirements.txt 
│   │   └── ... 
│   │ 
│   ├── check_spelling /
│   │   ├── src/ 
│   │   │   ├── main.py 
│   │   │   └── ... 
│   │   ├── .gitignore 
│   │   ├── requirements.txt 
│   │   └── ... 
│   │ 
│   ├── generate_contextual_examples_with_vocabulary /
│   │   ├── src/ 
│   │   │   ├── main.py 
│   │   │   └── ... 
│   │   ├── .gitignore 
│   │   ├── requirements.txt 
│   │   └── ... 
│   └── ... 
│
├── WordCount/
│   ├── __init__.py
│   ├── Validator/
│   │   ├── __init__.py
│   │   └── Validator.py
│   ├── dict.py
│   ├── list_of_files.txt
│   └── stop_words.txt
│
├── tests/ 
│   ├── tests_retrieve_dictionary_info / 
│   │   ├── conftest.py 
│   │   ├── test_*.py 
│   │   └── ... 
│   │
│   ├── tests_retrieve_translations_based_on_document / 
│   │   ├── conftest.py 
│   │   ├── test_*.py 
│   │   └── ... 
│   │ 
│   ├── tests_generate_contextual_examples / 
│   │   ├── conftest.py 
│   │   ├── test_*.py 
│   │   └── ... 
│   │
│   ├── tests_simplify_contextual_example / 
│   │   ├── conftest.py 
│   │   ├── test_*.py 
│   │   └── ...
│   ├── tests_retrieve_document_examples / 
│   │   ├── conftest.py 
│   │   ├── test_*.py 
│   │   └── ... 
│   ├── tests_check_spelling / 
│   │   ├── conftest.py 
│   │   ├── test_*.py 
│   │   └── ...
│   ├── tests_generate_contextual_examples_with_vocabulary / 
│   │   ├── conftest.py 
│   │   ├── test_*.py 
│   │   └── ...
│   │ 
│   ├── test_files/
│   │   ├── subfolder/
│   │   │   └── file11.txt
│   │   ├── file1.txt
│   │   ├── file2.txt
│   │   └── file3.txt
│   ├── file_list.txt
│   ├── test_dict.txt
│   └──test_integration_dict.py
│
├── .gitignore
├── .gitlab-ci.yml
├── Architectual&CodingGuidelines
├── requirements.txt
├── LICENSE
├── CONTRIBUTING.md
├── README.md
└── setup.py


```
## Description
WordCount is an application that helps people learn new vocabulary. The system provides an interface used to load given set of txt-files and can analyze that set. 

The application has the following features:
1. Get words frequency analyzis within set of files.
2. Get specific phrase analyzis within set of files.
3. Get phrase analyzis(phrase +- number of words specified) within set of files.

The interface is chosen to be CLI at this moment, having both interactive and manual modes. The executable can take a variety of parameters, each describes options that can be applied during run.

Here are the list of that options:
1. The system is able to collect files within the list of files' paths given or by providing a path to the directory with files.
If the file option has been chosen, then all paths in the file given should have .txt extension. If the file option not chosen, directory option is default.
2. If the directory option applied, the system has option to search files through subfolders or user can choose not to. Default value is no to search through subfolders in given directory.
3. It is not allowed to have both file and subfolder options applied. They are mutually excluding.
4. The system is capable of phrase analyzis. It is possible to specify phrase, amount of words before and after the phrase. It is not allowed to specify amount of words before\after the phrase if no phrase given.
5. As a result of work, the application generates report with data it received. It consists of list of files analyzed, words and phrase analyzis. The system has 2 formats of report generation: txt and csv. 

## Installation
This project is being developed using Python 3.10.
In order to prevent version error run

        python --version

in your terminal. Make sure it outputs Python 3.10.x

To run this project ensure you have installed python packages used for development, testing and build.
In order to prevent import-related errors run

        pip install -r requirements.txt

If you installed all needed dependencies - you now can run project via terminal or build executable.
To build executable, open terminal, go to WordCount\build\<your operating system> and run build.sh. This should create an executable of for a needed operating system. If you successfully built executable, you now can launch it in interactive mode or continue using in manual.


## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

USAGE: [py dict.py | <executable call>] [-p <phrase> [-pa <int>] [-pb <int>] ]  [-csv] [-s <foldername> | -f <filename> | -h ]

Examples:
    1. Generate phrase analyzis in csv format for phrase "Hello World" in set of text files in the "C:\users\user\documents" folder searching through subfolders of that directory. 

        py dict.py -p "Hello World" -csv -s "C:\users\user\documents"
    
    2. Generate phrase analyzis in text format for phrases "Hello" and one word before the given in set of text files in the "C:\users\user\documents" folder not searching through subfolders of that directory. 

        py dict.py -p "Hello" -pb 1 "C:\users\user\documents"
    
    3. Generate word analyzis in csv format in set of text files in the "C:\users\user\documents\files_list.txt" file.

        py dict.py -csv -f "C:\users\user\documents\files_list.txt"
        
## Support
If you have any questions prior to issues, or problems related to project, you can contact repository administrator at 
maksym.yaremenko@mask-me.net

## Roadmap
Currently we are following goals below:
0. Fix tests, finish CI pipeline.
1. Create the tts module so that user could listen to the proper pronuciation of the word or phrase.
2. Create the stt module so that user could check whether they pronouce word or phrase correctly.
3. Create the quiz module so that user could get and answer questions based on vocabulary currently loaded both using text and speech.
4. Create web interface so that user could use application via web browser.
5. Create mobile interface so that user could use application via smartphone.

## Contributing

We are looking forward for new contributors if you meet the requirements we set. 
To see detailed document read contributing.md

## Authors and acknowledgment
The initial project's author HushHush.

## License
WordCount, an application that helps learn vocabulary
Copyright (C) 2023  HushHush

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

For more detailed info read license.md
