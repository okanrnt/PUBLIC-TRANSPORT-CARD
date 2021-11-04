
class Back:
    
    def previo():
        
        while True:
            p = input('''Push 'p' to back: ''')
            if p == 'p':
                Display.logMet()
                break
            else:
                print('Key error. Try again please.')
        