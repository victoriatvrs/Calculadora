import math

print("\n[1] Soma")
print("\n[2] Subtração")
print("\n[3] Multiplicação")
print("\n[4] Divisão")
print("\n[5] Potência")
print("\n[6] Raiz quadrada")
print("\n[7] Porcentagem")
print("\n[8] Seno")
print("\n[9] Cosseno")
print("\n[10] Tangente")
print("\n[11] Logaritmo")
operacao = input("\nEscolha a operação: ")

n1 = float(input("\nDigite um número: "))
if operacao != '6' and operacao != '8' and operacao != '9' and operacao != '10':
  n2 = float(input("\nDigite o segundo número: "))  

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
  if n2 == 0:
    print("Impossível realizar divisão por 0!")
  else:
    result = n1 / n2
    print(f"{n1} / {n2} = {result}")
  
elif operacao == '5':
  result = 1
  for _ in range(int(n2)):
    result = result * n1
  print(f"{n1}ˆ{n2} = {result}")
  
elif operacao == '6':
  if n1 < 0:
    print("Essa raiz não existe no conjunto dos reais!")
  else:
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
  if n1 <= 0 or n2 <= 0 or n == 1:
    print("Impossível!")
  else: 
    result = math.log(n1, n2)
    print(f"Log de {n1} na base {n2} = {result}")
  
else:
  print("Operação inválida!")