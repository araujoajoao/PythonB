n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma vale:', s)
print('A soma entre', n1 ,'e' , n2 , 'vale:', s)
print('A soma entre {} e {} vale: {}' .format(n1 , n2 , s))

n = input('Digite um valor')
print(type(n))
print(n.isalnum)
print(n.isalpha)
print(n.isdecimal)
print(n.isnumeric)