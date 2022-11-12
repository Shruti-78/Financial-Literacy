class Schemes:
    def insurance(self,sal):
        print("1 Medical Insurance")
        print("2 ")
    def loan(self,sal):
        pass
    def pay_bills(self):
        pass
    def crypto(self):
        print("1.Bitcoin")
        print("2.Dogecoin")
        print("3.Ethereum")
        print("4.Tether")
        print("5.XRP")
        crypto=input("Enter the name of Crypto Currency : " )
        if crypto.lower() == "bitcoin":
            current_price=14_16_92_6
            print("Current price: ",current_price)
            choice=input("Do you want to Buy ? enter yes for no")
            if choice.lower() == "yes":
                coin=float(input("Enter the number of coins you want to Buy: "))
                price = current_price*coin
                print("Total payable amount: ",price)
        elif crypto.lower() == "dogecoin":
            current_price = 7.33
            print("Current price: ",current_price)
            choice=input("Do you want to Buy ? enter yes for no")
            if choice.lower() == "yes":
                coin=float(input("Enter the number of coins you want to Buy: "))
                price = current_price*coin
                print("Total payable amount: ",price)
        elif crypto.lower() == "ethereum":
            current_price = 98_08_3
            print("Current price: ",current_price)
            choice=input("Do you want to Buy ? enter yes for no")
            if choice.lower() == "yes":
                coin=float(input("Enter the number of coins you want to Buy: "))
                price = current_price*coin
                print("Total payable amount: ",price)
        elif crypto.lower() == "tether":
            current_price = 80.60
            print("Current price: ",current_price)
            choice=input("Do you want to Buy ? enter yes for no")
            if choice.lower() == "yes":
                coin=float(input("Enter the number of coins you want to Buy: "))
                price = current_price*coin
                print("Total payable amount: ",price)
        elif crypto.lower() == "xrp":
            current_price = 29.74
            print("Current price: ",current_price)
            choice=input("Do you want to Buy ? enter yes for no")
            if choice.lower() == "yes":
                coin=float(input("Enter the number of coins you want to Buy: "))
                price = current_price*coin
                print("Total payable amount: ",price)
        else:
            print("Invalid Currency name!!")


    def women_schemes(self):
          print("1.Pradhanmantri Ujjwala Yojana ")
          print("2.Sukanya Yojana ")
          print("3.beti bachao beti padhavo yojana")
          yojana = input("Enter the number of Yojana :")
          if(yojana=="1"):
              print("Pradhanmantri Ujjwala Yojana")
              print("****Details****")
              print('''Cash assistance for PMUY connections is provided by Government of India - Rs. 1600 (for a connection 14.2kg cylinder/ Rs. 1150 for a 5 kg cylinder). \n The cash assistance covers:\nSecurity Deposit of Cylinder – Rs. 1250 for 14.2 kg cylinder/ Rs. 800 for 5 kg cylinder\nPressure Regulator – Rs. 150\nLPG Hose – Rs. 100\nDomestic Gas Consumer Card – Rs. 25\nInspection/ Installation/ Demonstration charges – Rs. 75\nAdditionally, All PMUY beneficiaries will be provided with first LPG refill and Stove (hotplate) both free of cost along with their deposit free connection by the Oil Marketing Companies (OMCs).''')
              print("For more details visit https://web.umang.gov.in/landing/department/pradhan-mantri-ujjwala-yojna-pmuy.html")
          elif(yojana == "2"):
              print("Sukanya Yojana")
              print("****Details****")
              print('''Sukanya Samriddhi Yojana is a Small Savings Scheme of the Government of India meant exclusively for a girl child. The scheme is meant to meet the education and marriage expenses of a girl child.\nOnly ONE account can be opened in the name of a girl child (who is a resident Indian citizen) either in Post Office or in authorized commercial Banks. An Account under these rules shall be opened for a maximum of two girl children in one family under normal conditions.''')
              print("For more detils visit https://www.centralbankofindia.co.in/en/node/1640#:~:text=Sukanya%20Samriddhi%20Yojana%20is%20a,expenses%20of%20a%20girl%20child.")
          elif(yojana == "3"):
              print("beti bachao beti padhavo yojana")
              print("****Details****")
              print('''The scheme is divided into three components – (1) advocacy campaigns were launched to address the issue of declining CSR and SBR; (2) multi-sectoral interventions were planned and are being implemented in gender-critical districts across the country; and (3) a financial incentive-linked scheme—Sukanya Samriddhi scheme—was launched to encourage parents to build a fund for female children.''')
              print("For more details visit https://www.ibef.org/government-schemes/beti-bachao-beti-padhao")
          else:
              print("Invalid Input!!")
obj=Schemes()
obj.crypto()
obj.women_schemes()
