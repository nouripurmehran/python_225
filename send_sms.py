import requests

send_url = "https://api.kavenegar.com/v1/567235414F68622B506B694C634D66552B6B78667952324F424142764A753772/sms/send.json"

sms = {"receptor": "09359606252", "message": "salaaaaam"}

delivery = requests.post(send_url, sms)
print(delivery)
