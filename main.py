from alunos import cadastrar_aluno, listar_alunos, deletar_aluno, buscar_aluno, atualizar_cadastro

while True:
    print("\n--- ACADEMIA ---")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Atualizar Cadastro")
    print("5 - Remover aluno")
    print("6 - Sair do programa")

    op = input("Escolha: ")

    if op == "1":
        cadastrar_aluno()

    elif op == "2":
        listar_alunos()

    elif op == "3":
        buscar_aluno()

    elif op == "4":
        atualizar_cadastro()

    elif op == "5":
        deletar_aluno()

    elif op == "6":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")