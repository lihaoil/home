# def f(s,z):
#     return s+z
#
# list_1 = ('lll', 'lKK', 'wXy')
# list_2 = ['asd','sdf','dfg']
#
# print(map(f, list_1, list_2))
# print(list(map(f, list_1, list_2)))

def f(a):
    return a**2

abc = [1,2,3]
my_list = []
for cba in abc:
    my_list.append(f(cba))
print(my_list)
