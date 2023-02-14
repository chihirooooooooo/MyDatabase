from Database import DB
import csv
#filepath = "Fortune500"
DBsize = 10
rec_size = 176
using = False
current_database = None
filepath = None
deleted_list = []
# rec_size = 72 if a Windows file with cr lf at ends of the lines

while True:
  print("\n------------- User Menu ----------------")
  print("Press 1 create new database              |")
  print("Press 2 open database                    |")
  print("Press 3 close database                   |")
  print("Press 4 display record                   |")
  print("Press 5 update record                    |")
  print("Press 6 create report                    |")
  print("Press 7 add record                       |")
  print("Press 8 delete record                    |")
  print("Press 9 quit                             |")
  choice = input("Enter Choice: ")
  if choice == '1':
    filepath = input("which csv file do you want to use to create database? ")
    sample = DB()
    sample.createDB(filepath)
    #sample.CloseDB()
  elif choice == '2':
    if not using:
      filepath = input("which data file do you want to access? ")
      if DB.open(DB,filepath):
        current_database = sample
        print("Success")
      using = True
    else:
      print("Another database is already open")

  elif choice == '3':
    DB.close(DB)
    current_database = None
    using = False
    print("No database is open")
  elif choice == '4':
    if using:
      company = input("Which company info do you need? ")
      #print(company)
      found = False
      print(current_database.record_size)
      for line in range(current_database.record_size):
        #print(line)
        if line in deleted_list:
          continue
        sample.readDB(filepath, DBsize, rec_size)
        sample.readRecord(line)
    
        if sample.record["name"].strip() == company:
          found = True
          
      
      if found:
        print(f"Record {line}, : "+sample.record["name"]+"\t rank: "+sample.record["rank"]+"\t city: "+sample.record["city"]+"\t state: "+str(sample.record["state"])+"\t zip: "+sample.record["zip"]+"\t employees: "+sample.record["employees"])
      else:
        print("The company doesn't exist in the data file")

      # line = int(input("which line do you want to read? "))
      # sample.readDB(filepath, DBsize, rec_size)
      # sample.readRecord(line)
      
    else:
      print("No database is open")

  elif choice == '5' :
    if using:
      company = input("Which company info do you need? ")
      #print(company)
      found = False
      #print(current_database.record_size)
      for line in range(current_database.record_size):
        #print(line)
        sample.readDB(filepath, DBsize, rec_size)
        sample.readRecord(line)
        #print(sample.record["name"])
        if sample.record["name"].strip() == company:
          found = True
          break
      
      if found:
        field = input("Which field do you want to update? rank, city, state, zip, or employees: ")
        if field == "rank" or field == "city" or field == "state" or field == "zip" or field == "employees":
          newVal = input("Enter new value: ")
          
          with open('Fortune500.data', 'r') as file :
            filedata = file.read()

            # Replace the target string
            if field == "rank":
              filedata = filedata.replace(sample.record[field], "{:5.5}".format(newVal))
            if field == "city":
              filedata = filedata.replace(sample.record[field], "{:30.30}".format(newVal))
            if field == "state":
              filedata = filedata.replace(sample.record[field], "{:20.20}".format(newVal))
            if field == "zip":
              filedata = filedata.replace(sample.record[field], "{:30.30}".format(newVal))
            if field == "employees":
              filedata = filedata.replace(sample.record[field], "{:40.40}".format(newVal))




            # Write the file out again
            with open('Fortune500.data', 'w') as file:
              file.write(filedata)

          print("This is the new data")
          sample.record[field] = newVal
          print(f"Record {line}, : "+sample.record["name"]+"\t rank: "+sample.record["rank"]+"\t city: "+sample.record["city"]+"\t state: "+str(sample.record["state"])+"\t zip: "+sample.record["zip"]+"\t employees: "+sample.record["employees"])

      else:
        print("The company doesn't exist in the data file")

      # line = int(input("which line do you want to read? "))
      # sample.readDB(filepath, DBsize, rec_size)
      # sample.readRecord(line)
      
    else:
      print("No database is open")

  elif choice == "6"  :
    if using:
      print("This is the first ten records")
      for line in range(10):
          
          sample.readDB(filepath, DBsize, rec_size)
          sample.readRecord(line)
          print(f"Record {line}, : "+sample.record["name"]+"\t rank: "+sample.record["rank"]+"\t city: "+sample.record["city"]+"\t state: "+str(sample.record["state"])+"\t zip: "+sample.record["zip"]+"\t employees: "+sample.record["employees"])
    
    else:
      print("No database is open")

  elif choice == '8':
    if using:
      company = input("Which company do you want to delete? ")
      for line in range(current_database.record_size):
          #print(line)
          sample.readDB(filepath, DBsize, rec_size)
          sample.readRecord(line)
          #print(sample.record["name"])
          if sample.record["name"].strip() == company:
            found = True
            deleted_list.append(line)
            break
      
      if found:
        with open('Fortune500.data', 'r') as file :
              filedata = file.read()

              filedata = filedata.replace(sample.record["name"], "{:50.50}".format("")) 
              filedata = filedata.replace(sample.record["rank"], "{:5.5}".format(""))
            
              filedata = filedata.replace(sample.record["city"], "{:30.30}".format(""))
    
              filedata = filedata.replace(sample.record["state"], "{:20.20}".format(""))
    
              filedata = filedata.replace(sample.record["zip"], "{:30.30}".format(""))
        
              filedata = filedata.replace(sample.record["employees"], "{:40.40}".format(""))




              # Write the file out again
              with open('Fortune500.data', 'w') as file:
                file.write(filedata)
                print("Success")
              
              

    else:
      print("No database is open")

  elif choice == '7':
    if using:
      with open("Fortune500.csv", "r") as csv_file:
        with open("Fortune500.data","a") as outfile:

        ### INPUTS
          name1 = input("Enter company name: ")
          rank1 = input("Enter a rank number: ")
          city1 = input("Enter city: ")
          state1 = input("Enter state: ")
          zip1 = input("Enter zip number: ")
          employees1 = input("Enter employees: ")

          data_list = list(csv.DictReader(csv_file,fieldnames=('name','rank','city','state','zip','employees')))
          count = 0
          
          for dict in data_list:
              dict["name"] = name1
              dict["rank"] = rank1
              dict["city"] = city1
              dict["state"] = state1
              dict["zip"] = zip1
              dict["employees"] = employees1

              outfile.write("{:50.50}".format(dict["name"]))
              outfile.write("{:5.5}".format(dict["rank"]))
              outfile.write("{:30.30}".format(dict["city"]))
              outfile.write("{:20.20}".format(dict["state"]))
              outfile.write("{:30.30}".format(dict["zip"]))
              outfile.write("{:40.40}".format(dict["employees"]))
              outfile.write("\n")
              
              current_database.record_size = current_database.record_size + 1
              current_database.overflow_record = current_database.overflow_record + 1
              print(dict["name"] + " Added successfully")

              break 
            
          with open('Fortune500.config', 'w') as file:
            file.write(f"The number of records is {current_database.record_size}\n")
            file.write(f"The number of overflow records is {current_database.overflow_record}")
              
    else:
      print("No database is open")


  elif choice == '9':
    print("Bye!")
    break

  else:
    print("Invalid value!")

