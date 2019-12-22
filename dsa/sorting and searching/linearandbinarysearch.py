

class fsval:

    
    def __init__(self,iarray):
        self.iarray =list(map(int,iarray.split()))

        

    def linear(self, value): #any array

        for i in range(len(self.iarray)):
            if self.iarray[i] == value:
                print(value,"found at: ",i+1)
            elif self.iarray[i] != value and i == len(self.iarray)-1:
                print("not found")


    def binary(self,item): #only sorted array
        f = 0
        l = len(self.iarray)-1
        found = False
        while( f <= l and not found):
            m = (f + l)//2
            if self.iarray[m] == item :
                    found = True
            else:
                if item < self.iarray[m]:
                    l = m - 1
                else:
                    f = m + 1	
        if found == True:
            return print("found at: ",m+1)
        else:
            return print("not found")
        


ary = fsval("1 2 3 9 15 24 35")
ary.linear(35)
ary.binary(9)
