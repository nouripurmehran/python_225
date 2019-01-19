w = open("text", "r")

for line in w:
    x = line.split(",")
    sms = {"receptor": x[2], "message": x[1]}
    print(sms)
