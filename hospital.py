import time
import os
import pyodbc
def home_page():
    os.system('CLS');
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
        insert_data_menu();
    elif (opt ==2):
        time.sleep(1);
        view_data_menu();
    else:
        print("Invalid option please try again");
        time.sleep(1);
        hospital_data_menu();

def view_data_menu():
    print("\t\t===============================================");
    print("\t\t|How you like to view data please select.    |\n");
    print("\t\t|1.To view by customer ID.                   |\n");
    print("\t\t|2.To view by country                        |\n");
    opt=int(input("\t\t|Enter your choice :- "));
    if (opt == 1):
        time.sleep(1);
        view_customerID();
    elif (opt ==2):
        time.sleep(1);
        view_country();
    else:
        print("Invalid option please try again");
        time.sleep(1);
        view_data_menu();

def view_customerID():
    i=1;
    data="x";
    driver = '{Microsoft Access Driver (*.mdb, *.accdb)}' #which database we are using
    filepath = r'C:\Users\Adib\Desktop\New folder\incubyte_Hospital\hospital1.accdb'    #location of the database
    conn=pyodbc.connect(driver= driver, dbq=filepath, autocommit=True ) #eastablished the connection
    cursor=conn.cursor()
    print("\t\t===============================================");
    custID=input("\t\t|Please enter customer ID :- ");
    table_name = "Master_hospital"
    query = "SELECT * FROM {}".format(table_name)
    cursor.execute(query)
    while (i=1):
        if (i==1):
            onerow=cursor.fetchone();
            data=onerow.Customer_ID;
            if (data==custID):
                print (data);
                i=2;
            else:
                print("Record not found");


def view_country():
    print("\t\t===============================================");
    custID=input("\t\t|Please enter Country name :- ");


home_page();
