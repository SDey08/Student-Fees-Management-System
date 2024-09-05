def main():
    while 1:
        print("\n\n***********WELCOME************\n\n")
        print("1. LOGIN\n2. SIGNUP")
        choice = input("\nOption: ")

        if choice == "1":
            login()
        elif choice == "2":
            signup()
        else:
            print("\nInvalid option!")

def login():
    print("\n\n       LOGIN")
    email = input("\nEmail id: ")
    password = input("\nPassword: ")
    if email == " ":
        if password == " ":
            print("\nLogged in successfully!")
            student()
        else:
            print("\nInvalid email or password!")
            login()
    else:
        print("\nAccount not found!")
        main()
        
def signup():
    print("\n\n       SIGNUP")
    name = input("\nname: ")
    dob = input("\nD.O.B.(DD/MM/YYYY): ")
    contacts = input("\nPhone no.: ")
    email = input("\nEmail id: ")
    adno = input("\nAdmission no.: ")
    password = input("Create a strong password: ")
    pay_stat = "Not paid"
    print("\n\nAccount created successfully!")
    main()

def student():
    print("\n\n       PAYMENT")
    amt = input("\nAmount payable: Rs. ")

    if pay_stat == "Not paid":
        print("\nPayment status:", pay_stat)
        print("Do you want to:\n1. Proceed to payment\n2.Logout")
        ch = input("Option: ")
        if ch == "1":
            print("\nPROCEEDING. . .")
            feename = input("Title: ")
            #Payment procedure
            print("\nPayment procedure. . .\n\nPayment successful!")
            print("\n\n        RECEIPT")
            print(f"* * * {feename} * * *")
            print("Name:", name)
            print("Admission no.:", adno)
            print("Amount paid:", amt)
            pay_stat = "Paid"
        elif ch == "2":
            main()
        else:
            print("Invalid option!")
    else:
        print(f"* * * {feename} * * *")
        print("Name:", name)
        print("Admission no.:", adno)
        print("Amount paid: Rs.", amt)
        print("\nPayment status:", pay_stat)
        main()

main()