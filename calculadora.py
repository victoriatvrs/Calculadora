import math

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("\n\n[1] Soma")
print("\n[2] Subtração")
print("\n[3] Multiplicação")
print("\n[4] Divisão")
print("\n[5] Potência")
print("\n[6] Raiz quadrada (usado apenas o primeiro número)")
operacao = input("\nEscolha a operação: ")

if operacao == '1':
  result = n1 + n2
  print(f"{n1} + {n2} = {result}")
  
elif operacao == '2':
  result = n1 - n2
  print(f"{n1} - {n2} = {result}")
  
elif operacao == '3':
  result = n1 * n2
  print(f"{n1} * {n2} = {result}")
  
elif operacao == '4':
  result = n1 / n2
  print(f"{n1} / {n2} = {result}")
  
elif operacao == '5':
  result = 1
  for _ in range(int(n2)):
    result = result * n1
  print(f"{n1}ˆ{n2} = {result}")
  
elif operacao == '6':
  result = math.sqrt(n1)
  print(f"Raiz quadrada de {n1} = {result}")
  
else:
  print("Operação inválida!")