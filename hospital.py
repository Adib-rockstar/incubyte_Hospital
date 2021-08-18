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
        time.sleep(.25)
        os.system('CLS')
    else:
        print("You have entered wrong details");
        time.sleep(.25)
        os.system('CLS')
home_page();
