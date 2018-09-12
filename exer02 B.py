'''
autor : Geovanna Alves Magalhães
data : 17/05/18
'''

nota1 = float(input('Digite sua primeira nota'))
nota2 = float(input('Digite sua segunda nota'))

nota_total = nota1+nota2
print('Sua nota total é ' , nota_total)
media = nota_total / 2
print ('Sua média é ' , media)

if media >= 9.0 and media <= 10.0 :
    print('Você tirou A . VOCÊ FOI APROVADO ! ')
elif media >= 7.5 and media <=9.0 :
    print('Você tirou B . VOCÊ FOI APROVADO !' )
elif media >=6.0 and media <= 7.5 :
    print ('Você tirou C . VOCÊ FOI APROVADO ! ')
elif media >=4.0 and media <=6.0 :
    print ('Você tirou D . VOCÊ FOI REPROVADO :(')
elif media <= 4.0 :
    print ('Você tirou E . VOCÊ FOI REPROVADO :( ' )
 


