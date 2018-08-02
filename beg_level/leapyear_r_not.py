year=int(input())
if year%4==0 year % 100 != 0:
 print("leap year")
elif year%100==0:
 print(year,"not a leap year")
elif year%400==0:
 print(year,"leap year")
else:
 print(year,"not leap year")
