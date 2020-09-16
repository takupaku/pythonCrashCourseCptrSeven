prompt="enter your age: "
ask=int(input(prompt))

msg=""
while msg!='no':
    print(ask)

    if ask<3:
        print("the ticket is free!!")
        break
    elif ask>3 and ask<12:
        print("your ticket is $10!!")
        break
    else:
        print("your ticket is $15!!")
        break
