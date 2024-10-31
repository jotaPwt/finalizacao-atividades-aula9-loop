# ATIVIDADE 1

# Crie um sistema de banco, com as seguintes operações:

# ** Utilize While ou loop **

# # SISTEMA De banco

# - Acesso a conta

lista_acesso = []

cad_acesso = input('Cadastere seu acesso no banco: ')
print('Cadatro concluido')

lista_acesso.append(cad_acesso)

for i in range(1, 4):
    acesso = input('Digite seu acesso: ')
    if acesso == cad_acesso:
        print('Bem vindo a sua conta')  
        saldo = 1000
        print(f'Seu extrato atual é {saldo}')
    # - Fazer um deposito
        print('======================')
        print('Qual ação voce gostaria de realizar:')

        print('''
        id 0 = fazer um saque: 
        id 1 = fazer um depósito
        ''')

        acao = int(input('Digite o ID da ação desejada: '))

        if acao == 0:
            saque = int(input('insira o valor que voce gostaria sacar >>'))
            if saque > saldo:
                print('Voce nao tem todo esse dinheiro')
                pass
            elif saque <= saldo:
                print('Saque concluido')
                break
            elif saque == 0:
                print('nao é possivel sacar 0 reais')
            else:
                print('Ação indisponivel')

        elif acao == 1:
            dep = int(input('insira o valor que voce gostaria de depositar >>'))
            print('Depósito concluido com sucesso')
            
            break
        
        

    else:
        print(f'esse não é seu acesso. você tem {i} chances')
        if i > 2:
            print('Acesso Bloqueado')


print('''
    id 0 - sim
    id 1 - nao
''')

sair = input('Você gostaria de sair do sistema?')


if sair == 0:
    print('Saiu')
else:
    pass
# - Ver extrato
    
        
# - Fazer um saque 
# - Sair do sistema 

# ...........................................................

# ATIVIDADE 2

# CRIE A TABUADA COM O LOOP WHILE
# ESCOLHA UM NÚMERO E FAÇA O CALCULO DA MULTIPLICAÇÃO COM 
# TODOS OS NÚMEROS


n = int(input('Digite o numero da sua tabuda, COM FOR'))

for i in range(1,11):
    res = n * i
    print(f'{n} X {i} = {res}')


n = int(input('Digite o numero da sua tabuda, COM WHILE'))

tab = range(1,11)
contador = 0

while contador < 10:
    contador = contador + 1
    resultado = n * contador
    print(f'{n} X {contador} = {resultado}')
    