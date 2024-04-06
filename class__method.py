class person:
    name = "annonymus"
    def changeName(self,name):
        self.__class__.name = "rahul"
    
    @classmethod
    def changeName(cls,name):
        cls.name = "rah"