prompt="How many people are in the dinning group?: "
ask=int(input(prompt))
if ask>8:
    print("you have to wait for a table.")
else:
    print("your table is ready!!")