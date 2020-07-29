
def distance_from_zero(f):
    if type(f)==int or type(f)==float:
        return(abs(f))
    else:
        return "No"

f="ggg"
print('res= ', distance_from_zero(f))

# input дає тільки текст, тому ввід зробила саме так, не знаю як зробити по іншому, щоб можна було б вводити з клавіатури значення