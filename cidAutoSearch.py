# main.py
import prontuario

def main():
    print("Bem-vindo ao sistema de prontuário eletrônico.")
    nome_paciente = input("Digite o nome do paciente: ")

    # Escolha se quer buscar por código ou nome
    opcao_busca = input("Você quer buscar por [1] Código ou [2] Nome da doença? ")

    if opcao_busca == '1':
        codigo_doenca = input("Digite o código CID da doença: ")
        nome_doenca = prontuario.buscar_doenca_por_codigo(codigo_doenca)
        if nome_doenca == "Código não encontrado.":
            print("Código não encontrado.")
            return
    elif opcao_busca == '2':
        nome_doenca = input("Digite o nome da doença: ")
        codigo_doenca = prontuario.buscar_doenca_por_nome(nome_doenca)
        if codigo_doenca == "Doença não encontrada.":
            print("Doença não encontrada.")
            return
    else:
        print("Opção inválida.")
        return

    # Salvar o prontuário e exibir o nome do arquivo
    arquivo_json = prontuario.salvar_prontuario(nome_paciente, codigo_doenca, nome_doenca)
    print(f"Prontuário salvo no arquivo: {arquivo_json}")

if __name__ == "__main__":
    main()
