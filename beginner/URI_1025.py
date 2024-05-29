N1, N2, N3, N4 = input().split()

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

average = ((N1 * 2) + (N2 * 3 ) + (N3 * 4) + (N4 * 1)) / 10

print(f"Media: {average:.1f}")

if average >= 7:
    print("Aluno aprovado.")
elif (average >= 5 and  average < 7):

    score = float(input())
    print("Aluno em exame.")
    print(f"Nota do exame: {score:.1f}")
    average_final = (average + score) / 2

    if average_final >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {average_final:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {average_final:.1f}")

else:
    print("Aluno reprovado.")
