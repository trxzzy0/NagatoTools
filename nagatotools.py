import os 
import time

## Informacoes 

versao = 'Vers�o 1.0.3'
versao_python = '3.8'
maker = 'NagatoX'
contato = 'https://wa.me/5583996529700'

print('')
print('')
print('Version: ' + versao)
print('Vers�o do python utilizada: ' + versao_python)
print('')
print('=============================')
print('=============================')
print('')
print('Codded by: ' + maker)
print('Contato: ' + contato)
print('')
login = input('Senha: ' )
password = 'ultra123'

## Variaveis gerais
codigo_verificador = 'DNLQDIWcnwhfiWDMHIQWCNqc'
clear_terminal = os.system("cls")

def login_verification():
  if login == password:
     print('')
     print('Senha correta.')
     primeiro_menu()

  elif login != password:
    print('Senha incorreta.')
    return 

     
def primeiro_menu():
  print('')
  print("Ol�, voc� conseguiu acessar o primeiro menu.")
  print('')
  print('1: Verifica��o')
  print('')
  print('Obs: precisamos verificar antes de conceder acesso a nosso menu.')
  print('')

  # Escolher a op��o

  escolher_opcao = int(input('Pressione "1" para fazer a verifica��o: '))

  if escolher_opcao == 1:
    os.system("clear")
    concluir_verificacao()

  senha_verificacao = input('Digite o c�digo ou pressione 1 para voltar: ')
  
  if senha_verificacao == codigo_verificador:
    os.system("clear")
    menu_principal()
  elif senha_verificacao == '1':
    os.system("clear")
    primeiro_menu()
          
def concluir_verificacao():
  print('')
  print('Para fazer a verifica��o, envie um "up" com a print para este n�mero: wa.me/5583996529700. ap�s isso, apenas aguarde, iremos enviar a senha para o acesso total ao menu.')

  
def menu_principal():
  print('Parab�ns! fique com nosso menu.')
  print('')
  print('- Escolha o que deseja de acordo com a numera��o!')
  print('')
  print('1: Desativar n�mero')
  print('2: Linux tools')
  print('3: Derrubar IP')
  print('4: Gerador de contas')
  print('5: Packs pagos e recentes')
  print('')

  escolha_menu_principal = int(input('- Escolha: '))

  if escolha_menu_principal == 1:
    desativar_numero()


def desativar_numero():
  os.system("clear")
  print('===========================================================')
  print("""
    - Assunto do email:
      Perdido/Roubado: Por favor, desativem mimha conta

- Texto:

- Ola, tive meu aparelho perdido recentemente e preciso que meu numero 
echo do whatsapp seja desativado ate eu comprar um outro chip!! o meu numero e: (numero)

===========================================================
""")

os.system("clear")
login_verification()

