interface =  """

                       ===== MENU =====

    Sejam Bem-Vindos(a), qual operação deseja realizar hoje?

    (1) Depósito
    (2) Saque
    (3) Extrato
    (4) Sair

 
 """


saldo = 0
extrato = ""
saque = 0
saque_diario = 0 
limite_saque = 3


while True:

    print(interface)
    
    operacao = int(input(f"Resposta: "))

    if operacao == (1):
      
      valor = float(input(f"\nQual valor gostaria de depositar? R$"))
      
      if valor > 0:
          saldo += valor
          extrato += f"Depósito de R$ {valor:.2f} realizado com sucesso.\n"
          print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.\n")
      else:
       print("\nO valor inserido é inválido. Por favor, verifique e tente novamente com um valor correto.\n")
    
    elif operacao == (2):
       
       saque = float(input(f"\nPor favor, insira o valor desejado para saque. R$"))

       if saque <= saldo:
          if saque <= 500:
             if saque_diario < limite_saque:
              saque_diario += 1
              saldo -= saque
              extrato += f"\nSaque de R$ {saque:.2f} realizado com sucesso.\n"
              print(f"\nSaque de R$ {saque:.2f} realizado com sucesso.")


             else:
               print("\nNão foi possível realizar o saque, pois o limite diário foi atingido. Por favor, tente novamente amanhã.\n")
          else:
            print("\nNão foi possível realizar o saque. Por favor, tente novamente com um valor dentro do limite de R$ 500.\n")
        

       else:
        print("\nNão foi possível realizar a operação devido à falta de saldo. Por favor, verifique seu saldo e tente novamente.\n")

    elif operacao == (3):
        print("===== EXTRATO =====\n")
        if not extrato:
            print("\nNão foram realizadas operações na sua conta hoje.\n")
        else:
            print(extrato)
        print(f"\nSeu saldo atual é R$ {saldo:.2f}\n")
        print("===================\n")

    elif operacao == (4):
      print("\nAté a próxima operação\n ")
      break

    else:
      print("\nOperação invalida (erro de sintaxe), tente novamente\n")
