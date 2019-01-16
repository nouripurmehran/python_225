w = open("num&mess", "r")

for line in w:
    x = line.split(" ")
    sms = {"receptor": x[1], "message": x[0]}
    print(sms)
