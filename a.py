temperature=int(input("enter todays temperature"))
if temperature<20:
   print("it is cold today")
else:
   print("it is warm today")
israining=input("is it raining today")
if israining=="yes":
   print("bring an umbrella")
windspeed=int(input("enter the wind speed "))
if windspeed>30:
   print("it is windy today")
else:
   print("it is calm today")
haspuddles=input("are there puddles in the ground")
if haspuddles=="yes":
   print("the ground is wet")
else:
   print("the ground is dry")
print("")
print("weather check completed")
print("temperature:",temperature)
print("raining",israining)
print("has puddles",haspuddles)

      