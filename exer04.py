'''
autor : Geovanna Alves Magalhães
data : 16/05/18
'''
n1 = int(input('Digite um numero '))
n2 = int(input('Digite outro numero '))
n3 = int(input('Digite mais um numero '))

maior = n1
if (n2 > maior ) :
    maior = n2
if (n3 > maior) :
    maior = n3
    print('O maior numero é ' , maior )
