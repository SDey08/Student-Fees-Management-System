import mysql.connector as mysql

mydb = mysql.connect(host = "localhost", user = "rootsd", password = "1234", database = "stfeeman")
mycursor = mydb.cursor(buffered=True)
mth = ('JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER')

def main():
    while 1:
        print("\n\n-------------------------------------")
        print("|           :  WELCOME  :           |")
        print("-------------------------------------")
        print("\n             1. LOGIN\n             2. SIGNUP\n             3. EXIT")
        choice = input("\nOption: ")

        if choice == "1":
            login()
        elif choice == "2":
            signup()
        elif choice == "3":
            exit(0)
        else:
            print("\nInvalid option!")

def login():
    print("\n\n-------------------------------------")
    print("|           :  LOGIN  :             |")
    print("-------------------------------------")
    email = input("\nEmail id: ")
    password = input("Password: ")
    mycursor.execute("SELECT * FROM students")
    data = mycursor.fetchall()

    if len(data) == 0:
       print("\nAccount not found!")
       main()
    else: 
        for row in data:
            if row[4] == email:
                if row[6] == password:
                    print("\nLogged in successfully!")
                    name, adno = row[1], row[5]
                    student(name, adno)
                else:
                    print("\nInvalid email or password!")
                    login()
            else:
                if row[0] == len(data):
                    print("\nAccount not found!")
                    main()

def signup():
    print("\n\n-------------------------------------")
    print("|           :  SIGNUP  :            |")
    print("-------------------------------------")
    name = input("\nFullname: ")
    dob = input("D.O.B.(DD/MM/YYYY): ")
    contacts = input("Phone no.: ")
    email = input("Email id: ")
    adno = input("Admission no.: ")
    password = input("Create a strong password: ")
    
    get_val = (name, dob, contacts, email, adno, password)
    mycursor.execute("INSERT INTO students (name, dob, ph, email_id, adm_no, password) VALUES (%s, %s, %s, %s, %s, %s)", get_val)
    mydb.commit()
    print("\nAccount created successfully!")
    main()

def student(name, adno):
    print("\n\n-------------------------------------")
    print("|       :  PAYMENT STATUS  :        |")
    print("-------------------------------------")
    month = (input("\n\nEnter the month for which you want to pay the fees: ")).upper()
    while month not in mth:
        print("\n\nError! Month not found.")
        month = (input("\nEnter the month for which you want to pay the fees: ")).upper()
    pay_check(name, adno, month)

def pay_check(name, adno, month):

    mycursor.execute("SELECT * FROM payments WHERE adm_no = %s AND month = %s", (adno, month))
    data = mycursor.fetchall()

    if len(data) == 0:
        print("\n\nPayment status: Not available")
        while 1:
            print("\n\nDo you want to:\n1. Proceed to payment\n2. Logout")
            ch = input("\nOption: ")
            if ch == "1":
                print("\n\nPROCEEDING. . .")
                print("\n\n-------------------------------------")
                print("|           :  PAYMENT  :            |")
                print("-------------------------------------")              
                amt = input("\n\nEnter the amount to be paid: Rs. ")
                #Payment procedure
                print("\nPayment procedure. . .\n\n\nPayment successful!")
                print("\n\n--------------RECEIPT---------------")  
                print(f"\n\n      * * * {month} FEES * * *")
                print("\n        Name:", name)
                print("        Admission no.:", adno)
                print("        Amount paid: Rs.", amt)
                get_val = (name, adno, amt, month)
                mycursor.execute("INSERT INTO payments (name, adm_no, amt, pay_stat, month) VALUES (%s, %s, %s, 'Paid', %s)", get_val)
                mydb.commit()               
                main()
            elif ch == "2":
                main()
            else:
                print("Invalid option!") 
    else:
        print("\n\nPayment status: Available")
        print(f"\n\n      * * * {month} FEES * * *")
        print("\n        Name:", name)
        print("        Admission no.:", adno)
        print("        Amount paid: Rs.", data[0][3])
        main()

main()