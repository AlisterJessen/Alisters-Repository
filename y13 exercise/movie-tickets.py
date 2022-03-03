ticket = int(input("enter a ticket price between $5 and $10: "))
group = int(input("enter the amount of people in your group: "))

print("the total cost of the tickets before any discount is ${}".format(ticket * group))

if group > 8:
    print("the total cost of the tickets before any discount is ${}".format(ticket * group * 0.75))

if group < 8:
    print("not enough people")