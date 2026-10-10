todo = []
doing = []
done = []

def mostrar_tarefas():
    print("\n--- TO DO ---")
    for i, t in enumerate(todo, start=1):
        print(f"{i}. {t}")

    print("\n--- DOING ---")
    for i, t in enumerate(doing, start=1):
        print(f"{i}. {t}")

    print("\n--- DONE ---")
    for i, t in enumerate(done, start=1):
        print(f"{i}. {t}")
    print()

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    print("""
1 - To do
2 - Doing
3 - Done
""")
    lista = int(input("Em qual lista? "))
    if lista == 1:
        todo.append(tarefa)
    elif lista == 2:
        doing.append(tarefa)
    elif lista == 3:
        done.append(tarefa)
    else:
        print("Lista inválida!")

while True:
    print("""
==================== LISTA DE TAREFAS ====================
O que você quer fazer?
1 - Adicionar tarefa
2 - Visualizar tarefas
3 - Limpar todas as tarefas
4 - Sair
""")
    escolha = int(input())

    if escolha not in (1, 2, 3, 4):
        print("Valor inválido!")
        continue

    match escolha:
        case 1:
            adicionar_tarefa()
        case 2:
            mostrar_tarefas()
        case 3:
            todo.clear()
            doing.clear()
            done.clear()
            print("Tarefas limpas!")
        case 4:
            print("Encerrando programa")
            break