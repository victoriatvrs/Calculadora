import math

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("\n\n[1] Soma")
print("\n[2] Subtração")
print("\n[3] Multiplicação")
print("\n[4] Divisão")
print("\n[5] Potência")
print("\n[6] Raiz quadrada (apenas o primeiro número)")
print("\n[7] Porcentagem")
print("\n[8] Seno (apenas o primeiro número)")
print("\n[9] Cosseno (apenas o primeiro número)")
print("\n[10] Tangente (apenas o primeiro numero)")
print("\n[11] Logaritmo")
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
  
elif operacao == '7':
  result = (n1 * n2)/100
  print(f"{n1}% de {n2} = {result}")
  
elif operacao == '8':
  result = math.sin(math.radians(n1))
  print(f"Sin({n1}) = {result}")
  
elif operacao == '9':
  result = math.cos(math.radians(n1))
  print(f"Cos({n1}) = {result}")
  
elif operacao == '10':
  result = math.tan(math.radians(n1))
  print(f"Tan({n1}) = {result}")
  
elif operacao == '11':
  result = math.log(n1, n2)
  print(f"Log de {n1} na base {n2} = {result}")
  
else:
  print("Operação inválida!")