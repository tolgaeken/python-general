class Person:
    def __init__(self,name,year):
        if len(name) >10:
            raise Exception("Name alanı 10 karakterden fazla içeriyor")
        else:
            self.name = name

pr = Person("Aliiiiiiiiiiiiiiiiii",1990)