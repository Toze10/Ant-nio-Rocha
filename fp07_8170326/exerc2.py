file = open ("valores.txt", "r")

lista = []
    
linhas = file.readlines()


def sort(my_list):
    if len(my_list) > 1:
        mid = int(len(my_list)/2)
        left = my_list[:mid]
        right = my_list[mid:]
        # Split
        sort(left)
        sort(right)
        # sort
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1
        # left leftovers
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1
        # right leftovers
        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1


for i in linhas:
    i = int(i.split("\n")[0])
    lista.append(i)



sort(lista)
print(lista)

#print (lista[::-1])

for i in range(len(lista)-1, -1, -1):
   print(lista[i], end= " ")