
def Exercicio01():
    A = 10
    B = 20
    msg = "Antes da troca: A = {}, B = {}".format(A,B)
    aux = A
    A   = B
    B   = aux
    msg = msg + "\nApós a troca A = {}, B = {}".format(A,B)
    return msg

def Exercicio02(num1):
    return num1 - 1

def Exercicio03(bas, alt):
    return bas * alt

def Exercicio04(anos, meses, dias):
    return (anos * 365) + (meses * 30) + dias

def Exercicio05():
    print('Informe a quantidade da população')
    pop = int(input())
    print('Informe a quantidade de votos brancos')
    bra = float(input())
    print('nforme a quantidade de votos nulos')
    nul = float(input())
    print('Informe a quantidade de votos válido')
    val = float(input())
    print('A porcetagem de votos em brancos é: ',(bra / pop) * 100,'%')
    print('A porcetagem de votos nulos é: ',(nul / pop) * 100,'%')
    print('A porcetagem de votos válidos é: ',(val / pop) * 100,'%')
    print('A quantidade total da população é: ',pop)

def Exercicio06():
    print('Informe o salário do colaborador(a)')
    salario = float(input())
    print('Informe a porcetagem que o colaborador terá de aumento')
    percen = float(input())
    A = (salario / 100) * percen + salario
    msg = 'O salário do colaborador(a) vai passar a ser: A = {}'.format(A)
    return msg

def Exercicio07(fab):
    dist = (fab * 1.28)
    gov = (fab * 1.45)
    vfinal = dist + gov
    msg = 'O valor final do veículo é: vfinal = {}'.format(vfinal)
    return msg

def Exercicio08(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    msg = 'A média do aluno(a) é: media = {}'.format(media)
    return msg

def Exercicio09(qnt):
     if qnt > 0 and qnt < 12:
         valor = qnt * 1.30
     else:
         valor = qnt * 1.00
     msg = 'O valor do produto é = {}'.format(valor)
     return msg

def Exercicio11(vendas, sal):
    if vendas > 0 and vendas <= 1500:
        sal = (sal * 0.3) + sal
    elif vendas == 0:
        sal = sal
    else:
        sal = (sal * 0.5) + sal
    msg = 'O valor do salário do venerdor esse mês é = {}'.format(sal)
    return msg

def Exercicio12(cont, sal, deb, cred):
    sal = sal - deb - cred
    if sal < 0:
        return 'Saldo NEGATIVO, reveja seus gastos!!!'
    else:
        return 'Parabéns, seu saldo é POSITIVO!!!'

def Exercicio13(num):
    if num < 0 or num > 10:
        return 'Digite um valor entre 1 e 10!!!!'
    else:
       return for x in range (1, 11):







