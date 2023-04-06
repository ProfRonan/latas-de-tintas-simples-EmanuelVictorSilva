print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)
litros_de_tinta = metros_quadrados / 3
if litros_de_tinta > 18:
   qtd_de_latas = int(litros_de_tinta/18) + 1
   valor_total = qtd_de_latas * 80
   print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")
if litros_de_tinta <= 18 and metros_quadrados > 0:
   qtd_de_latas = 1 
   valor_total = qtd_de_latas * 80
   print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")
   

