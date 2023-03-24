vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    print('Multado! Você excedeu o limite permitide que é de {}km/h'.format(vel))
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de R$  {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')    
print('----------Fim----------')