money = int(input("Сколько вы хотите положить денег в банк?"))
procent = int(input("Под какой процент?"))
month = int(input("Срок"))
if month > 12:
    S = money + (money*(procent/100))
    print(S)
else:
    print(money)

