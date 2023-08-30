#################################### CLASS DEFINTION ##################################################
class Operations:
    
    def __init__(self, strng, substrng):
        self.strng = strng
        self.substrng = substrng
        
#################################### LONGEST WORD #####################################################

    def lngword(self):
        global wordlst
        wordlst = []
        lenlist = []
        longestword = ''
        strt = 0
        for i in range(len(self.strng)):
            if self.strng[i] == ' ':
                wordlst.append(self.strng[strt:i])
                strt = i + 1
            elif i == len(self.strng) - 1:
                wordlst.append(self.strng[strt:i + 1])

        for i in range(len(wordlst)):
            lenlist.append(len(wordlst[i]))

        newlen = sorted(lenlist)

        for i in range(len(lenlist)):
            if newlen[len(newlen) - 1] == lenlist[i]:
                longestword = wordlst[i]

        return longestword

################################### FREQUENCY CHECK ####################################################

    def freqchk(self):
        cnt = 0
        for i in range(len(self.strng)):
            if self.strng[i:i + len(self.substrng)] == self.substrng:
                cnt += 1
        return cnt

################################### PALINDROME CHECK ####################################################

    def chkpali(self):
        mainstr = []

        for i in range(len(self.strng)):
            mainstr.append(self.strng[i])

        revstr = mainstr.copy()
        revstr.reverse()

        if mainstr == revstr:
            print("It is a palindrome")
        else:
            print("It is not a palindrome")

################################# FIRST OCCURANCE ########################################################
        
    def fstsub(self):
        for i in range(len(self.strng)):
            if self.strng[i] == self.substrng[0]:
                for j in range(len(self.substrng)):
                    if self.substrng == self.strng[i:i + len(self.substrng)]:
                        return i

################################ WORD COUNT #############################################################

    def ctword(self):
        countlst = []
        wrd = 1
        ctlst = sorted(wordlst)
        ctlst1 = sorted(list(set(wordlst)))
        for j in range(len(ctlst1)):
            for i in range(len(wordlst)):
                if ctlst1[j] == ctlst[i]:
                    wrd += 1
            countlst.append(wrd - 1)
            wrd = 1
        # print(ctlst1)
        # print(countlst)
        for i in range(len(ctlst1)):
            print(ctlst1[i] + ' = ' + str(countlst[i]))

############################### MENU ####################################################################            
    
    def menu(self):
        i = 1
        while i >0:
            print("MENU")
            print("Press 1 to print longest word in the string")
            print("Press 2 to print the frequency of occurance of the substring")
            print("Press 3 to print if the string is a palindrome or not")
            print("Press 4 to print the index of the first occurance of substring")
            print("Press 5 to print the number of times each word has occured")
            print("Press 6 to exit")
            oprn = int(input("Enter the serial number of the operation you want to perform:"))
            
            if oprn == 1:
                print(self.lngword())
            elif oprn == 2:
                print(self.freqchk())
            elif oprn == 3:
                self.chkpali()
            elif oprn == 4:
                print(self.fstsub())
            elif oprn == 5:
                self.ctword()
            elif oprn == 6:
                break
            
############################### STRING INPUT ###########################################################

stringA = input("Enter a string:")
stringB = input("Enter a substring:")

############################### FUNCTION CALLING #######################################################

a = Operations(stringA, stringB)
a.menu()

########################################################################################################




