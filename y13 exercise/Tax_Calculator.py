

wi = int(input("What is your weekly income before tax?"))

pay = wi * 55



ten = pay * 0.895

seven = pay * 0.825

three = pay * 0.70

threee = pay * 0.65

if pay <= 14000:
    print("10 Your yearly income before tax is ${} after tax is ${} and your weekly income is ${}.".format(pay, ten, wi))

if pay <= 48000 and pay >= 14001:
    print("7 Your yearly income before tax is ${} after tax is ${} and your weekly income is ${}.".format(pay, seven, wi))

if pay <= 70000 and pay >= 48001:
    print("3 Your yearly income before tax is ${} after tax is ${} and your weekly income is ${}.".format(pay, three, wi))

if pay <= 180000 and pay >= 70001:
    print("33 Your yearly income before tax is ${} after tax is ${} and your weekly income is ${}.".format(pay, threee, wi))

