valor_da_lata = 80
litros_de_uma_lata = 18
cobertura = 3

print("Bem vindo à loja de Tintas do seu ZÉ")
metros_quadrados =float( input("Qual a área em m²?\n"))






litros_de_tinta = metros_quadrados/cobertura
qtd_de_latas =  int(litros_de_tinta/litros_de_uma_lata)
if (litros_de_tinta%litros_de_uma_lata != 0):
    qtd_de_latas += 1
valor_total = qtd_de_latas*valor_da_lata

print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")


#No arquivo `main.py`, escreva instruções para resolver um problema de uma loja de tintas.
#Não altere o código já criado adicione suas instruções **APENAS** no(s) local(is) indicado(s).
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a 
# tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.