import math

acc = 1000

all_customers = []
customer_slab1 = []
customer_slab2 = []
customer_slab3 = []
customer_slab4 = []


class User:
    schemes = []

    def __init__(self, name, age, phn_no, salary, city, gmail, acc_n, passw):
        self.gmail = gmail
        self.name = name
        self.age = age
        self.phone_number = phn_no
        self.salary = salary
        self.city = city
        self.acc_no = acc_n
        self.balance = 0
        self.password = passw

    def saving(self):
        saving_amt = float((self.salary * 20) / 100)
        print("Your Saving Amount Must be ", saving_amt)

    def withdraw(self, amount_to_with):
        if self.balance - amount_to_with < 0:
            print("Insufficient balance to withdraw")
        else:
            self.balance -= amount_to_with
            print("Amount withdrawn successfully")

    def deposit(self, amount_to_deposit):
        self.balance += amount_to_deposit
        print("Amount deposited successfully")

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Mail: ", self.gmail)




class Scheme:
    def loan(self):
        elig_loan = 250000 * 15
        print("You are eligible to pursue a loan upto Rs.", elig_loan)
        loan = int(input("Enter the amount of loan you want to pursue: "))
        time = int(input("For how long will you need this loan?(years) : "))
        if loan > elig_loan:
            print("\nSORRY! The request couldn't be processed...\nYou are not eligible for a loan of this amount...")
            loan = 0
        else:
            print(
                "\nYour loan is being processed to your account!\nIt might take some time for the transaction to be "
                "processed...")
            rate = 6
            interest = loan * math.pow((1 + rate / 100), time)
            amount = loan + interest
            print("\nLOAN PROCESSED! \n You now owe Rs.", amount, "(inclusive of all taxes)")

    def insurance(self):
        print("1.Tata AIG Wellsurance Woman Policy")
        print("2.Care Health Insurance Joy Policy")
        print("3. Bajaj Allianz Women Specific Critical Illness Plan")
        print("4.Star Women Care Insurance Plan")
        print("5.HDFC ERGO Women Cancer Plus Plan")
        insurance = input("Enter the number of insurance: ")
        if insurance == "1":
            print("Tata AIG Wellsurance Woman Policy")
            print(
                '''The Tata AIG Wellsurance Woman Policy is a health cum wellness plan that is designed especially for women.\n With the Tata AIG Wellsurance Woman Policy, women can get coverage for critical illness, cosmetic reconstructive surgery, and many more.\nTax benefits can also be enjoyed with Tata AIG Wellsurance Woman Policy as mentioned under section 80D of the Income Tax Act.\n Please note that the minimum eligibility criteria for this plan is 18 years and the maximum is 65 years.''')
            print("For more details visit https://www.insurancedekho.com/health-insurance/tata-aig ")
        elif insurance == "2":
            print("Care Health Insurance Joy Policy")
            print(
                '''Another women-oriented health insurance that you can consider buying is the Care Health Insurance Joy Policy.\n The Care Health Insurance Joy Policy is aimed at providing coverage for pregnant women.\n Almost all maternity related expenses are covered under\n Care Health Insurance Joy Policy so that pregnant women can\n enjoy this beautiful phase of their life without worrying\n much about the expenses.\n Also, the Joy Policy offered by Care Health Insurance has a waiting\n period of just 9 months and even offers newborn baby cover''')
            print("For more details visit https://www.careinsurance.com/buy-maternity-health-insurance-plan.html")
        elif insurance == "3":
            print("Bajaj Allianz Women Specific Critical Illness Plan")
            print(
                '''Another women-oriented health insurance that you\n can consider buying is the Care Health Insurance Joy Policy.\n The Care Health Insurance Joy Policy is aimed at\n providing coverage for pregnant women.\nAlmost all maternity related expenses are covered under\n Care Health Insurance Joy Policy so that pregnant women\n can enjoy this beautiful phase of their life \nwithout worrying much about the expenses.\nAlso, the Joy Policy offered by Care Health Insurance\n has a waiting period of just 9 months and \neven offers newborn baby cover.''')
            print("For more details visit https://www.bajajallianz.com/")
        elif insurance == "4":
            print("Star Women Care Insurance Plan")
            print(
                '''Women aged between 18-75 years can enjoy the benefits\n of the Star Women Care Insurance Plan. \nThe Star Women Care Insurance Plan offered by Star Health \nInsurance provides coverage for women and their dependents.\n The Star Women Care Insurance Plan comes with different\n options under ‘sum insured’ such as Rs.5,00,000/-,\n Rs.10,00,000/-, Rs.15,00,000/-, Rs.20,00,000/- , Rs.25,00,000/-,\n Rs.50,00,000/- and Rs.1,00,00,000/. Depending on the budget\n as well as requirements, women can pick a preferred\n sum insured. ''')
            print("For more details visit https://www.reliancegeneral.co.in/")
        elif insurance == "5":
            print("HDFC ERGO Women Cancer Plus Plan")
            print(
                '''The HDFC ERGO Women Cancer Plus Plan as\n the name suggests is aimed at providing much-needed\n financial protection to all those women who are\n struggling with cancer. As the medical expenses \nfor cancer treatment are quite high, the HDFC \nERGO Women Cancer Plus Plan is a must-have for women.\n Along with cancer, major illness is also covered\n and even minor burns are included as coverage\n under the HDFC ERGO Women Cancer Plus Plan.\n''')
            print("For more details visit https://www.hdfcergo.com/")
        else:
            print("Invalid input!!")

    def pay_bills(self):
        print("1 Electricity Bill")
        print("2 Water Bill")
        choice = int(input("Enter the option"))
        if choice == 1:
            input("Enter customer no: ")
            print("Click on the link to pay your bill")
            print("https://wss.mahadiscom.in/wss/wss?uiActionName=getViewPayBill")
        if choice == 2:
            input("Enter customer no: ")
            print("Click on the lik to pay your bill")
            print("https://mjp.maharashtra.gov.in/en/water-bill-payment")

    def crypto(self):
        print("1.Bitcoin")
        print("2.Dogecoin")
        print("3.Ethereum")
        print("4.Tether")
        print("5.XRP")
        crypto = input("Enter the name of Crypto Currency : ")
        if crypto.lower() == "bitcoin":
            current_price = 14_16_92_6
            print("Current price: ", current_price)
            choice = input("Do you want to Buy ? enter yes for no")
            if choice.lower() == "yes":
                coin = float(input("Enter the number of coins you want to Buy: "))
                price = current_price * coin
                print("Total payable amount: ", price)
        elif crypto.lower() == "dogecoin":
            current_price = 7.33
            print("Current price: ", current_price)
            choice = input("Do you want to Buy ? enter yes for no")
            if choice.lower() == "yes":
                coin = float(input("Enter the number of coins you want to Buy: "))
                price = current_price * coin
                print("Total payable amount: ", price)
        elif crypto.lower() == "ethereum":
            current_price = 98_08_3
            print("Current price: ", current_price)
            choice = input("Do you want to Buy ? enter yes for no")
            if choice.lower() == "yes":
                coin = float(input("Enter the number of coins you want to Buy: "))
                price = current_price * coin
                print("Total payable amount: ", price)
        elif crypto.lower() == "tether":
            current_price = 80.60
            print("Current price: ", current_price)
            choice = input("Do you want to Buy ? enter yes for no")
            if choice.lower() == "yes":
                coin = float(input("Enter the number of coins you want to Buy: "))
                price = current_price * coin
                print("Total payable amount: ", price)
        elif crypto.lower() == "xrp":
            current_price = 29.74
            print("Current price: ", current_price)
            choice = input("Do you want to Buy ? enter yes for no")
            if choice.lower() == "yes":
                coin = float(input("Enter the number of coins you want to Buy: "))
                price = current_price * coin
                print("Total payable amount: ", price)
        else:
            print("Invalid Currency name!!")

    def mahila_bachat_gat(self):
        print("mahila bachat gat available in following cities : ")
        print("Pune\nKolhapur\nSangli ")
        city = input("1.Enter the city name: ")
        if city.lower() == "pune":
            print("Here are some available mahila bachat gat names : ")
            print("1.Krushna mahila bachat gat")
            print("2.Anusuya mahila bachat gat")
            print("3.Swara mahila bachat gat")
            print("4.Gajanan mahila bachat gat")
            name = input("Enter the number of the mahila bachat gat: ")
            if name == "1":
                print(
                    '''Krushna mahila bachat gat\nAddress:Survey No. 18, Sai NagarKondhwa Budruk, Pune - 411048\n Contact no.9876256562''')
                print(
                    "For more details visit https://www.sulekha.com/krushna-mahila-bachat-gat-kondhwa-budruk-pune-contact-address")
            elif name == "2":
                print(
                    '''Anusuya mahila bachat gat\n Address:495/96 Elina Apartment, Mehun Pura, \nShaniwar Peth, Pune - 411030, Neardakshin Maruti Mandir\n Contact no.9049068863''')
                print(
                    "For more details visit https://www.justdial.com/Pune/Anusuya-Mahila-Bachat-Gat-Neardakshin-Maruti-Mandir-Shaniwar-Peth/020PXX20-XX20-160926130309-X8Z6_BZDET")
            elif name == "3":
                print(
                    '''Swara mahila bachat gat\n Address:Sr No 26 Munjoba Wasahat Chinchwade Nager Chinchwad, Pune \n Contact no:9766611008.''')
                print(
                    "For more details visit https://aadharcenter.com/Swara-Mahila-Bachat-Gat-contact-Prashant-Mohan-Thakare-mobile-9766611008/")
            elif name == "4":
                print(
                    '''Gajanan mahila bachat gat\n Address:S. No. 53, 53/1, Kalepadal, Gajanan Colony, Hadapsar, Pune\n Contact no:9922652307''')
                print("For more details visit https://gajanan-mahila-bachat-gat.business.site/")
            else:
                print("Invalid Input!!")
        elif city.lower() == "kolhapur":
            print("1.Sneha Mahila Bachat Gat")
            print("2.Jijamata Sway Sahayya Mahila Bachat Gat ")
            print("3.Anjaniprabha Mahila Bachat Gat ")
            print("4.Shri Sai Mahila Bachat Gat")
            name = input("Enter the number of the mahila bachat gat: ")
            if name == "1":
                print(
                    '''Sneha Mahila Bachat Gat\nAddress:Kolhapur HO, Kolhapur - 416003, Balwant Nagar\n Contact no:9850006125''')
                print(
                    "For more Details visit https://www.justdial.com/Kolhapur/Sneha-Mahila-Bachat-Gat-Balwant-Nagar-Kolhapur-HO/0231PX231-X231-130401101609-T2K8_BZDET")
            elif name == "2":
                print(
                    '''Jijamata Sway Sahayya Mahila Bachat Gat \n Address:Tervan, Kolhapur - 416509\n Contact no:9595779033''')
                print(
                    "For more details https://www.justdial.com/Kolhapur/Jijamata-Sway-Sahayya-Mahila-Bachat-Gat/0231PX231-X231-180224155029-E8F6_BZDET")
            elif name == "3":
                print(
                    '''Anjaniprabha Mahila Bachat Gat\n Address:787/2/PL NO 6 Ramanand Nagar Kolhapur\n Contact no:9876345698''')
                print(
                    "For more details visit https://www.mastersindia.co/gst-search/?name=anjaniprabha-mahila-bachat-gat-kolhapur&gstin=27AAGAA2707H1Z0")
            elif name == "4":
                print(
                    '''Shri Sai Mahila Bachat Gat\n Address:Karnal Sangli Pre Sou Rajshri M Hipparkar 416416 Kolhapur\n Contact no:8796457690''')
                print("For more details https://local.infobel.in/IN106666918/shri_sai_mahila_bachat_gat-kolhapur.html")
            else:
                print("Invalid Input!!!")
        elif city.lower() == "sangli":
            print("1.Jyotirling Mahila Bachat Gat")
            print("2.Shri Dhanlaxmi Swayamsahayata Mahila Bachat Gat")
            print("3.Anushka Mahila Bachat Gat ")
            print("4.Sarsvati Mahila Bachat Gat")
            name = input("Enter the number of the mahila bachat gat: ")
            if name == "1":
                print(
                    '''Jyotirling Mahila Bachat Gat\n Address:Malia Nivas Mali Vasti, Jijamata Colony Abhayanagar Sangli\n Contact no:8796458734''')
                print(
                    "For more details visit https://www.dnb.com/business-directory/company-profiles.jyotirling_mahila_bachat_gat.89279d4352f4db48a7244a9147c89bba.html")
            elif name == "2":
                print(
                    '''Shri Dhanlaxmi Swayamsahayata Mahila Bachat Gat\n Address:AP Tadavale Tal, Sangli\n Contact no:7689564390''')
                print(
                    "For more details visit https://local.infobel.in/IN105021226/shri_dhanlaxmi_swayamsahayata_mahila_bachat_gat-sangli.html")
            elif name == "3":
                print(
                    '''Anushka Mahila Bachat Gat \n Address:A P Anita Subhash Shinde Kavthepiranmarathi Shala,Sangli\n Contact no:78965090''')
                print(
                    "For more details visit https://local.infobel.in/IN111347730/anushka_mahila_bachat_gat-sangli.html")
            elif name == "4":
                print(
                    '''Sarsvati Mahila Bachat Gat\n Address:VH2J+XH5, South Shivaji Nagar, Nishant Colony, Sangli Miraj Kupwad\n Contact no: 9879897689 ''')
                print(
                    "For more details visit https://local.infobel.in/IN104484184/saraswati_swayam_sahyyata_mahila_bachat_gat-sangli.html")
            else:
                print("Invalid Input!!")
        else:
            print("Currently data not available please visit next time!")

    def women_schemes(self):
        print("1.Pradhanmantri Ujjwala Yojana ")
        print("2.Sukanya Yojana ")
        print("3.beti bachao beti padhavo yojana")
        yojana = input("Enter the number of Yojana :")
        if (yojana == "1"):
            print("Pradhanmantri Ujjwala Yojana")
            print("****Details****")
            print(
                '''Cash assistance for PMUY connections is provided by Government of India - Rs. 1600 (for a connection 14.2kg cylinder/ Rs. 1150 for a 5 kg cylinder). \n The cash assistance covers:\nSecurity Deposit of Cylinder – Rs. 1250 for 14.2 kg cylinder/ Rs. 800 for 5 kg cylinder\nPressure Regulator – Rs. 150\nLPG Hose – Rs. 100\nDomestic Gas Consumer Card – Rs. 25\nInspection/ Installation/ Demonstration charges – Rs. 75\nAdditionally, All PMUY beneficiaries will be provided with first LPG refill and Stove (hotplate) both free of cost along with their deposit free connection by the Oil Marketing Companies (OMCs).''')
            print(
                "For more details visit https://web.umang.gov.in/landing/department/pradhan-mantri-ujjwala-yojna-pmuy.html")
        elif (yojana == "2"):
            print("Sukanya Yojana")
            print("****Details****")
            print(
                '''Sukanya Samriddhi Yojana is a Small Savings Scheme of the Government of India meant exclusively for a girl child. The scheme is meant to meet the education and marriage expenses of a girl child.\nOnly ONE account can be opened in the name of a girl child (who is a resident Indian citizen) either in Post Office or in authorized commercial Banks. An Account under these rules shall be opened for a maximum of two girl children in one family under normal conditions.''')
            print(
                "For more detils visit https://www.centralbankofindia.co.in/en/node/1640#:~:text=Sukanya%20Samriddhi%20Yojana%20is%20a,expenses%20of%20a%20girl%20child.")
        elif (yojana == "3"):
            print("Beti Bachao Beti Padhao Yojana")
            print("****Details****")
            print(
                '''The scheme is divided into three components – (1) advocacy campaigns were launched to address the issue of declining CSR and SBR; (2) multi-sectoral interventions were planned and are being implemented in gender-critical districts across the country; and (3) a financial incentive-linked scheme—Sukanya Samriddhi scheme—was launched to encourage parents to build a fund for female children.''')
            print("For more details visit https://www.ibef.org/government-schemes/beti-bachao-beti-padhao")
        else:
            print("Invalid Input!!")


print("1 Create a new account")
print("2 Login to your account")
print("3 View Schemes")
print("4 Deposit money in your account")
print("5 Withdraw money from your account")
print("6 Exit")
menu = int(input("Enter the action you want to perform: "))
if menu == 1:
    name = input("Enter the name : ")
    mail = input("Enter your gmail: ")
    pw = input("Enter password: ")
    age = input("Enter the age : ")
    phone_no = input("Enter the phone number : ")
    salary = int(input("Enter the salary : "))
    city = input("Enter the city : ")
    acc_no = acc + 1
    new_cust = User(name, age, phone_no, salary, city, mail, acc_no, pw)
    new_cust.new_customer(salary)
    print("Thank you for registering with Mahila Arthkosh!")
    print("Your account has been successfully created.")
    new_cust.saving()
    if salary < 300000:
        customer_slab1.append(new_cust)
    elif 300000 <= salary < 500000:
        customer_slab2.append(new_cust)
    elif 500000 <= salary < 750000:
        customer_slab3.append(new_cust)
    else:
        customer_slab4.append(new_cust)
    all_customers.append(new_cust)
    acc += 1
if menu == 2:
    mail = input("Enter your email: ")
    input("Enter password: ")
    print("Logged in successfully")
    print("Available Schemes are:")
    print("1 Loans")
    print("2 Insurance")
    print("3 Pay Bills")
    print("4 Crypto")
    print("5 Women Schemes")
    print("6 Mahila Bachat Gat")
    print("7 Logout")
    schm = 0
    while schm==0 or schm == 1 or schm == 2 or schm == 3 or schm == 4 or schm == 5 or schm == 6:
        schm = int(input("Enter the number of the scheme you would like to know about "))
        schemes = Scheme()
        if schm == 1:
            schemes.loan()
        elif schm == 2:
            schemes.insurance()
        elif schm == 3:
            schemes.pay_bills()
        elif schm == 4:
            schemes.crypto()
        elif schm == 5:
            schemes.women_schemes()
        elif schm == 6:
            schemes.mahila_bachat_gat()




