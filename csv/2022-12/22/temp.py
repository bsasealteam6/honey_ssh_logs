import csv
passwords = open("passwords.txt",'w')
usernames = open("usernames.txt",'w')
with open('p22-2022-12-28_06-00.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)

    for row in spamreader:
        if len(row) < 7:
            print(row)
        else:
            usernames.write(f'{row[5]}\n')
            passwords.write(f'{row[6]}\n')
