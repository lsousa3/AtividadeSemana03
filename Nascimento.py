from datetime import date

sexo = str(input('Digite [M] para sexo Masculino\nDigite [F] para sexo Feminino '))

sexo = sexo.upper()

if sexo == 'F':
    print('Você não precisa se alistar Mocinha! ')

else:
    ano_nasc = int(input('Digite o seu ano de nascimento: '))

    ano_atual = date.today().year
    ano_alistamento = ano_atual - ano_nasc  # se alista com 18 anos
    tempo_passou = 18 - ano_alistamento

    print(f'Voce tem {ano_alistamento} anos SOLDADO !')

    if ano_alistamento < 18: #verifica se o soldado ainda n fez 18 anos e calcula quantos anos falta para o alistamento
        print('Você ainda esta novo para se alistar SOLDADO ! ')
        print(f'Ainda falta {tempo_passou} anos, fique tranquilo SOLDADO ! ')

    elif ano_alistamento == 18:  #verifica se o soldado tem 18 anos, se tiver precisa se alistar
        print('Está na hora do seu Alistamento SOLDADO !')

    else: #verifica se o soldado tem mais de 18 anos,se sim ele precisa se alistar e calcula quanto tempo passou do alistamento
        print('Jã passou da hora de você se alistar SOLDADO !')


        print('Você deveria ter se alistado a {} anos, vá ao posto de alistamento mais proximo !'.format(tempo_passou))