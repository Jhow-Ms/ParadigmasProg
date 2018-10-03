class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

def cadastro_da_contatos():
        menu = "1 - Cadastrar\n2 - Listar\n0 - Sair\n"
        op = input(input(menu))
        while op != 0:
            if op == 1:
                try:
                    f = open("agenda.txt", "a")
                    nome = input("Digite o nome")
                    numero = input("Digite o numero")
                    f.write(nome + ";" + numero + "\n")
                    f.close()
                except IOError:
                   pass
                finally:
                  print("Realmente passou por aqui")
            elif op == 2:
                try:
                    with open("agenda.txt","r") as outro_f:
                        linhas = outro_f.readLines()
                        print(linhas)
                except IOError:
                    pass
                finally:
                    print("Finally passando")
            else:
                print("Tchau")
            op = int(input(menu))

cadastro_de_contatos()