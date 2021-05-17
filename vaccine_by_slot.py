import requests
import json
import random
import re
import datetime
import os

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

TodayDate = datetime.datetime.now()
ExactTodayDate = TodayDate.strftime("%d-%m-%Y")
Pincode = 560095


user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
]
url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=%s&date=%s' % (Pincode,ExactTodayDate)


user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent}
response = requests.get(url,headers=headers)
ResponseFromCowin = (response.text)
test = (response.json())


FindCentreidFromResponse = re.findall("center_id",ResponseFromCowin)
FindCentreid = FindCentreidFromResponse.count("center_id")
FindSessionsFromResponse = re.findall("session_id",ResponseFromCowin)
FindSessions = FindSessionsFromResponse.count("session_id")


for i in range(FindCentreid):
    print("=============================================================")
    print("Vaccination Centre Name =",test['centers'][i]['name'])
    Vaccination_Center_Name = test['centers'][i]['name']
    print("Vaccination Centre Address =",test['centers'][i]['address'])
    print("Vaccination Centre Pincode =",test['centers'][i]['pincode'])
    print("From Time =",test['centers'][i]['from'])
    print("To Time =",test['centers'][i]['to'])
    print("Fee Type =",test['centers'][i]['fee_type'])
    Vaccination_Cost = test['centers'][i]['fee_type']
    sessiondecode = (test['centers'][i]['sessions'])
    changeToList = (list(sessiondecode))
    changeToList1 = (str(changeToList))
    FindSessionsFromResponse1 = re.findall("session_id",changeToList1)
    FindSessions1 = FindSessionsFromResponse1.count("session_id")
    for i in range(FindSessions1):
        if changeToList[i]['available_capacity'] or changeToList[i]['available_capacity_dose1'] or changeToList[i]['available_capacity_dose2'] > 0:
            print("Date of Vaccination =",changeToList[i]['date'])
            print("Vaccination Available =",changeToList[i]['available_capacity'])
            print("Vaccination Available Dose1 =",changeToList[i]['available_capacity_dose1'])
            print("Vaccination Available Dose2 =",changeToList[i]['available_capacity_dose2'])
            print("Vaccination Age Limt +45 =",changeToList[i]['min_age_limit'])
            Age = changeToList[i]['min_age_limit']
            print("Type of vaccination Available =",changeToList[i]['vaccine'])
            Vaccine_Type = changeToList[i]['vaccine']
            print("Available vaccination slots =",changeToList[i]['slots'])
            print("Vaccine is available please try to book a slot")
            subject = "VACCINATION ALERT !!!!: " +  "\t" + "::"  + str(TodayDate) + "\t" + ":" + "PINCODE :" + str(Pincode)+ "\t" + ":" + "VACCINATION CENTER :" + str(Vaccination_Center_Name)+ "\t" + ":" + "AGE :" + str(Age)+ "\t" + ":" + "VACCINATION TYPE :" + str(Vaccine_Type) + "\t" + ":" + "VACCINATION COST :" + str(Vaccination_Cost)
            body = "TRY TO BOOK THE VACCINATION SLOT"
            sender_email = ""          ######## SENDER EMAIL ID ###############
            receiver_email = ""        ######## RECEIVER EMAIL ID ###############
            password = ""                     ######## SENDER EMAIL ID PASSWORD ###############
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            text = message.as_string()
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)
            print("ALERT SENT")
        else:
            print("Date of Vaccination =",changeToList[i]['date'])
            print("Vaccination Available =",changeToList[i]['available_capacity'])
            print("Vaccination Available Dose1 =",changeToList[i]['available_capacity_dose1'])
            print("Vaccination Available Dose2 =",changeToList[i]['available_capacity_dose2'])
            print("Vaccination Age Limt +45 =",changeToList[i]['min_age_limit'])
            print("Type of vaccination Available =",changeToList[i]['vaccine'])
            print("Available vaccination slots =",changeToList[i]['slots'])
            print("Vaccine is not available please wait ....")
            print("VACCINATION IS NOT AVAILABLE")
            print("***************************************************************************")
response.close()



    
