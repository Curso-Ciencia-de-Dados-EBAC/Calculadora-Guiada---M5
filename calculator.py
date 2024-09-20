from menu import menu
from operator import add, sub, mul, truediv

print("\033[1mCalculadora Guiada\033[0m\n")
print("\033[1mUse as setas\033[0m para navegar pelo menu.")
print("Aperte \033[1mENTER\033[0m para selecionar.")
print("Aperte \033[1mESC\033[0m para encerrar o programa.")
print("Utilize \033[1m. (ponto)\033[0m como separador decimal para números reais.\n")

print("Escolha o modo de operação:")
mode = menu(["Inteiro", "Real"])
print(f"\nModo escolhido: \033[1m{mode}\033[0m\n")

print("Escolha a operação: ")
op_names = ["Adição", "Subtração", "Multiplicação", "Divisão"]
op_symbols = ["+", "-", "x", "/"]
op_functions = [add, sub, mul, truediv]
op_map = {
    name: {
        "symbol": symbol,
        "function": function
    } 
    for name, (symbol, function) in zip(op_names, list(zip(op_symbols, op_functions)))
}
op = menu(op_names)
print(f"\nOperação escolhida: \033[1m{op}\033[0m\n")

t = int if mode == "Inteiro" else float

try:
    a = input("Insira o primeiro valor: ")
    a = t(a)
    b = input("Insira o segundo valor: ")
    b = t(b)
except ValueError:
    if (not a or not b):
        print("Valor vazio")
    if (type(a) == str or type(b) == str):
        print("Valor inválido.")
        exit()
    print(f"Número não é {mode.lower()}.")
    
try:
    print(f"\n\033[3m{a} {op_map[op]['symbol']} {b} = {op_map[op]['function'](a,b)}\033[0m")
except (ZeroDivisionError, ValueError):
    print("Resultado indefinido.")
