prompt="enter your topping you want for your pizza: "
prompt+="\nenter quit if you are finished:\n "

msg=""
while msg!='quit':
    msg=input(prompt)

    if msg!='quit':
        print("we will add your "+msg+" with your pizza!!")
