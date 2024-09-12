import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, Nosso plano diamante possui:{os.linesep}'
              f'DJ por 5 horas{os.linesep}'
              f'Sonorização Completa{os.linesep}'
              f'Iluminação completa{os.linesep}'
              f'Pista de dança{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, Nosso plano diamante possui:{os.linesep}'
              f'DJ por 5 horas{os.linesep}'
              f'Sonorização Completa{os.linesep}'
              f'Iluminação completa{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, Nosso plano diamante possui:{os.linesep}'
              f'DJ por 5 horas{os.linesep}'
              f'Sonorização Completa{os.linesep}'
              f'Iluminação simples{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, Nosso plano diamante possui:{os.linesep}'
              f'DJ por 5 horas{os.linesep}'
              f'Sonorização Completa{os.linesep}')
    elif resposta == '0':
        print(f'{nome} muito obrigado por usar o chat Blackout. Até logo!')
        exit()#Essa linha encerra o programa
    else:
        print("Escolha apenas 0,1,2,3 ou 4")


def start():
    # Apresentar o chatbot
    print('Ola! Seja muito bem-vindo ao chat blackout!')
    # Pedir o nome
    nome = input('Digite o seu nome: ')
    # Pedir o email
    #email = input('Digite o seu email: ')
    while True:
        # Oferecer o menu de opções
        resposta = input(
            f'{nome} qual plano você gostaria de saber mais sobre?{os.linesep}'
            f'[1] - Plano Diamante {os.linesep}'
            f'[2] - Plano Ouro {os.linesep}'
            f'[3] - Plano Prata {os.linesep}'
            f'[4] - Plano Bronze{os.linesep}'
            f'[0] - Para encerrar o chat{os.linesep}'
            f'Digite a opção:{os.linesep}')

        # Processar a resposta enviada
        processar_resposta(resposta, nome)

        # Aguardar que o usuário pressione Enter antes de continuar
        input("Pressione Enter para retornar ao menu...")
        # Limpar a tela
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    start()
