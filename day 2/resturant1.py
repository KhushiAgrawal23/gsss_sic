print('1:Idly 2:Dosa 3:Upma 4:Puri')
user_choice = int(input('Enter your choice of food: '))

match user_choice:
    case 1 : print('Yummy and soft Idli for you')
    case 2 : print('The famous Milari Dosa')
    case 3 : print('The tasty Brahmin Upma ')
    case 4 : print('Hot and Spicy Channa-Puri')
    case _ : print('Protein rich Cockroaches for you Maam')