class baap:
    __money = ""
    
    def amethod(self):
        self.any=__money

class beta(baap):
    def baapkacash(self):
        # print(self.__money) #error 
        print(self._beta__money)

obj=beta()
obj.baapkacash()

