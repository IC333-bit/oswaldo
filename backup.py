import os

def exc():
    print('Excluiu uma pasta')


def create():
    print('Criou uma pasta')
    nome = input('Digite o nome da pasta: ')
    if os.path.exists(nome):
        print(f'A pasta {nome} já existe')
    else:
        os.mkdir(nome)
        print(f'A pasta {nome} f65 criada')


def atua():
    print('atualizou uma pasta')


op = str(input('Deseja iniciar (S/N): '))
if op == 'S':
  while True:
      opcao = str(input('Digite uma dessas opções: excluir, criar ou atualizar: '))

      if op == 'S':
          if opcao == 'excluir':
             exc()
          elif opcao == 'criar':
              create()
          elif opcao == 'atualizar':
              atua()
          else:
              print('Voe digitou errado, ou então colocou ')
      else:
          break
else:
  print('Ok muito obrigado')
