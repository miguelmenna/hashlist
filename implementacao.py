# Registro HashLista
class HashLista:
    def __init__(self, chave, prox):
        self.chave = chave
        self.prox = prox

# Algoritmo HashMenuLista
def HashMenuLista(tabela):
    op, pos, num, i = 0, 0, 0, 0
    for i in range(len(tabela)):
        tabela[i] = None
    print("Escolha o que deseja fazer:")
    print("1 - Inserir")
    print("2 - Remover")
    op = int(input())

    # Escolhe o que deseja fazer
    while op != 0:
        if op == 1:
            print("Insira o número a ser inserido:")
            num = int(input())
            pos = FuncaoHashing(num)
            InserirNaHash(tabela, pos, num)
        elif op == 2:
            print("Insira o número a ser removido:")
            num = int(input())
            pos = FuncaoHashing(num)
            tabela[pos] = tabela[pos].prox

# Função FuncaoHashing
def FuncaoHashing(num):
    return num % len(tabela)

# Função InserirNaHash
def InserirNaHash(tabela, pos, num):
    no = HashLista(num, None)
    if tabela[pos] is None:
        tabela[pos] = no
    else:
        aux = tabela[pos]
        while aux.prox is not None:
            aux = aux.prox
        aux.prox = no

# Função RemoverDaHash
def RemoverDaHash(tabela, num):
    pos = FuncaoHashing(num)
    if tabela[pos] is None:
        print("Número não encontrado")
    else:
        tabela[pos] = tabela[pos].prox
