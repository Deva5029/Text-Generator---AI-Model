import csv
import os
import datetime
import sys

class WordCounter:

    def __init__(self, parameters):
        if type(parameters) != dict:
            raise TypeError
        self.read_subfolders = parameters['-s']
        self.list_of_files_in_file = parameters['-f']
        self.phrase = parameters['-p']
        self.phrase_frequency_dict={}
        # self.stop_words_flag = parameters['-a']
        self.count_after = parameters['-pa']
        self.count_before = parameters['-pb']
        self.path = parameters['Path']
        self.words = []
        self.files = []
        self.words_dict = dict()
        self.error_files = []
        self.stop_words = []
        self.stop_words_path = os.getcwd()+"/stop_words.txt"
        self.csv_report = parameters['-csv']
    
    def collect_files(self):
        self.files = []
        if self.list_of_files_in_file:
            if not os.path.exists(self.path):
                self.error_files.append(self.path + " : not open \n")
            # elif not self.path:

            else:
                with open(self.path, encoding="utf8") as file:  
                    text = file.readlines()
                for line in text:
                    if line[-1]=="\n":
                        self.files.append(line[:-1])
                    else:
                        self.files.append(line)
        elif self.read_subfolders:
            #Collect files reading subfolders
            for root, dirs, files in os.walk(self.path):
                for file in files:
                    if file.endswith(".txt"):
                        self.files.append(os.path.join(root, file))
        else:
            #Collect files without reading subfolders
            if not os.path.exists(self.path):
                self.error_files.append(self.path + " : not open \n")
            elif self.path.endswith(".txt") :
                    self.files.append(self.path)
            else:
                for file in os.listdir(self.path):
                    if file.endswith(".txt"):
                        self.files.append(os.path.join(self.path, file))
    
    def get_phrase_frequency(self, word, count_before = 0, count_after = 0):
        #get a dictionary of all phrase with a given characteristic from files
        if self.words == []:
            self.get_words()

        if  ' ' in word or (count_before > 0 or count_after > 0):
            phrase_list = []
            word = word.lower()
            s1 = word.encode('ascii', errors='ignore').decode('ascii')
            phrase_list += s1.split()
            self.phrase_frequency_dict={}
            flag = False
           
            for index in range(count_before, len(self.words) - count_after):
                for i in range(len(phrase_list)):
                    if self.words[index+i] == phrase_list[i]:
                        flag = True
                    else: 
                        flag = False
                        break
                 
                if flag:    
                        phrase = ""
                        for i in range(index - count_before, index + count_after + len(phrase_list)):  
                            phrase += " "
                            phrase += self.words[i] 
                
                        if phrase in self.phrase_frequency_dict:
                            self.phrase_frequency_dict[phrase] += 1
                        else:
                            self.phrase_frequency_dict[phrase] = 1
            self.sort_by_values_phrase()
            if self.phrase_frequency_dict == {}:
                phrase = ""
                for el in phrase_list:
                    phrase += el 
                    phrase += " "
                self.phrase_frequency_dict[phrase] = 0
            
        else:
            if self.words_dict == {}:
                self.get_words_dict()

            if word in self.phrase_frequency_dict:
                self.phrase_frequency_dict[word] = self.words_dict[word]
            else:
                self.phrase_frequency_dict[word] = 0
   
    def get_words(self):
        #get a list of all words from files

        words_list=[]
        self.words=[]

        for filename in self.files:
            if not os.path.exists(filename):
                self.error_files.append(filename+" : not open \n")
            elif filename[-4:] != ".txt":
                self.error_files.append(filename+" : not corect format \n")

            else:
                with open(filename, encoding="utf8") as file:
                    text = file.read()

                text = text.replace("\n", " ")
                text = text.replace(",", " ").replace(".", " ").replace("?", " ").replace("!", " ").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("0", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("(", "").replace(")", "").replace("_", "").replace("+", "").replace("=", "").replace(":", "").replace(";", "").replace("'", "").replace('"', "").replace("•", "").replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace('/',' ').replace('\\',' ')
                text = text.lower()
                s1 = text.encode('ascii', errors='ignore').decode('ascii')
                words_list+=s1.split()

        for word in words_list:
            if word not in self.stop_words and word != "-":
                self.words.append(word)
    
    def get_words_dict(self):
        #get a dictionary of all words from files

        self.words_dict = dict()
    
        for word in self.words:
            if word in self.words_dict:
                self.words_dict[word] = self.words_dict[word] + 1

            else:
                self.words_dict[word] = 1

        self.sort_by_values()
 
    def sort_by_values(self):
        #sort dictionary by values

        sorted_dict = {}
        sorted_keys = sorted(self.words_dict, key=self.words_dict.get,reverse = True)  

        for w in sorted_keys:
            sorted_dict[w] = self.words_dict[w]

        self.words_dict = sorted_dict 

    def sort_by_values_phrase(self):
        #sort phrase dictionary by values

        sorted_dict = {}
        sorted_keys = sorted(self.phrase_frequency_dict, key = self.phrase_frequency_dict.get, reverse = True)  

        for w in sorted_keys:
            sorted_dict[w] = self.phrase_frequency_dict[w]
        self.phrase_frequency_dict = sorted_dict    
  
    def update_run_number(self, filename):
        #program run number definition

        if not os.path.exists(filename):
            return 1 

        else:
            with open(filename, encoding="utf8") as file:
                file.read(12)
                text=file.readline()

                if text == '\n':
                    return 1
                else:    
                    return int(text) + 1

    def get_run_number(self, filename):
        if not os.path.exists(filename):
            return 1 
        with open(filename, encoding="utf8") as file:
                file.read(12)
                text=file.readline()
                if text == '\n':
                    return 1
                return int(text)
                
    def collect_stop_words(self):
        if not os.path.exists(self.stop_words_path):
            self.error_files.append(self.stop_words_path + " : not open \n")
        else:
            with open(self.stop_words_path) as file:
                text = file.read()
            text = text.replace("\n", " ")
            self.stop_words=text.split()
    
    def create_report(self, timestamp, run_number):
        if run_number == 0:
            REPORT_DIR = os.getcwd() + "/Report"
        else:
            REPORT_DIR = os.getcwd() + "/Report " + str(run_number)
        error_filename = REPORT_DIR + "/error_file.txt"    
        # stop_filename=os.getcwd()+"/Report/stop.txt"
        words_filename = REPORT_DIR + "/words.txt"
        phrase_frequency_filename = REPORT_DIR + "/phrase_frequency.txt"
        files_filename = REPORT_DIR + "/list_of_files.txt"
        run = self.update_run_number(words_filename)

        if not os.path.isdir(REPORT_DIR):
            os.mkdir(REPORT_DIR)

        with open(words_filename.replace("\\", "/"), "w", encoding="utf8" ) as file: 
            file.write("run number: "+str(run)+"\n")
            file.write("data: "+str(timestamp)+"\n\n")
            for word in self.words_dict:
                file.write(str(word)+" : "+str(self.words_dict[word])+"\n")
                
        with open(error_filename, "w", encoding="utf8" ) as file:
            for error in self.error_files:
                file.write(os.getcwd() + "\\" + error.replace("/", "\\") + "\n")
        
        with open(files_filename, "w", encoding="utf8" ) as file:
            for filename in self.files:
                file.write(filename.replace("/", "\\") + "\n")
        with open(phrase_frequency_filename, "w", encoding="utf8") as file:
            for word in self.phrase_frequency_dict:
                file.write(str(word) + " : " + str(self.phrase_frequency_dict[word]) + "\n")

    

    def create_csv_report(self, timestamp, run_number):
        if run_number == 0:
            report_dir = os.getcwd() + "/Report"
        else:
            report_dir = os.getcwd() + "/Report " + str(run_number)

        if not os.path.isdir(report_dir):
            os.mkdir(report_dir)

        # Write words data to CSV
        words_filename = os.path.join(report_dir, "words.csv")
        with open(words_filename, mode="w", encoding="utf-8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["word", "frequency", "run number", "datetime",])
            for word, freq in self.words_dict.items():
                writer.writerow([word, freq, run_number, timestamp,])

        # Write error files data to CSV
        error_filename = os.path.join(report_dir, "error_file.csv")
        with open(error_filename, mode="w", encoding="utf-8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["error_file"])
            for error in self.error_files:
                writer.writerow([error])

        # Write phrase frequency data to CSV
        phrase_frequency_filename = os.path.join(report_dir, "phrase_frequency.csv")
        with open(phrase_frequency_filename, mode="w", encoding="utf-8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["phrase", "frequency"])
            for phrase, freq in self.phrase_frequency_dict.items():
                writer.writerow([phrase, freq])

        # Write list of files data to CSV
        files_filename = os.path.join(report_dir, "list_of_files.csv")
        with open(files_filename, mode="w", encoding="utf-8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["file"])
            for filename in self.files:
                writer.writerow([filename])
            
    def generate_report(self, run_number=0):
        now = datetime.datetime.now()
        self.collect_files()
        self.collect_stop_words()
        self.get_words()
        self.get_words_dict()
        if self.phrase:
            self.get_phrase_frequency(self.phrase,self.count_before, self.count_after)
        if run_number == 0:
            print("Operations were successfull, generating report in /Report directory.")
        else:
            print("Operations were successfull, generating report in /Report "+str(run_number)+" directory.")
        
        if self.csv_report:
            self.create_csv_report(now, run_number)
        else:
            self.create_report(now, run_number)

def generateHelpText(errorCode):
    if errorCode == 0:
        print("USAGE: py dict.py [-pa <int>] [-pb <int>] [-p <phrase>] [-s <foldername> | -f <filename> | -h  ]")
        print("-pa <int>    Count word after phrase")
        print("-pb <int>    Count word before phrase")
        print("-p <phrase>  Phrase")

    elif errorCode == 1:
        print("Invalid format of input file path")
    elif errorCode == 2:
        print("Invalid format of input directory path")
    elif errorCode == 3:
        print("Unexpected parameter '-h'. '-h' is only usable without any positional arguments. Exiting with error.")
    elif errorCode == 4:
        print("Unexpected amount of positional arguments: system can only take up to 4 positional arguments, more were given. Exiting with error.")
    elif errorCode == 5:
        print("Unexpected parameter '-s' together with '-f'. Parameters '-f' and '-s' are mutually exclusive. Exiting with error.")
    elif errorCode == 6:
        print("Unexpected amount of positional arguments: at least 1 expected, 0 given")
    elif errorCode == 7:
        print("Argument must be greater than zero")
    elif errorCode == 8:
        print("Wrong parameter")
    elif errorCode == 9:
        print("Not valid filename")
    elif errorCode == 10:
        print("Cannot create report")
    elif errorCode == 11:
        print("'-pa' or '-pb' cannot use without '-p'")
    elif errorCode == 12:
        print("Unexpected argument")

def processArgv():

    args_dict = {}
    args_dict['Path'] = None
    args_dict['-a'] = False
    args_dict['-s'] = False
    args_dict['-f'] = False
    args_dict['-p'] = False  
    args_dict['-pa'] = False 
    args_dict['-pb'] = False 
    args_dict['-csv'] = False

    if '-p' in sys.argv :
        word_list = []
        arg = sys.argv[sys.argv.index('-p') + 1]
        if "-" == arg[0]:
            error = 12
            generateHelpText(error)
            exit(error) 
        
        if len(sys.argv) > sys.argv.index('-p') + 2:
            for word in range (sys.argv.index('-p') + 2, len(sys.argv)):
                if '-' in sys.argv[word][0] or sys.argv[word].endswith('.txt') or os.path.exists(sys.argv[word]) :
                    break
                else:
                    arg += ' '
                    arg += sys.argv[word]
                    word_list.append(sys.argv[word])
            for el in word_list:
                sys.argv.remove(el)
            sys.argv[sys.argv.index('-p') + 1] = arg
            args_dict['-p'] = arg

 

    if '-pa' in sys.argv :
        try:
            error = 12
            if '-p' not in sys.argv:
                error = 11
                exit(error)
            arg = int(sys.argv[sys.argv.index('-pa') + 1])
            
            if arg < 0:
                error = 7
                exit(error)  
            args_dict['-pa'] = arg
        except:
            generateHelpText(error)
            exit(error) 

    if '-pb' in sys.argv :
        try:
            error = 12
            if '-p' not in sys.argv:
                error = 11
                exit(error)
            arg = int(sys.argv[sys.argv.index('-pb') + 1])
            
            if arg < 0:
                error = 7
                exit(error)  
            args_dict['-pb'] = arg
        except:
            generateHelpText(error)
            exit(error) 
       

    for el in sys.argv:
        if "-" == el[0] and not (el == '-a' or el == '-s' or el == '-f'or el == '-p' or el == '-pa' or el == '-pb' or el == '-h' or el == '-csv'):
            error = 8
            generateHelpText(error)
            exit(error) 
    if len(sys.argv) == 1:
        error = 6
        generateHelpText(error)
        exit(error)

    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        error = 0
        generateHelpText(error)
        exit(error)

    if len(sys.argv) > 2 and '-h' in sys.argv:
        error = 3
        generateHelpText(error)
        exit(error)

    if len(sys.argv) > 9:
        error = 4
        generateHelpText(error)
        exit(error)

    if '-a' in sys.argv:
        args_dict['-a'] = True

    if '-s' in sys.argv and '-f' in sys.argv:
        error = 5
        generateHelpText(error)
        exit(error)

    if '-s' in sys.argv and not '-f' in sys.argv:
        args_dict['-s'] = True

    if '-csv' in sys.argv:
        args_dict['-csv'] = True
  
    if '-f' in sys.argv:
        args_dict['-f'] = True
        if not os.path.exists(sys.argv[-1]) or not sys.argv[-1].endswith('.txt'):
            error = 1
            generateHelpText(error)
            exit(error)
    else:
        if (sys.argv[-1].endswith('.txt') and  not '-s' in sys.argv):
            pass
        elif sys.argv[-1].endswith('.txt') or not os.path.exists(sys.argv[-1]):
            error = 2
            generateHelpText(error)
            exit(error)

    args_dict['Path'] = sys.argv[-1]
    return args_dict

def correct_pars_and_args(parameters):
    if not parameters['Path']:
        return parameters['Path']
    if not parameters['-p'] and (parameters['-pa'] or parameters['-pb']):
            return False
    if parameters['-s'] and parameters['Path']:
        if parameters['Path'].endswith('.txt') or parameters['-f']:
            return False
    if parameters['-f'] and parameters['Path']:
        if not parameters['Path'].endswith('.txt') or parameters['-s']:
            return False
    return True

def main1(parameters):
    word_counter = WordCounter(parameters)
    word_counter.generate_report() 

def main2():
    word_counter =[]
    parameters = {}
    parameters['-a'] = False
    parameters['-s'] = False
    parameters['-f'] = False
    parameters["-p"] = False
    parameters["-pa"] = False
    parameters["-pb"] = False
    parameters['Path'] = False
    parameters['-csv'] = False
    i = 0
    ch = 1
    while ch != 0: 
        try:
                           print('\n 1 - Directory or *.txt file',
                                 '\n 2 - Reading files from subfolder',
                                 '\n 3 - Reading files from *.txt file ',
                                 '\n 4 - Write phrase',
                                 '\n 5 - List parameters'
                                 '\n 6 - Help',
                                 '\n 7 - Generate report ',
                                 '\n 0 - Exit ')
                           ch = int(input('\n\nEnter parameter: '))
        except:
                generateHelpText(8)
                ch = -1
        if ch == 1:
            folder = 1
           
            while folder != 0:
                try:
                    print('\n 1 - Enter Directory',
                          '\n 2 - *.txt file',
                          '\n 0 - Exit')
                    folder = int(input('\n\nEnter parameter : '))
                    print()
                    if folder == 1:
                        directory = str(input('Enter directory: '))
                        parameters['Path'] = directory
                        if directory.endswith('.txt') or not os.path.exists(directory) :
                            error = 2
                            generateHelpText(error)
                            folder =-1
                            parameters['Path'] = False
                        
                    elif folder == 2:
                        parameters['Path'] = str(input('Enter *.txt file: '))
                        if not parameters['Path'].endswith('.txt'):
                            parameters['Path'] = False
                            generateHelpText(9)
                    elif folder == 0:
                        pass
                    else:
                        error = 8
                        generateHelpText(error)
                        
                except:
                    error = 8
                    generateHelpText(error)
                    folder =-1

        elif ch == 2:  
            subfolder = 1
            while subfolder != 0:
                try:
                    print("\n 1 - Yes ",
                          "\n 2 - No ",
                          "\n 0 - Exit")
                    print("\n\n Reading files from subfolder ")
                    subfolder = int(input("Enter parameter :  "))
                    if subfolder == 1:
                        if parameters["-f"]:
                            generateHelpText(5)
                            parameters['-s'] = False
                        else:
                            parameters['-s'] = True
                    elif subfolder == 2:
                        parameters['-s'] = False
                    elif subfolder == 0:
                        pass
                    else:
                        generateHelpText(8)
                except:
                    generateHelpText(8)
                    subfolder =-1
       
        elif ch == 3:
            file =1
            while file !=0:
                try:
                    print("\n 1 - Yes ",
                          "\n 2 - No ",
                          "\n 0 - Exit")
                    print("\n\n Reading files from *.txt file ")
                    file = int(input("Enter parameter :  "))

                   
                    if file == 1:
                        if parameters["-s"]:
                            generateHelpText(5)
                            parameters['-f'] = False
                        else:
                            parameters['-f'] = True
                    elif  file == 2:
                        parameters['-f'] = False
                    elif file == 0:
                        pass
                    else:
                        generateHelpText(8)
                except:
                    generateHelpText(8)
                    file =-1
        
        elif ch == 4: 
            pa=-1
            pb=-1
            phrase = -1
            
            while phrase != 0:
                if parameters['-p']:
                    try:
                        
                        print("\n 1 - Write phrase ",
                            "\n 2 - Write number words before phrase ",
                            "\n 3 - Write number words after phrase ",
                            "\n 0 - Exit")
                        phrase = int(input("\n\nEnter parameter: "))
                    
                    except:
                        phrase = -1
                    if phrase == 1:
                        parameters['-p'] = str(input('Enter phrase: '))
                    elif phrase == 2: 
                        try:
                            pb = int(input('Enter number words before phrase: '))
                            if pb > 0 :
                                parameters['-pb'] = pb
                            else:
                                generateHelpText(7)
                        except:
                            generateHelpText(8)
                            pb=-1
                    elif phrase == 3: 
                        try:
                            pa = int(input('Enter number words after phrase: '))
                            if pa > 0 :
                                parameters['-pa'] = pa
                            else:
                                generateHelpText(7)
                        except:
                            generateHelpText(8)
                            pa=-1
                    elif phrase == 0:
                        pass
                    else:
                        generateHelpText(8)
                else:
                    try:
                        parameters['-pb'] = False
                        parameters['-pa'] = False 
                        print("\n 1 - Write phrase ",
                            "\n 0 - Exit")
                        phrase = int(input("\n\nEnter parameter: "))
                    
                    except:
                        phrase = -1
                    if phrase == 1:
                        parameters['-p'] = str(input('Enter phrase: '))
                    elif phrase == 0:
                        pass
                    else:
                        generateHelpText(8)
        elif ch == 5:
            print(parameters)

        elif ch == 6:
            generateHelpText(0)

        elif ch == 7:
            if correct_pars_and_args(parameters):
                csv_report = int(input("\nEnter 1 if you want to generate .txt report \n0 - .csv report\n:"))
                parameters['-csv'] = csv_report == 0
                word_counter.insert(i, WordCounter(parameters))
                word_counter[i].generate_report(i+1)
                i+=1
                parameters = {}
                parameters['-a'] = False
                parameters['-s'] = False
                parameters['-f'] = False
                parameters["-p"] = False
                parameters["-pa"] = False
                parameters["-pb"] = False
                parameters['Path'] = False
                parameters['-csv'] = False
            else:
                generateHelpText(10)

        elif ch == 0:
            pass
        else :
            generateHelpText(8)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        main2()
    else:
        parameters = processArgv()
        main1(parameters)
        
