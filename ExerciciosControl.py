
import this
import ExercicioMoldel
this.opcao = -1

def Menu():
    print('Menu\n\n'         +
          '\n1.  Exercicio 01'+
          '\n2.  Exercicio 02'+
          '\n3.  Exercicio 03'+
          '\n4.  Exercicio 04'+
          '\n5.  Exercicio 05'+
          '\n6.  Exercicio 06'+
          '\n7.  Exercicio 07'+
          '\n8.  Exercicio 08'+
          '\n9.  Exercicio 09'+
          '\n10. Exercicio 10'+
          '\n11. Exercicio 11'+
          '\n12. Exercicio 12'+
          '\n13. Exercicio 13'+
          '\n14. Exercicio 14'+
          '\n15. Exercicio 15'+
          '\n16. Exercicio 16'+
          '\n17. Exercicio 17'+
          '\n18. Exercicio 18'+
          '\n19. Exercicio 19'+
          '\n20. Exercicio 20'+
          '\n0. Sair'        +
          '\nEscolha uma das opções acima: ')
    this.opcao = int(input())

def Executar():
    while(this.opcao != 0):
        Menu()
        if this.opcao == 0:
            print('Obrigado!')
        elif this.opcao == 1:
            print(ExercicioMoldel.Exercicio01())
        elif this.opcao == 2:
            print("Informe um número")
            num1 = int(input())
            print(ExercicioMoldel.Exercicio02(num1))
        elif this.opcao == 3:
            print('Infome a base do retângulo')
            bas = float(input())
            print('Informe a altura do retângulo')
            alt = float(input())
            print(ExercicioMoldel.Exercicio03(bas, alt))
        elif this.opcao == 4:
            print('informe quantos anos completos que você tem')
            anos = float(input())
            print('Informe a quantidade de meses completos que você tem')
            meses = float(input())
            print('Infome a quantidade de dias completos que você tem')
            dias = float(input())
            print(ExercicioMoldel.Exercicio04(anos, meses, dias))
        elif this.opcao == 5:
            print(ExercicioMoldel.Exercicio05())
        elif this.opcao == 6:
            print(ExercicioMoldel.Exercicio06())
        elif this.opcao == 7:
            print('Informe o valor de fábrica do veículo')
            fab = float(input())
            print(ExercicioMoldel.Exercicio07(fab))
        elif this.opcao == 8:
            print('Informe a primeira nota')
            n1 = float(input())
            print('Informe a segunda nota')
            n2 = float(input())
            print('Informe a terceira nota')
            n3 = float(input())
            print(ExercicioMoldel.Exercicio08(n1, n2, n3))
        elif this.opcao == 9:
            print('Qual a quantidade de maça que vossa senhoria quer comprar')
            qnt = int(input())
            print(ExercicioMoldel.Exercicio09(qnt))
        elif this.opcao == 11:
            print('Qual salário do vendedor(a)?')
            sal = float(input())
            print('Qual o valor de venda do vendedor(a)?')
            vendas = float(input())
            print(ExercicioMoldel.Exercicio11(vendas, sal))
        elif this.opcao == 12:
            print('Digite o número da sua conta')
            cont = int(input())
            print('Qual valor do seu saldo antes dos gastos?')
            sal = float(input())
            print('Qual valor gasto em débito?')
            deb = float(input())
            print('Qual o valor gasto em crédito?')
            cred = float(input())
            print(ExercicioMoldel.Exercicio12(cont, sal, deb, cred))
        else:
            print('Opção informada não é válida')