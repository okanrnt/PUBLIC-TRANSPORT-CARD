
class Display:
    
    def logMet():

        flag = True
        while flag:
            
            print('1: Register for Card')
            print('2: Load Remainder')
            print('3: Display Remainder')
            print('4: Display HES Code')
            print('5: All Informations')
            print('q: Quit')
            print('-------------------------')
            press = input('Choose an operation: ')
            if press == '1':
                
                Card.register()
                break
            elif press == '2':
                
                Card.loadRemainder()
                break
            elif press == '3':
                
                Card.searchRemainder()
                break
            elif press == '4':
                
                Card.displayHEScode()
                break
            elif press == '5':
                
                Card.DisplayAllInformations()
                break
            elif press == 'q':
                
                flag = False
                print('Logout.')
            else:
                print('Key error.')

Display.logMet()


























            