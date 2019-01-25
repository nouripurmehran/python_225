import requests
import datetime


now = datetime.datetime.now()
today_date = datetime.date.today()

today_date = str(today_date)

text = open("text", "r")

for line in text:
    x = line.split(",")
    log = open("logfile.txt", "a")
    if today_date == x[0]:

        send_url = "https://api.kavenegar.com/v1/567235414F68622B506B694C634D66552B6B78667952324F424142764A753772/sms/send.json"

        sms = {"receptor": x[2], "message": x[1]}
        delivery = requests.post(send_url, data=sms)

        delivery = str(delivery)

        if delivery == "<Response [200]>":
            log.write(f"sended {now}\n")
        elif delivery == "<Response [418]>":
            log.write(f"Account credit is not enough {now}\n")
        elif delivery == "<Response [414]>":
            log.write(f"The number of recipients is greater than the limit {now}\n")
        else:
            log.write(f"An error has occurred {now}\n")

    else:
        log.write(f"Do not have any remind for this date  {now}\n")
    log.close()
text.close()
