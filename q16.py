import csv


def read_and_print_csv(file_path):
    with open(file_path, mode='r') as file:

        csv_reader = csv.reader(file)
        

        for row in csv_reader:

            print(row)


file_path = 'C://Users//Ajay//Documents//Automobile.csv'  

read_and_print_csv(file_path)
