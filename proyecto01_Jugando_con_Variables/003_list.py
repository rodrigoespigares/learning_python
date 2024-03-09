lista=[[1,2,3],['a','b','c']]


lista.append({1:'a',2:'b'})
print("---- append ----")
print(lista)

lista.insert(1,"pan")
print("---- insert ----")
print(lista)

lista.remove("pan")
print("---- remove ----")
print(lista)

index = lista.index(['a','b','c'])
print("---- index ----")
print(index)
print("---- len ----")
print(len(lista))
print("---- count ----")
lista.append(3)
lista.append(3)
lista.append(3)
lista.append(3)
print(lista.count(3))

print("---- normal - reverse ----")
print(lista[0])

listaRev = lista[0]
print(listaRev[::-1])

print("---- FOR ----")
for element in lista:
    print(element)