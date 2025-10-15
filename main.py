def analisar_arredondamento():
    while True:
        # Entrada do número
        print("\n--- Arredondamento & Truncamento ---")
        numero = input("Digite um número real: ").strip().replace(",", ".")
        try:
            valor = float(numero)
        except ValueError:
            print("Valor inválido. Tente novamente.\n")
            continue

        # Quantidade de casas decimais desejada
        try:
            casas = int(input("Quantas casas decimais após a vírgula? "))
            if casas < 0:
                print("Use um valor positivo.\n")
                continue
        except ValueError:
            print("Digite um número inteiro válido.\n")
            continue

        # Conversão para string com várias casas para análise
        str_valor = f"{abs(valor):.10f}".rstrip("0").rstrip(".")
        partes = str_valor.split(".")
        parte_int = partes[0]
        parte_frac = partes[1] if len(partes) > 1 else ""

        # Completa a parte fracionária com zeros, se necessário
        while len(parte_frac) < casas + 2:
            parte_frac += "0"

        # Obtém os dígitos relevantes
        d_anterior = int(parte_frac[casas - 1]) if casas > 0 else 0
        d_corte = int(parte_frac[casas]) if len(parte_frac) > casas else 0
        d_seguinte = int(parte_frac[casas + 1]) if len(parte_frac) > casas + 1 else 0

        # --- Aplica as regras ---
        regra = ""
        arredondado = valor
        truncado = valor

        # Truncamento
        truncado = int(valor * (10 ** casas)) / (10 ** casas)

        # Arredondamento IEEE 754 (round half to even)
        if d_corte > 5:
            regra = (f"{d_corte} > 5 → arredonda para cima")
            arredondado = truncado + (1 / (10 ** casas))
        elif d_corte < 5:
            regra = (f"{d_corte} < 5 → arredonda para baixo (mantém)")
            arredondado = truncado
        else:  # d_corte == 5
            if d_seguinte > 0:
                regra = (f"{d_corte} = 5 e dígitos seguintes > 0 → arredonda para cima")
                arredondado = truncado + (1 / (10 ** casas))
            elif d_anterior % 2 != 0:
                regra = (f"{d_corte} = 5 e dígito anterior é ímpar → arredonda para cima (para par)")
                arredondado = truncado + (1 / (10 ** casas))
            else:
                regra = (f"{d_corte} = 5 e dígito anterior é par → mantém (round half to even)")
                arredondado = truncado

        # --- Exibição dos resultados ---
        print("\n--- Análise ---\n")
        print(f"Número original: {valor}")
        print(f"Parte fracionária: {parte_frac}\n")
        print(f"d{casas} = {d_anterior} | d{casas+1} = {d_corte} | d{casas+2} = {d_seguinte}")
        print(f"\nRegra aplicada: {regra}\n")
        print(f"Arredondado ({casas} casas): {round(arredondado, casas)}")
        print(f"Truncado    ({casas} casas): {truncado:.{casas}f}")
        print("\n---------------------------\n")

        # Verifica se quer continuar
        repetir = input("Deseja testar outro número? (s/n): ").strip().lower()
        if repetir != "s":
            print("Encerrando o programa...")
            break
        print("\n")


if __name__ == "__main__":
    analisar_arredondamento()
