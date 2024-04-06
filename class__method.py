class person:
    name = "anonymous"
    def changeName(self,name):
        self.__class__.name = "raoul"   #method 01 
    
    @classmethod
    def changeName(cls,name):
        cls.name = "rah"                #method 02