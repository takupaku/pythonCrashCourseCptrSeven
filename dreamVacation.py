dreamVacation={}

poll_activationFlag=True
while poll_activationFlag:
    name=input("what is your name?: ")
    vacation=input("where do you want to go one day?: ")
    dreamVacation[name]=vacation

    repeat=input("would you like to take another poll?(yes/no)")
    if repeat=='no':
        poll_activationFlag=False

print("-----poll result------")
for name,response in dreamVacation.items():
    print(name+' would like to go to '+response+'.')