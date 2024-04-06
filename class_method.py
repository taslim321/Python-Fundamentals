class student:
    def __init__(self,name,marks):
        self.name= name
        self.marks = marks

    def get_avg(self):
        sum=0
        for val in marks:
            sum+=val
        print("hi",self.name,"your avg score is:",sum/3)

s1=student("Taslim",[99,97,95]) 
s1.get_avg()