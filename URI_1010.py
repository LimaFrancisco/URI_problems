codigo1, unidade1, preco1 = input().split()
unidade1 = int(unidade1)
preco1 = float(preco1)

codigo2, unidade2, preco2 = input().split()
unidade2 = int(unidade2)
preco2 = float(preco2)

valor_a_pagar = (unidade1 * preco1) + (unidade2 * preco2)

print(f"VALOR A PAGAR: R$ {valor_a_pagar:.2f}")
