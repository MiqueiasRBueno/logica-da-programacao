# Programa para calcular área de um lote

print() # Imprimi uma linha em branco
print("\033[1;35mPrograma para calcular área de um lote\033[m\n") # Imprime o título do programa
comp = float(input('Digite o comprimento do terreno em metros: ')) # Solicita ao usuário a entrada do comprimento do lote
larg = float(input('Digite a largura do terreno em metros: ')) # Solicita ao usuário a entrada da largura do lote
area = float(comp * larg) # Calcula a área do lote de acordo com as entradas do usuário
print(f'A área total calculada do terreno: {area} m²') # Imprime o resultado pós processamento dos dados



print('\033[1;35;4mA Ester quer café!!!\033[m') # Imprimi uma frase para ester