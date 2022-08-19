import csv
  #This is  modified way to change modify the data from the csv to the required cells which is writen to a new file
with open("names.csv", mode="r") as original:
    reader_obj = csv.reader(original)
      
    with open("output.csv", mode="w") as new:
        writer_obj = csv.writer(new)
        for column in reader_obj:
            writer_obj.writerow((column[0], column[2])) # changing the number in the coloumn to 0-2 allows the user to see specific data