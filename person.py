class Person:
    def __init__(self,name):
        self.name=name
        
    def legally_change_name(self,new_name):
        self.name=new_name
        
    def introduce_myself(self):
        print("My name is {} ".format(self.name))
    
    
    

p1= Person("Chenna")

p1.legally_change_name("Chenna Panthagani")

p1.introduce_myself()

p2= Person("Kesava")

p2.legally_change_name("Kesava Rao")

p2.introduce_myself()