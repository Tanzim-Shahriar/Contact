import csv
data=[
    ["Name","Email","Phone Number","Address"]
]


def addname(name):
    if name.isalpha():
        lists.append(name)
    else:
        print("Name should contain only string value")
        name=input("Enter name again")
        addname(name)


def addPhone(phone):
    for i in range(len(data)):
        if phone in data[i]:
            print("This number is already exists.")
            phone = input("Enter number again")
            addPhone(phone)

    return phone

def addEmail(email):
    lists.append(email)
def addAddress(address):
    lists.append(address)
def dltContact(dlt):
    for i in range(len(data)):
        if dlt in data[i]:
            del data[i]
            break
def disPlay(dsp):

    for i in range(len(data)):
        if dsp in data[i]:
            print("Name: ",data[i][0])
            print("Email: ",data[i][1])
            print("Phone number: ",data[i][2])
            print("Address: ",data[i][3])


while True:

    print("0. Exit")
    print("1. Add contacts")
    print("2. Delete contacts")
    print("3. Search contact details")


    menu=input("Enter option: ")
    if menu=="0":
        break
    elif menu=="1":
        lists = []
        name=input("Enter your name: ")
        addname(name)
        email=input("Enter email: ")
        addEmail(email)
        phone=int(input("Enter phone number: "))
        phn=addPhone(phone)
        lists.append(phn)
        address=input("Enter address: ")
        addAddress(address)

        data.append(lists)

        with open("Contactlist.csv", mode="w", newline='') as csvFile:
            csvFileWriter = csv.writer(csvFile)
            csvFileWriter.writerows(data)
    elif menu=="2":
        dlt=input("Enter the contact number you want to delete: ")
        dltContact(dlt)
    elif menu=="3":
        dsp=input("Enter the contact number you want to search: ")
        disPlay(dsp)
    else:
        print("Invalid option")

