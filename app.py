def orientar_descarte(material):
    banco_dados = {
        "pilha": "Descarte em coletores específicos de eletrônicos ou farmácias. NÃO jogue no lixo comum.",
        "papel": "Lixo azul. Certifique-se de que não está sujo com comida.",
        "plastico": "Lixo vermelho. Lave o recipiente para evitar mau cheiro.",
        "vidro": "Lixo verde. Se estiver quebrado, embrulhe em jornal para não ferir o coletor."
    }
    material_limpo = material.lower().strip()
    if not material_limpo:
        return "Erro: O material não pode estar vazio."
    return banco_dados.get(material_limpo, "Material não catalogado. Consulte o site da prefeitura para este item.")

if __name__ == "__main__":
    print("--- EcoTask: Guia de Descarte Consciente ---")
    item = input("Qual material você deseja descartar? ")
    print(orientar_descarte(item))
