import csv
def print_db():
    with open("db.csv", newline='') as data:
        #data_base = data.read()
    #print(data_base)
        reader = csv.reader(data)
        for row in reader:
            print(row)


def add_user(fname, lname, phone, about):
    with open('db.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(lname, fname, phone, about)