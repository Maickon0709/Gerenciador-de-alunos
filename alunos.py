from banco import conectar

def cadastrar_aluno():
    conexao, cursor = conectar()

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = input("CPf: ")

    cursor.execute(
        "INSERT INTO alunos (nome, idade, cpf) VALUES (%s, %s, %s)",
        (nome, idade, cpf)
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
        print(f"cpf: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Idade: {aluno[2]}")
        print("-" * 20)

    conexao.close()


def buscar_aluno():
    conexao, cursor = conectar()

    id_aluno = input("Digite o cpf do aluno: ")
    cursor.execute(
        "SELECT * FROM alunos WHERE cpf = %s",
        (id_aluno,)
    )
    alunos = cursor.fetchall()

    if alunos:
        for aluno in alunos:
            cpf, nome, idade, plano = aluno
            print(f"\nCPF: {cpf}")
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
    else:
        print("Aluno não encontrado")

    conexao.close()

def atualizar_cadastro():
    conexao, cursor = conectar()

    listar_alunos()
    cpf_aluno = int(input("Digite o cpf do aluno:"))
    novo_nome = input("Nome novo: ")
    nova_idade = int(input("Idade nova: "))

    cursor.execute(
        """
        UPDATE alunos
        SET NOME = %s, idade = %s WHERE cpf = %s
        """,
        (novo_nome, nova_idade, cpf_aluno)
    )

    conexao.commit()
    conexao.close()

    print("Cadastro atualizado com sucesso! ")


def deletar_aluno():
    conexao, cursor = conectar()

    listar_alunos()
    cpf_aluno = int(input("Digite o cpf do aluno: "))

    cursor.execute(
        "DELETE FROM alunos WHERE cpf = %s",
        (cpf_aluno,)
    )

    conexao.commit()
    conexao.close()
    print("Aluno removido com sucesso")