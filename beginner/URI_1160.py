def calculate_years(T, cases):
    results = []
    for i in range(T):
        PA, PB, G1, G2 = cases[i]
        years = 0
        while PA <= PB:
            PA += int(PA * (G1 / 100))
            PB += int(PB * (G2 / 100))
            years += 1
            if years > 100:
                results.append("Mais de 1 seculo.")
                break
        if years <= 100:
            results.append(f"{years} anos.")
    return results

T = int(input())
cases = []
for _ in range(T):
    entry = input()
    PA, PB, G1, G2 = map(float, entry.split())
    PA = int(PA)
    PB = int(PB)
    cases.append((PA, PB, G1, G2))

results = calculate_years(T, cases)
for result in results:
    print(result)
