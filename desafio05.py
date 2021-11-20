#1
n = int(input('Digite un número: '))
a = n - 1
s = n + 1
print('Analisandon o valor {}, o seu antecessor é {}, e seu sucessor é {}'.format(n , a, s))
print('Analisandon o valor {}, o seu antecessor é {}, e seu sucessor é {}'.format(n , (n-1), (n+1)))
#2
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}'.format(n , d))
print('O triplo de {} é igual a {} \nA raiz quadrada de {} é igual a {}'.format(n , t , n , r))
#3
n1 = float(input('Digite primeira nota: '))
n2 = float(input('Digite segunda nota: '))
media = (n1 + n2) / 2
print('A média entre {} e {} é igual a {}'.format(n1 , n2, media))
#4
medida = float(input('Distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}cm e {}mm'.format(medida , cm , mm) )
#5
n = int(input('Digite um número da sua tabuada: '))
print('-' * 14)
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
print('-' * 14)
#6
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
#7
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
print('Sua parede tem dimenão de {}x{} e sua área é {}m².'.format(l, a, area))
t = area / 2
print('Você precisará de {} litros de tinta'.format(t))
#8
p = float(input('Qual o preço do produto? R$'))
d = p - (p * 5 / 100)
print('O produto que custa R${:.2f}, na promoção custará R${:.2f}'.format(p, d))
#9
s = float(input('Qual o salário do funcionário? R$'))
a = s + (s * 15 / 100)
print('O funcionário que ganhava R${:.2f} com 15% de aumento, ganhará R${:.2f}'.format(s, a))
