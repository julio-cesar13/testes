def blocks():
    doc = open("templates/template", "r")
    lista = doc.readlines()
    lista_cor = []
    
    for i in range(26):
        for j in range(38):
            if lista[i][j] == '1':
                lista_cor.append((i + 1, j + 1))
    return lista_cor
