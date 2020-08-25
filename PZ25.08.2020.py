 
class Empoloyer(Departament):
    def __init__ (self, first_name, second_name, age, sallary, job, bonus):
        
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.sallary = sallary
        self.job = job
        self.bonus = 0
        
    def __prn__(self):
        return f'Employer',{self.first_name}, {self.second_name}


class Departament:
    def __init__ (self, name):
        self.name = name
        self.employers[]
    
    def add_employer(self, employer):
        self.employers.append(employer)



def vvid():
    emloyer1 = Employer(
        first_name = "John",
        second_name ="Smith",
        age = 34
        sallary = 1000
        job = "Engineer"

    )

    emloyer2 = Employer(
        first_name = "Edward",
        second_name ="Norton",
        age = 29
        sallary = 1500
        job = "Manager"
        
    )
    departament = Departament(name = "New")
    departament.add_employer(empoloyer1)
    departament.add_employer(empoloyer2)

    for i in departament:
        print (i)


vvid()
# Я ще роблю, тут помилка, я просто кидаю перший варіант :)