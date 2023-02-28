class car:
def _init_(self,model,make,year_of_man,engine_capacity):
        self.model = model
        self.make = make
        self.year = year_of_man
        self.engine_capacity = engine_capacity
    
        


#getters
def get_model(self):
    return self.model


def get_make(self):
     return self.make



def get_year(self):
    return self.year_of_man


car1 = ("demio","nissan",2008,2300)
car2 = ("hillux","toyota",2005,2500)
car3 = ("camri","toyota",2018,2000)


print(car1.get_model())
print(car1.get_year_of_man())


print(car2.get_model())
print(car2.get_year_of_man())