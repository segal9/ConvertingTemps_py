# first determine from the user the units they desire"
unit = input("What is the desired temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp )/ 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp} °F") # to get degrees hit in win: Alt + 0176
elif unit == "F":
    #pass
    temp = round(( temp - 32 ) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp} °C") # to get degrees hit in win: Alt + 0176
    
else:
    print(f"{unit} is the wrong unit chosen. Try again please.")