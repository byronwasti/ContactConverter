import csv

data = csv.reader(open('Contacts.CSV'),delimiter=',')
data.next()

emails = []
names = []

for row in data:
    emails.append(row[1])
    names.append(row[0])

email_1 = []
for i in range(len(emails)):
    tmp = emails[i].split('(')
    tmp2 = tmp[-1]
    tmp3 = tmp2.split(')')
    tmp4 = tmp3[0]

    email_1.append(tmp4)

print(names[1])


with open('Output.csv','w') as csvfile:
    writer = csv.writer(csvfile,delimiter=',')    
    writer.writerow(['Name','Email'])
    for i in range(len(email_1)):    
        writer.writerow([names[i], email_1[i]])

    #writer.writecolumn(email_1)
