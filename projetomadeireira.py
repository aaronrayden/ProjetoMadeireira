# FUNÇÕES:

# função que retorna o valor do frete:
def transporte():
  print('\nAgora escolha qual o meio de transporte para o frete do seu pedido:')
  print('1 - Rodoviário: + R$1000,00')
  print('2 - Ferroviário: + R$2000,00')
  print('3 - Hidroviário: + R$2500,00')
  while True:
    try:
        escolha = int(input('Digite a opção do frete (1/2/3): '))
        if escolha == 1:
            return 1000
        elif escolha == 2:
            return 2000
        elif escolha == 3:
            return 2500
    except ValueError:
        print('Opção não disponível. Tente novamente.')
        continue
    else:
        print('Opção não disponível. Tente novamente.')
        continue

    # função que retorna o valor da quantidade de toras em m³ e o valor do desconto:


def qtd_toras():
    print('\nEstes são os descontos especiais da nossa unidade:')
    print('4% - A partir de 100m³.\n9% - A partir de 500m³.\n16% - A partir de 1000m³.')
    print('Obs.: NÃO aceitamos pedidos acima de 2000m³.')
    while True:
        try:
            escolha = int(input('Digite a quantidade desejada (em metros³): '))
            desconto = 0
            if escolha < 100:
                print('Desconto não aplicado para este valor...')
                return escolha, 0
            elif 100 <= escolha < 500:
                print(f'Desconto de 4% aplicado!')
                desconto += (4 / 100)
                return escolha, desconto
            elif 500 <= escolha < 1000:
                print(f'Desconto de 9% aplicado!')
                desconto += (9 / 100)
                return escolha, desconto
            elif 1000 <= escolha <= 2000:
                print(f'Desconto de 16% aplicado!')
                desconto += (16 / 100)
                return escolha, desconto
            elif escolha > 2000:
                print('Não aceitamos pedidos com esta quantidade de toras. Por favor digite novamente.')
                continue
        except ValueError:
            print('Por favor, digite uma opção válida.')
            continue
        else:
            print('Por favor, digite uma opção válida.')
            continue

        # função que retorna o valor por m³ do tipo de tora escolhida:


def escolha_tipo():
    print('Estes são os tipos de madeira disponíveis em estoque e seus respectivos valores:')
    print('Tora de Pinho (PIN): R$150,40/m³\nTora de Peroba (PER): R$170,20/m³')
    print('Tora de Mogno (MOG): R$190,90/m³\nTora de Ipê (IPE): R$210,10/m³\nTora de Imbuia (IMB): R$220,70/m³')
    while True:
        try:
            escolha = input('\nDigite a sigla correspondente ao tipo de madeira desejado: ')
            if escolha.lower() == 'pin':
                x = 150.40
                return x

            elif escolha.lower() == 'per':
                x = 170.20
                return x

            elif escolha.lower() == 'mog':
                x = 190.90
                return x

            elif escolha.lower() == 'ipe':
                x = 210.10
                return x

            elif escolha.lower() == 'imb':
                x = 220.70
                return x

        except ValueError:
            print('Sigla não compreendida. Por favor, digite novamente.')
            continue
        else:
            print('Sigla não compreendida. Por favor, digite novamente.')
            continue

        # PROGRAMA PRINCIPAL:


print('\nBem vindo! Apresento-lhe o seguinte programa desenvolvido por:')
print('Glauber Diego da Silva Fidelix dos Santos.\n')

print('Bem vindo à Madeireira Fidelix!\n')

choice = escolha_tipo()

woods = qtd_toras()

transport = transporte()

print('\nCalculando o valor total...\n')

# calcula o valor final com desconto(se tiver) e soma o valor do frete:
total = (choice * woods[0]) - ((choice * woods[0]) * woods[1]) + transport

print(f'O total do pedido é de R${total}, sendo R${choice * woods[0]} o valor bruto,')
print(f'R$ {(choice * woods[0]) * woods[1]} o total descontado, e um acréscimo de R$ {transport} de frete.')