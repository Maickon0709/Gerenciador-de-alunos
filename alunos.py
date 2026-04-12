from banco import conectar

def cadastrar_aluno():
    conexao, cursor = conectar()

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    plano = input("Plano: ")

    cursor.execute(
        "INSERT INTO alunos (nome, idade, plano) VALUES (?, ?, ?)",
        (nome, idade, plano)
    )

    conexao.commit()
    conexao.close()
    print("Aluno cadastrado!")


def listar_alunos():
    conexao, cursor = conectar()

    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    print("\n--- LISTA DE ALUNOS ---")
    for aluno in alunos:
        print(f"ID: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Idade: {aluno[2]}")
        print(f"Plano: {aluno[3]}")
        print("-" * 20)

    conexao.close()


def buscar_aluno():
    conexao, cursor = conectar()

    nome = input("Digite o nome do aluno: ")
    cursor.execute(
        "SELECT * FROM alunos WHERE nome = ?",
        (nome,)
    )
    alunos = cursor.fetchall()

    if alunos:
        for aluno in alunos:
            id, nome, idade, plano = aluno
            print(f"\nID: {id}")
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"Plano: {plano}")
    else:
        print("Aluno não encontrado")

    conexao.close()


def deletar_aluno():
    conexao, cursor = conectar()

    listar_alunos()
    id_aluno = int(input("Digite o ID do aluno: "))

    cursor.execute(
        "DELETE FROM alunos WHERE id = ?",
        (id_aluno,)
    )

    conexao.commit()
    conexao.close()
    print("Aluno removido com sucesso")