print('welcome to our restuarant')
match food_type:
    case 1:
        print('1. roti sabji 2:poha')
        user_choice = int(input('enter your choice of food:'))
        match user_choice:
            case 1: print()

    case 2:

        print('1:Idly 2:Dosa 3: upma 4:puri')
        user_choice = int(input('enter your choice of food:'))

        match user_choice:
            case 1 : print()
    

    case _ : print('this is')

user_choice = int(input('do you wish to have'))
 print('visist again')