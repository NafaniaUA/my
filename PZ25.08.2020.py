MAX_BONUS = 500
class Employer:
    def __init__ (self, first_name, second_name, age, sallary, job, bonus=0):

        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.sallary = sallary
        self.job = job
        self.bonus = bonus

    def __repr__(self):
        return f'Employer({self.first_name, self.second_name})'
    
    @property
    def total_sallary(self):
        return self.bonus + self.sallary
    
    def add_bonus (self, bonus):
        if bonus > MAX_BONUS:
            print("Ви перевищили максимальний бонус")
        else:
            self.bonus+=bonus



class Departament:
    def __init__ (self, name, emploers = []):
        self.name = name
        self.employers = emploers
    
    def __iter__(self):
        return (e for e in self.employers)

    def add_employer(self, employer):
        self.employers.append(employer)



def vvid():
    employer1 = Employer(
        first_name = "John",
        second_name ="Smith",
        age = 34,
        sallary = 1000,
        job = "Engineer",
        #bonus=0

    )

    employer2 = Employer(
        first_name = "Edward",
        second_name ="Norton",
        age = 29,
        sallary = 1500,
        job = "Manager",
        #bonus=0

    )
    departament = Departament(name = "New")
    employer1.add_bonus(6000)
    departament.add_employer(employer1)
    departament.add_employer(employer2)

    print(departament.name)
    for e in departament:
        print(e,'sallary ', e.total_sallary)

    


vvid()

