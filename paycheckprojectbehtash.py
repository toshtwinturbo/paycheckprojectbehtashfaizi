user = str
end = False
hours = round(40,2)
print("Paycheck Analyzer")
while end == False:
  user = input("\nPlease enter your name or type 'exit' to quit: ")
  if user == "exit":
     print("Goodbye!")
     break
  else:
     hours = (float(input("Please input weekly hours worked: ", )))
     payrate =(float(input("Please input hourly pay: ", )))
  if hours <= 40:
     print("Employee's name: ", user)
     print("Overtime hours: 0")
     print("Overtime Pay: $0.00")
     regularpay = round(hours * payrate, 2)
     fedtax = float(regularpay * .15)
     statetax = float(regularpay * .10)
     fica = float(regularpay * .2)
     print("Gross Pay: $", regularpay)
     print("Federal Tax: $", fedtax)
     print("State Tax: $", statetax)
     print("FICA: $", fica)
  elif hours > 40:
     overtimehours = round(hours - 40.00,2)
     print("Employee's name: ", user)
     print("Overtime hours: ", overtimehours)
     regularpay = round(hours * payrate,2)
     overtimerate = round(payrate * 1.5, 2)
     overtimepay = round(overtimehours * overtimerate)
     grosspay = round(regularpay+overtimepay,2)
     fedtax = float(grosspay * .15)
     statetax = float(grosspay * .10)
     fica = float(grosspay * .2)

     print("Regular Pay: $", regularpay)
     print("Overtime Pay: $",overtimepay)
     print("Gross Pay: $", grosspay)

     print("Federal Tax: $", fedtax)
     print("State Tax: $", statetax)
     print("FICA: $", fica)