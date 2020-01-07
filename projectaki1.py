from random import randint
class pelatis:
    def __init__(self):
        self.onoma=""
        self.tilefono=""
        self.afm=""
    def setpel(self,o,t,a):
        self.onoma=o
        self.tilefono=t
        self.afm=a

    def newPel(self):
        self.onoma=input("Ονομα:")
        self.tilefono=input("Τηλεφωνο :")
        self.afm=input("ΑΦΜ :")

    def show(self):
        print(self.onoma,",", self.tilefono,",",self.afm)


class logariasmos:

    nextcode=1
    def __init__(self):
        self.code=logariasmos.nextcode
        logariasmos.nextcode=logariasmos.nextcode+1
        self.pel=[]
        self.poso=0

    def addpelati(self,p):
        print (self.code)
        self.pel.append(p)
        p.show()

        
    def katathesi(self,katath):
        self.poso= self.poso + katathesi

    def analipsi(self,analip):
        if self.poso>analip:
            self.poso=self.poso - analip
        else:
            print("ποσο αναληψης μεγαλυτερο απο υπολοιπο")

    
    def show(self):
        
        print("Kodikos:",self.code)
        print("Ypoloipo:",self.poso)
        for p in self.pel:
            p.show()

def menu():
    P=[]
    L=[]


    p1=pelatis()
    p2=pelatis()
    p1.setpel('p1','231243','11')
    p2.setpel('p2','245532','22')
    P.append(p1)
    P.append(p2)
    while(True):
        try:
            print("1. Εισαγωγή νέου πελάτη")
            print("2. Δημιουργία Λογαριασμού")
            print("3. Κατάθεση")
            print("4. Ανάλυψη")
            print("5. Υπόλοιπο λογαριασμού")
            print("6. Σύνολα πελάτη")
            print("7.Σύνολα τράπεζας")
            print("8. Αποθήκευση")
            print("9. Φόρτωση")
            print("10. Λιστα πελατών")
            
            print("0. Έξοδος")
            x=int(input("Επιλέξτε λειτουργία: "))
            if(x<0 or x>10):
                  print ("error1")
            elif(x==0):
                  break

            elif(x==1):
                  p=pelatis()
                  p.newPel()
                  P.append(p)
                 
            elif(x==2):
                l=logariasmos()
                n=int(input("Posoi dikaiouxoi?"))
                for i in range(1,n+1):
                    
                    k=input("Dose afm pelati %d?" %i)
                    fnd=0
                    for j in P:
                       
                        if(j.afm==k):
                            
                            l.addpelati(j)
                            fnd=1
                            break
                    
                    if(fnd==0):
                        print("Den vrethike")
                        i=i-1
                l.show()
                L.append(l)
            elif(x==10):
                for pp in P:
                    pp.show()
                    print("-------------------------")
            
        except:
           print ("error2")


menu()  


