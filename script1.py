"""def data_fio(name, surname):
    return f"{surname.upper()} {name.lower()}"

print(data_fio('ali', 'aliev'))"""

#\
def plus(*args):
    return sum(args)


print(plus(1, 2, 3, 4, 5))
print(plus(91, 62, 23, 84, 15))

def func(**kwargs):
    return kwargs

print(func(a=12, b=764, c=234, d=543))

