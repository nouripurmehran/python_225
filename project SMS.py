import requests
import datetime
import calendar

now = datetime.datetime.now()
today_time = datetime.date.today()

cy = now.year
cm = now.month

last_day = calendar.monthrange(cy, cm)[1]

if today_time == last_day:

    send_url = "https://api.kavenegar.com/v1/567235414F68622B506B694C634D66552B6B78667952324F424142764A753772/sms/send.json"

    sms = {"receptor": "09359606252", "message": "salaaaaam"}

    delivery = requests.post(send_url, data=sms)

    delivery = str(delivery)

    if delivery == "<Response [200]>":
        print("پیام ارسال شد.")
    elif delivery == "<Response [418]>":
        print("اعتبار حساب شما کافی نیست . ")
    elif delivery == "<Response [414]>":
        print("تعداد دریافت کننده ها بیشتر از حد مجاز است.")
    else:
        print("خطایی رخ داده است.")

else:
    print("today is not last day of month")
