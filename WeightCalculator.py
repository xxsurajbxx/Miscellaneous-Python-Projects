weight = input("Weight: ")
LoK = input("Lbs or Kgs: ")
if LoK.lower() == "lbs":
    int(weight)
    if int(weight) > 150:
        weight_in_kgs = int(weight) * 0.453592
        print(f"you weigh {weight_in_kgs} in kgs fatass")
    elif int(weight) <= 150:
        weight_in_kgs = int(weight) * 0.453592
        print(f"you weigh {weight_in_kgs} in kgs")
elif LoK.lower() == "kgs":
    if int(weight) > 68:
        weight_in_lbs = int(weight) * 2.20462
        print(f"you weigh {weight_in_lbs} in lbs fatso")
    elif int(weight) <= 68:
        weight_in_kgs = int(weight) * 2.20462
        print(f"you weigh {weight_in_kgs} in kgs")