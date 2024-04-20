def cky_algorithm(grammar, string):
    n = len(string)
    # Inicializar tabla CKY
    table = [[set() for _ in range(n+1)] for _ in range(n)]
    
    # Paso 1: Llenar la diagonal principal de la tabla CKY con los símbolos terminales correspondientes
    for i in range(n):
        for nt, terminals in grammar.items():
            for t in terminals:
                if t == string[i]:
                    table[i][i+1].add(nt)
    
    # Paso 2: Calcular las celdas restantes de la tabla CKY
    for l in range(2, n+1):  # Longitud de la subcadena
        for i in range(n - l + 1):  # Posición inicial de la subcadena
            j = i + l
            for k in range(i + 1, j):  # División de la subcadena
                for nt, productions in grammar.items():
                    for prod in productions:
                        if len(prod) == 2: 
                            B, C = prod
                            if B in table[i][k] and C in table[k][j]:
                                table[i][j].add(nt)
    
    # Paso 3: Comprobar si la cadena pertenece al lenguaje generado por la gramática
    return 'S' in table[0][n]

def main():
    print("Ingrese el número de casos:")
    c = int(input())  # Número de casos
    for case in range(1, c+1):
        print(f"\nCaso {case}:")
        print("Ingrese el número de no terminales y el número de cadenas a analizar separados por un espacio:")
        l = input()
        n = [int(i) for i in l.split()]
        G = {}
        print("Ingrese las producciones de la gramática en el formato: <no_terminal> <derivaciones separadas por espacios>")
        for _ in range(n[0]):  # Leer las producciones de la gramática
            prod_input = input().split()
            G[prod_input[0]] = prod_input[1:]
        # print("Ingrese las cadenas a analizar:")
        for i in range(n[1]):  # Probar las cadenas
            if n[1] == 1 or i == 0:
                print("Ingrese la cadena a analizar:")
            else:
                print("Ingrese la otra cadena a analizar:")
            test_string = input()
            ans = cky_algorithm(G, test_string)
            if ans:
                print('yes')
            else:
                print('no')

if __name__ == "__main__":
    main()

    