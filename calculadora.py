n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("\n\n[+] Soma")
print("\n[-] Subtração")
print("\n[*] Multiplicação")
print("\n[/] Divisão")
print("\n[ˆ] Potência")
operacao = input("\nEscolha a operação: ")

if operacao == "+":
  result = n1 + n2
  print(f"{n1} + {n2} = {result}")
  
elif operacao == "-":
  result = n1 - n2
  print(f"{n1} - {n2} = {result}")
  
elif operacao == "*":
  result = n1 * n2
  print(f"{n1} * {n2} = {result}")
  
elif operacao == "/":
  result = n1 / n2
  print(f"{n1} / {n2} = {result}")
  
elif operacao == "ˆ":
  result = 1
  for _ in range(int(n2)):
    result = result * n1
  print(f"{n1}ˆ{n2} = {result}")
  
else:
  print("Operação inválida!")