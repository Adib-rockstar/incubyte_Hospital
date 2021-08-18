import time
import os
def home_page():
    flag=0;
    print("\t\t========================================");
    print("\t\t| Welcome to Hospital Database          |");
    print("\t\t| Please Enter Login Details            |\n");
    username=input("\t\t| USERNAME : ");
    password=input("\t\t| PASSWORD : ");
    admin=open("login.txt",'r');
    admindata=admin.readline();
    dollarindex=admindata.index("$");
    user=admindata[:dollarindex];
    passw=admindata[dollarindex + 1:];
    if (user == username and passw == password):
        print("\n\t\tLOGGED IN SUCCESSFULLY..!         |\n");
        print("\t\t========================================");
        flag=1;
        time.sleep(.50);
        os.system('CLS');
        hospital_data_menu();
    else:
        print("\t\tYou have entered wrong details");
        time.sleep(1);
        os.system('CLS');
        home_page();

def hospital_data_menu():
    print("\t\t===============================================");
    print("\t\t|What you like to do please select an option |\n");
    print("\t\t|1.To insert customer data                   |\n");
    print("\t\t|2.To view customer data                     |\n");
    opt=int(input("\t\t|Enter your choice :- "));
    if (opt == 1):
        time.sleep(1);
        insert_data();
    elif (opt ==2):
        time.sleep(1);
        view_data();
    else:
        print("Invalid option please try again");
        time.sleep(1);
        hospital_data_menu()


home_page();
