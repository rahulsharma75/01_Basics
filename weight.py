user_weight = float(input("Please enter your weight: "))

unit_weight = input("L(bs) or K(gs): ")

if unit_weight.upper() == "L":
    converted = user_weight * 0.45
    print(f"You are {converted} kilos")
elif unit_weight.upper() == "K":
    converted = user_weight // 0.45
    print(f"You are {converted} pounds")
else: 
    print(f"please enter correct input")
    




