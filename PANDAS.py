import pandas as pd

pd.set_option('display.max_columns', None)

data = pd.read_csv("ingredients.csv")

data = data[["unhealthy", "healthy", "healthy1", "healthy2", "conversion", "conversion1", "conversion2"]]
data2 = data.set_index("unhealthy", drop = True)
healthy = data2.loc[ : ,"healthy" : "healthy2" ]
#print(healthy)
conversions = data2.loc[ : ,"conversion" : "conversion2"]
#print(conversions)


for i in data["unhealthy"]:
    useramount = ""
    row = data2.loc[i, : ]
    healthrow = healthy.loc[i, : ]
    #print(healthrow)
    convertrow = conversions.loc[i, : ]
    #print(convertrow)
    while not useramount.isdigit():
        useramount = input(f"How many {i} do you want: ")
    useramount = int(useramount)
    number = 0
    for j in healthrow:
        if j != "None":
            if number == 0:
                number = ""
            elif number > 0:
                number = str(number)
            #print(number)
            amount = float(convertrow[f"conversion{number}"]) * useramount
            print(f"You could use {amount} of {j}")
            if number.isdigit():
                number = int(number)
                number += 1
            elif number == "":
                number = 1
    number = 0