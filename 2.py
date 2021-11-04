
class Datee:
    
    hesCodesSet = set()
    
    def datetimee():
        
        import datetime
        now = datetime.datetime.now()
        date = datetime.datetime.strftime(now, '%c')
        return date

    def HEScode():
        
        import random
        a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','P','R','S','O','V','T','Y','Z','Q','W']
        n = ['1','2','3','4','5','6','7','8','9']
        
        r1 = random.sample(a,3)
        r1.append(' ')
        r1.append('-')
        r1.append(' ')
     
        r2 = random.sample(n,3)
        r2.append(' ')
        r2.append('-')
        r2.append(' ')

        r3 = random.sample(a, 3)
        r3.append(' ')
        r3.append('-')
        r3.append(' ')
    
        r4 = random.sample(n, 3)
        
        sumL = r1 + r2 + r3 + r4
        aa = ''.join(sumL)
        
        lenn = len(Datee.hesCodesSet)
        Datee.hesCodesSet.add(aa)
        if lenn == len(Datee.hesCodesSet):
            r1 = random.sample(a,3)
            r1.append(' ')
            r1.append('-')
            r1.append(' ')
         
            r2 = random.sample(n,3)
            r2.append(' ')
            r2.append('-')
            r2.append(' ')
    
            r3 = random.sample(a, 3)
            r3.append(' ')
            r3.append('-')
            r3.append(' ')
        
            r4 = random.sample(n, 3)
            
            sumL = r1 + r2 + r3 + r4
            aa = ''.join(sumL)
            Datee.hesCodesSet.add(aa)
            return aa
        else:
            return aa
            
            














        
        