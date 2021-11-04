
class Card:
    
    infDict = dict()
    listID = list()
    
    def __init__(self,ID,name,surname,dateOfBirth,date):
        
        self.ID = ID
        self.name = name
        self.surname = surname
        self.dateOfBirth = dateOfBirth
        self.date = date
        self.addDict()
        self.listIDD()
        
    def addDict(self):
        
        self.infDict.update({
            self.ID : {
                'name' : self.name,
                'surname' : self.surname,
                'birth' : self.dateOfBirth,
                'remainder' : 0,
                'date' : self.date
                }
            })
        
    def listIDD(self):
        
        self.listID.append(self.ID)
        
    def register():
        
        if len(Card.listID) == 0:
            ID = 1
        else:
            ID = Card.listID[-1] + 1
            
        name = input('Name: ')
        surname = input('Surname: ')
        dateOfBirth = input('Birth: ')
        date = Datee.datetimee()
        
        Card(ID,name,surname,dateOfBirth,date)
        print('''Your ID no: {} .Don't forget it please because all operations make with it.'''.format(ID))
        print('You can get your card from cardmatic.')
        print('You must integrate your card your HES code.')
        print('*********************************************')
        push = input('push 1 to make a HES code\npush 2 to integrate to the card HES code\npush: ')
        
        while True:
            if push == '1':
                
                ID = int(input('ID NO: '))
                infD = Card.infDict[ID]
                infD['HES code'] = Datee.HEScode()
                print('Your HES code has been made and integrated.')
                break
            elif push == '2':
                
                ID = int(input('ID NO: '))
                infD = Card.infDict[ID]
                infD['HES code'] = input('HES code: ')
                print('Your HES code has been integrated.')
                print('You can check your card information.')
                break
            else:
                print('Error.Try again.')
        
        Back.previo()
                
    def loadRemainder():
        
        ID = int(input('ID: '))
        remainder = Card.infDict[ID]
        oldRemainder = remainder['remainder']
        loadRem = int(input('How many remainder do you want to load?: '))
        remainder['remainder'] = oldRemainder + loadRem
        print('Your current remainder: {}'.format(remainder['remainder']))
        Back.previo()
    def searchRemainder():
        
        ID = int(input('ID: '))
        remainder = Card.infDict[ID]
        print('Your current remainder: {}'.format(remainder['remainder']))
        Back.previo()
        
    def displayHEScode():
        
        ID = int(input('ID: '))
        HesC = Card.infDict[ID]
        print('Your HES Code: {}'.format(HesC['HES code']))
        Back.previo()
    
    def DisplayAllInformations():
        ID = int(input('ID: '))
        inff = Card.infDict[ID]
        print(inff)
        Back.previo()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    