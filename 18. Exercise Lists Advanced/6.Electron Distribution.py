num_of_electrons = int(input())
list_electrons = []
while num_of_electrons > 0:
    n = len(list_electrons) + 1
    shell = min(2*(n**2), num_of_electrons)
    list_electrons.append(shell)
    num_of_electrons -= shell

print(list_electrons)