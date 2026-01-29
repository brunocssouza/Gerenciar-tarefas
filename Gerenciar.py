import os
tarefas = []

def nome_programa():
     print('𝒈𝒆𝒓𝒆𝒏𝒄𝒊𝒂𝒏𝒅𝒐 𝒖𝒎𝒂 𝒍𝒊𝒔𝒕𝒂')

def main():
    os.system('cls')
    nome_programa()
    exibir_opcao()
    escolher_opcao()

def exibir_opcao():
     print("=================================")
        print("\n1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
print("=================================")

def limpar(texto):
        os.system('cls')
        print(texto)
        print()

def Adicionar_tarefa():
    limpar('Adicionando uma tarefa! ')

    while True:
        tarefa = input('Digite uma tarefa: ').strip()

        if not tarefa:                          
            print('Sem Resposta! \n')           # Caso não coloque nada, mostra as opções menu ou continuar 

            while True:  
                opcao = input('Digite MENU para voltar ao menu principal ou CONTINUAR para prosseguir: ').strip().lower()

                if opcao in ['menu']:
                    voltar_ao_menu_principal()
                    return 
                elif opcao in ['continuar']:
                    Adicionar_tarefa()
                    return
                else:                               # Caso não coloque nada, mostra as opções menu ou continuar 
                    print("Opção inválida. Digite 'menu' ou 'continuar'.")
                break
            
        tarefas.append(tarefa)
        print('Tarefa adicionada com sucesso!\n ')

        while True:
            continuar = input('Deseja adicionar mais itens à lista? (Sim ou Não): ').strip().lower()

            if not continuar:
                print('Sem Resposta! \n')
                continue
                    
            elif continuar in ['sim','s']:
                Adicionar_tarefa()
                return 
            elif continuar in ['não','nao','n']:
                voltar_ao_menu_principal()
                return
            else:
                print('Resposta inválida. Digite Sim ou Não.')
            break

def Visualizar_tarefas():
    limpar('Visualizando Tarefas!')
    if tarefas:
        print("\nTarefas:")
        for i ,tarefa in enumerate(tarefas, 1):
            print(f"{i}.{tarefas}")
    else:
        print("Nenhuma tarefa cadastrada.")

    voltar_ao_menu_principal()

def Remover_tarefa():
        limpar('Removendo Tarefas')
        if not tarefas:
                print("Erro: Nenhuma tarefa para remover.")
                return
 
        try:
            print(f'{tarefas}')
            indice = int(input("Digite o número da tarefa a ser removida: ")) - 1

            if 0 <= indice < len(tarefas):
                removida = tarefas.pop(indice)
                print(f"Tarefa '{removida}' removida!")
            else:
                print("Erro: Índice inválido! Digite um número válido.")
        except ValueError:
            print("Erro: Entrada inválida! Digite um número.")

        voltar_ao_menu_principal()            

def Sair():  
    limpar('Saindo...')

def opcao_invalida():
    print('Opção Invalida!')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nPressione qualquer tecla, para voltar ao menu principal!')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha a opção: '))

        if opcao_escolhida == 1:
            Adicionar_tarefa()
        elif opcao_escolhida == 2:
            Visualizar_tarefas()
        elif opcao_escolhida == 3:
            Remover_tarefa()
        elif opcao_escolhida == 4:
            Sair()
    except:
        opcao_invalida()


if __name__ == '__main__':
    main()




'''             CONTEXTO
        O desafio é criar um programa que permita ao usuário gerenciar tarefas adicionando, visualizando e removendo itens de uma lista. 
        Para isso, o programa precisa exibir um menu interativo e aceitar diferentes entradas do usuário,
        e tratar essas entradas para evitar erros inesperados.
'''
'''             COMENTÁRIOS
        "pop", é um método usado para remover e retornar um elemento de uma estrutura de dados.
        "enumerate", uma função usada para percorrer uma sequência (lista, tupla, string, etc.)

'''



