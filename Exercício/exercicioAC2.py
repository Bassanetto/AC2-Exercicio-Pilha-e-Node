
from ast import Break
from Node import Node #nó simples a ser utilizado na pilha

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        #insere um item na pilha
        node = Node(data) #CRIOU UM NÓ
        node.next = self.top #APONTOU PARA O PRÓXIMO 
        self.top = node #adiciona o nome criado no topo da pilha
        self.size = self.size + 1 

   
    def peek(self):
        # retorna o topo sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")
    
    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r
    def __str__(self):
        return self.__repr__()

pilha = Stack()
n = int(input("Insira um número: "))
pilha.push(n)
x = str(input("Insira a operação: "))
if x != '!':
    pilha.push(x)
    y = int(input("Insira um número: "))
    pilha.push(y)
    if x == '+':
        r = (n + y)
    elif x == '/':
        if y == 0:
            r = print("não é possível dividir por zero") 
        else:
            r = (n / y)
    elif x == '-':
        r = (n - y)
    elif x == '*':
        r = (n * y)
    elif x == '^':
        r = (n ** y)
else:
    r = 1
    for num in range(1, n + 1):
        r *= num


print(pilha)
print (r)


