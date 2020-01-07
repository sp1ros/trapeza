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
        self.pel.append(p)
        

        
    def katathesi(self,katath):
        self.poso= self.poso + katath
        print("Νέο υπόλοιπο= ",self.poso)

    def analipsi(self,analip):
        if self.poso>analip:
            self.poso=self.poso - analip
            print("Νέο υπόλοιπο= ",self.poso)
        else:
            print("ποσο αναληψης μεγαλυτερο απο υπολοιπο")

    
    def show(self):
        
        print("Υπόλοιπο: ",self.poso)
        


    

def menu():
    P=[]
    L=[]


  
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
            elif(x==3):
                a=int(input("Αριθμός Λογαριασμού :"))
                fnd=0
                for katlog in L:
                    if(katlog.code==a):
                        kata=int(input("Ποσό κατάθεσης :"))
                        katlog.katathesi(kata)
                        fnd=1
                        
                if(fnd==0):
                    print("Δεν υπάρχει ο λογαριασμός")

            elif(x==4):
                a=int(input("Αριθμός Λογαριασμού :"))
                fnd=0
                for katlog in L:
                    if(katlog.code==a):
                        an=int(input("Ποσό ανάληψης :"))
                        katlog.analipsi(an)
                        fnd=1
                        
                if(fnd==0):
                    print("Δεν υπάρχει ο λογαριασμός")
            elif(x==5):
                
                ip=int(input("αριθμός λογαριαάσμου :"))
                fnd=0
                for katlog in L:
                    if(katlog.code==ip):
                        katlog.show()
                        fnd=1
                if(fnd==0):
                    print("Δεν υπάρχει ο λογαριασμός")
            elif(x==6):
                af=input("δώσε ΑΦΜ πελάτη :")
                s=0
                for i in L:
                    for j in i.pel:
                       if (j.afm==af):
                           s+=i.poso
                print("συνολικο υπλοιπο πελατη =",s)

                
            elif(x==7):
                s=0
                for j in L:
                    s+=j.poso
                print("συνολικό τράπεζας = ",s)
                    
                
            elif(x==8):
                file=open("data.txt","w")
                file.write(str(len(P))+"\n")
                file.write(str(len(L))+"\n")
            
                for pp in P:
                    file.write(pp.onoma + "\n")
                    file.write(pp.tilefono + "\n")
                    file.write(pp.afm + "\n")
                for ll in L:
                    file.write(str(ll.code)+"\n")
                    file.write(str(ll.poso)+"\n")
                    file.write(str(len(ll.pel))+"\n")
                    for p2 in ll.pel:
                        file.write(p2.afm+"\n")
                file.close()
                    
            elif(x==9):
                file=open("data.txt","r")
                
                n1=int(file.readline())
                n2=int (file.readline())
                for i in range(0,n1):
                    o=file.readline().replace("\n","")
                    t=file.readline().replace("\n","")
                    a=file.readline().replace("\n","")
                    p=pelatis()
                    p.setpel(o,t,a)
                    P.append(p)
                for i in range(0,n2):
                    l=logariasmos()
                    c=file.readline()
                    l.code=int(c)
                    ps=file.readline()
                    l.poso=int(ps)
                    n3=int(file.readline())
                    for j in range(0,n3):
                        a=file.readline().replace("\n","")
                        p1=pelatis()
                        p1.setpel("","",a)
                        l.addpelati(p1)    
                    L.append(l)
                file.close()
                
            else:
                for pp in P:
                    pp.show()
                    print("-------------------------")
            
        except Exception as e:
           print ("error2 ",e)


menu()  


