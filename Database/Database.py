import csv
import os.path
import pandas as pd

class DB:
    csv_num_record = 0
    record_size = 0
    overflow_record = 0
    #default constructor
    def init(self):
        self.filestream = None
        self.config = None
        self.num_record = 0
        self.record_size = 0
        self.text_filename = None
    #create database
    def createDB(self,filename):
        #Generate file names
        data_num_record = 0
        csv_filename = filename + ".csv"
        text_filename = filename + ".data"
        config_filename = filename + ".config"
        # Read the CSV file and write into data files
        with open(csv_filename, "r") as csv_file:
            linenums = pd.read_csv(csv_filename)
            #print("Number of lines present:-", len(linenums))
            csv_num_record = len(linenums)
            data_list = list(csv.DictReader(csv_file,fieldnames=('name','rank','city','state','zip','employees')))

        # Formatting files with spaces so each field is fixed length, i.e. ID field has a fixed length of 10
        def writeRecord(filestream, dict):
            filestream.write("{:50.50}".format(dict["name"]))
            filestream.write("{:5.5}".format(dict["rank"]))
            filestream.write("{:30.30}".format(dict["city"]))
            filestream.write("{:20.20}".format(dict["state"]))
            filestream.write("{:30.30}".format(dict["zip"]))
            filestream.write("{:40.40}".format(dict["employees"]))
            filestream.write("\n")

        with open(text_filename,"w") as outfile:

            while True:
              print("\n------------- User Menu ----------------")
              print("Press 0 quit                             | ")
              print("Press 1 to record search                 |")
              print("Press 2 to add all records")
              menuChoice = int(input("Enter Choice: "))
              print("----------------------------------------")

              if menuChoice == 0:
                  self.record_size = data_num_record
                  break
              if menuChoice == 1:
                  num = int(input("Enter a line number: "))
                  count = 0
                  if num > csv_num_record:
                    print(f"Invalid Range: Number must be within 0-{csv_num_record}")
                  else:
                    for dict in data_list:
                        if count == num:
                            print(dict)
                            data_num_record = data_num_record + 1
                            print(data_num_record)
                            writeRecord(outfile,dict)
                        count = count + 1
              if menuChoice == 2:
                    count = 0
                    for i in range(500):
                        dict = data_list[i]
                        data_num_record = data_num_record + 1
                        writeRecord(outfile, dict)
                        count += 1
                    print("Successfully entered", count,"database")
              elif (menuChoice < 0) & (menuChoice > 3):
                print("\n------------- User Menu ----------------")
                print("Press 0 quit                             | ")
                print("Press 1 to record search                 |")
                print("Press 2 to add all records")
                menuChoice = int(input("Enter Choice: "))
                print("----------------------------------------")
                print("Invalid choice, please try again")
        
        with open(config_filename,"w") as outfile:
            outfile.write(f"The number of records is {data_num_record}\n")
            outfile.write(f"The number of overflow record is {self.overflow_record} ")

    def open(self, name):
        filename = name + ".data"
        configName = name + ".config"
        try:
            self.filestream = open(filename, 'r+')
            self.config = open(configName, 'r')
            #print("Success")
        except FileNotFoundError:
            print(f"Data file not found for database '{name}'. Please call the database function to create it.")
            return False

        return True
    #read the database
    def readDB(self, filename, DBsize, rec_size):
        self.filestream = filename + ".data"
        # self.record_size = DBsize
        self.rec_size = rec_size
        if not os.path.isfile(self.filestream):
            print(str(self.filestream)+" not found")
        else:
            self.text_filename = open(self.filestream, 'r+')

    #read record method
    def readRecord(self, recordNum):
        self.flag = False
        name = rank = city = state = zip = employees = "None"

        if recordNum >=0 and recordNum < self.record_size:
            #print("test")
            self.text_filename.seek(0,0)
            self.text_filename.seek(recordNum*self.rec_size)
            line= self.text_filename.readline().rstrip('\n')
            #print(line)
            self.flag = True
        else:
            print("booo")
            print("Out of bounds!")
        if self.flag:
            #print("hi")
            name = line[0:50]
            rank = line[50:55]
            city = line[55:85]
            state = line[85:105]
            zip = line[105:135]
            employees = line[135:175]

        self.record = dict({"name":name,"rank":rank,"city":city,"state":state,"zip":zip, "employees": employees})

    #Binary Search by record id
    def binarySearch (self, input_ID):
        
        low = 0
        high = self.record_size - 1
        self.found = False

        while high >= low:

            self.middle = (low+high)//2
            self.getRecord(self.middle)
            # print(self.record)
            mid_id = self.record["ID"]
            
            if int(mid_id) == int(input_ID):
                self.found = True
                break
            elif int(mid_id) > int(input_ID):
                high = self.middle - 1
            elif int(mid_id) < int(input_ID):
                low = self.middle + 1


    #close the database
    def close(self):
        if self.filestream:
            self.filestream.close()
            self.config.close()
            self.filestream = None
            self.config = None
        
        

