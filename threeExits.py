prompt="enter your topping you want for your pizza: "
prompt+="\nenter quit if you are finished:\n "

flag=True
while flag:
    msg=input(prompt)
    if msg=='quit':
        flag=False
        print("we have accepted your order.")
        break
    else:
        print("we will add your "+msg+" with your pizza!!")

