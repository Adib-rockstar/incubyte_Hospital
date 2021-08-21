import time     #mainly used to create a effect of loading..
import os       #used to clear the command prompt
import pyodbc   #to establish connection between database and python
import site     #use to exit the porgram
def home_page():
    os.system('CLS')
    flag=0
    print("\t\t========================================")
    print("\t\t| Welcome to Hospital Database          |")
    print("\t\t| Please Enter Login Details            |\n")
    username=input("\t\t| USERNAME : ")
    password=input("\t\t| PASSWORD : ")
    admin=open("login.txt",'r')
    admindata=admin.readline()
    dollarindex=admindata.index("$")
    user=admindata[:dollarindex]
    passw=admindata[dollarindex + 1:]
    if (user == username and passw == password):
        print("\n\t\tLOGGED IN SUCCESSFULLY..!         |\n")
        print("\t\t========================================")
        flag=1
        time.sleep(.50)
        os.system('CLS')
        hospital_data_menu()
    else:
        print("\t\tYou have entered wrong details")
        time.sleep(1)
        os.system('CLS')
        home_page()

def hospital_data_menu():
    print("\t\t===============================================")
    print("\t\t|What you like to do please select an option |\n")
    print("\t\t|1.To insert customer data                   |\n")
    print("\t\t|2.To view customer data                     |\n")
    print("\t\t|3.To edit customer data                     |\n")
    opt=int(input("\t\t|Enter your choice :- "))
    if (opt == 1):
        time.sleep(1)
        insert_data_menu()
    elif (opt ==2):
        time.sleep(1)
        view_data_menu()
    else:
        print("Invalid option please try again")
        time.sleep(1)
        hospital_data_menu()

def insert_data_menu():
    i=1
    id=[]
    newid=["C"]
    custid=" "
    driver = '{Microsoft Access Driver (*.mdb, *.accdb)}' #which database we are using
    filepath = r'C:\Users\Adib\Desktop\New folder\incubyte_Hospital\hospital1.accdb'    #location of the database
    conn=pyodbc.connect(driver= driver, dbq=filepath, autocommit=True ) #eastablished the connection
    cursor=conn.cursor()
    table_name = "master_hospital"
    query = "SELECT * FROM {}".format(table_name)
    cursor.execute(query)
    while (i==1):
        if (i==1):
            try:
                onerow=cursor.fetchone()
                id=onerow.Customer_ID
            except:
                i=2
    id=id[1:]
    id=int(id)
    id=id+1
    newid.append(id)
    custid = ''.join(map(str, newid))
    print (custid)
    try:
        print("\t\t===============================================")
        print("\t\t|Enter the details of the customer            |")
        cust_name=input("\t\t|Customer Name : ")
        open_date=input("\t\t|Customer Open Date (YYYY-MM-DD) : ")
        last_date=input("\t\t|Customer Last Last_Consulted_Date (YYYY-MM-DD) : ")
        vacci=input("\t\t|Customer Vaccination Type : ")
        doctor=input("\t\t|Doctor Consulted : ")
        state=input("\t\t|Customer State : ")
        contri=input("\t\t|Customer Country : ")
        country=contri.lower()
        post=input("\t\t|Customer Postcode : ")
        dob=input("\t\t|Customer Date of Birth (YYYY-MM-DD) : ")
        active=input("\t\t|Active (A/N) : ")
        val=(cust_name,custid,open_date,last_date,vacci,doctor,state,country,post,dob,active)
        cursor.execute("INSERT INTO {} VALUES (?,?,?,?,?,?,?,?,?,?,?)".format(country),val)
        print("\n\t\t|DATA INSERTED")
        table_name = "master_hospital"
        vals=(custid,country)
        cursor.execute("INSERT INTO {} VALUES (?,?)".format(table_name),vals)
        cursor.commit()
        print("\t\t===============================================")
        print("\n\t\t|Do you like to do more activity if yes then press 1 ")
        yes=int(input("\t\t|Please Enter : "))
        if(yes == 1):
            os.system('CLS')
            hospital_data_menu()
        else:
            exit()
    except:
        print("You have entered some wrong values")
        hospital_data_menu()

def view_data_menu():
    print("\t\t===============================================")
    print("\t\t|How you like to view data please select.    |\n")
    print("\t\t|1.To view by customer ID.                   |\n")
    print("\t\t|2.To view by country                        |\n")
    opt=int(input("\t\t|Enter your choice :- "))
    if (opt == 1):
        time.sleep(1)
        view_customerID()
    elif (opt ==2):
        time.sleep(1)
        view_country()
    else:
        print("Invalid option please try again")
        time.sleep(1)
        view_data_menu()

def view_customerID():
    i=1
    j=1
    opt=1
    custidcheck="x"
    driver = '{Microsoft Access Driver (*.mdb, *.accdb)}' #which database we are using
    filepath = r'C:\Users\Adib\Desktop\New folder\incubyte_Hospital\hospital1.accdb'    #location of the database
    conn=pyodbc.connect(driver= driver, dbq=filepath, autocommit=True ) #eastablished the connection
    cursor=conn.cursor()
    print("\t\t===============================================")
    custID=input("\t\t|Please enter customer ID :- ")
    custID=custID.upper()
    table_name = "master_hospital"
    query = "SELECT * FROM {}".format(table_name)
    cursor.execute(query)
    while (i==1):
        if (i==1):
            try:
                onerow=cursor.fetchone()
                custidcheck=onerow.Customer_ID
            except:
                print("Record not found")
                i==2
            if (custidcheck==custID):
                countrycheck=onerow.Country
                query2="Select * from {}".format(countrycheck)
                cursor.execute(query2)
                while (j==1):
                    inneronerow=cursor.fetchone()
                    custidcheck=inneronerow.Customer_ID
                    if (custidcheck==custID):
                        print("\t\t========================================")
                        print("\t\t|Details of the customer               |")
                        print("\t\t|Customer Name : ",inneronerow.Customer_Name)
                        print("\t\t|Customer ID : ",inneronerow.Customer_ID)
                        print("\t\t|Customer Open Date : ",inneronerow.Customer_Open_Date)
                        print("\t\t|Customer Last Last_Consulted_Date : ",inneronerow.Last_Consulted_Date)
                        print("\t\t|Customer Vaccination Type : ",inneronerow.Vaccination_Type)
                        print("\t\t|Doctor Consulted : ",inneronerow.Doctor_Consulted)
                        print("\t\t|Customer State : ",inneronerow.State)
                        print("\t\t|Customer Country : ",inneronerow.Country)
                        print("\t\t|Customer Postcode : ",inneronerow.Postcode)
                        print("\t\t|Customer Date of Birth : ",inneronerow.DOB)
                        print("\t\t|Active : ",inneronerow.Active_Customer)
                        opt=2
                        print("\n\t\t|Do you like to do more activity if yes then press 1 ")
                        yes=int(input("\t\t|Please Enter : "))
                        if(yes == 1):
                            os.system('CLS')
                            hospital_data_menu()
                        else:
                            exit()
    if (opt == 1):
        print("Record Not Found")

def view_country():
    i=1
    count=0
    choose=0
    print("\t\t===============================================")
    driver = '{Microsoft Access Driver (*.mdb, *.accdb)}' #which database we are using
    filepath = r'C:\Users\Adib\Desktop\New folder\incubyte_Hospital\hospital1.accdb'    #location of the database
    conn=pyodbc.connect(driver= driver, dbq=filepath, autocommit=True ) #eastablished the connection
    cursor=conn.cursor()
    try:
        table_name=input("\t\t|Write the Country name :- ")
        table_name=table_name.lower()
        query = "SELECT * FROM {}".format(table_name)
        cursor.execute(query)
    except:
        print("Sorry we do not have branch in that country")
        exit()
    print("\t\t===============================================")
    print("\t\tPlease Select The Foramt:                     |")
    print("\t\t|1.PIPE DELIMETER")
    print("\t\t|2.BOX FORMAT")
    choose=int(input("\t\t|Please Enter : "))
    if (choose == 1):
        try:
            while(i==1):
                os.system('CLS')
                print("========================================")
                print("Details of the customer               |")
                print("|H|Customer_Records|")
                for row in cursor.fetchall():
                    print("|D|",end="")
                    for i in row:
                        print(i,"|",end="")
                    print()
                    count=count+1
                print("|T|",count,"|")
                print("\t\t=========================================")
                print("\t\t===============================================")
                print("\n\t\t|Do you like to do more activity if yes then press 1 ")
                yes=int(input("\t\t|Please Enter : "))
                if(yes == 1):
                    os.system('CLS')
                    hospital_data_menu()
                else:
                    exit()
        except:
            i==2
    elif(choose == 2):
        try:
            while(i==1):
                inneronerow=cursor.fetchone()
                print("\t\t========================================")
                print("\t\t|Details of the customer               |")
                print("\t\t|Customer Name : ",inneronerow.Customer_Name)
                print("\t\t|Customer ID : ",inneronerow.Customer_ID)
                print("\t\t|Customer Open Date : ",inneronerow.Customer_Open_Date)
                print("\t\t|Customer Last Last_Consulted_Date : ",inneronerow.Last_Consulted_Date)
                print("\t\t|Customer Vaccination Type : ",inneronerow.Vaccination_Type)
                print("\t\t|Doctor Consulted : ",inneronerow.Doctor_Consulted)
                print("\t\t|Customer State : ",inneronerow.State)
                print("\t\t|Customer Country : ",inneronerow.Country)
                print("\t\t|Customer Postcode : ",inneronerow.Postcode)
                print("\t\t|Customer Date of Birth : ",inneronerow.DOB)
                print("\t\t|Active : ",inneronerow.Active_Customer)
                print("\t\t===============================================")
                print("\n\t\t|Do you like to do more activity if yes then press 1 ")
                yes=int(input("\t\t|Please Enter : "))
                if(yes == 1):
                    os.system('CLS')
                    hospital_data_menu()
                else:
                    exit()
        except:
            i==2
    else:
        print("Wrong Input")

home_page()
