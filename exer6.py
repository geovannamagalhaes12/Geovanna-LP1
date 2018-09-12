'''
autor : Geovanna Alves Mgalhães
data : 16/05/18
'''

metros = int(input('Qual o tamaho em m² da area que sera pintada?'))
litros = metros / 3
preco_l = 80.0
capacidade_l = 18
latas = int(litros / capacidade_l )
total = latas * preco_l
print ('Você usará ' , latas , 'latas de tinta')
print (' O preço total a ser pago é de R$ : ' , total)
