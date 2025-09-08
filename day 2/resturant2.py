print('Welcome to our restaurant THE TASTE')

food_type = int(input('1:North 2:South. Your choice Please: '))
match food_type:
    case 1 :
        print('1:Roti-Subji 2:Poha 3:Samosa 4:pav-bhaji')
        user_choice = int(input('Enter your choice of food: ')) 
        match user_choice:
            case 1 : print('Roti-Subji')
            case 2 : print('Poha')
            case 3 : print('Samosa')
            case 4 : print('pav-bhaji')
            case _ : print('Protein rich Cockroaches for you Maam')
    case 2 : 
        print('1:Idly 2:Dosa 3:Upma 4:Puri')
        user_choice = int(input('Enter your choice of food: '))
        match user_choice:
            case 1 : print('Yummy and soft Idli for you')
            case 2 : print('The famous Milari Dosa')
            case 3 : print('The tasty Brahmin Upma ')
            case 4 : print('Hot and Spicy Channa-Puri')
            case _ : print('Protein rich Cockroaches for you Maam')
    case _ : print('This is not Garden Maamu')
print('Thank you Visit again!')