import requests

def validar_cep(cep):
    """Consulta a API ViaCEP para validar o endereço."""
    cep = cep.replace("-", "").strip()
    if len(cep) != 8 or not cep.isdigit():
        return None
    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        # Faz a chamada à API pública (HTTP GET)
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" not in dados:
                return f"{dados['logradouro']}, {dados['bairro']} - {dados['localidade']}/{dados['uf']}"
    except requests.exceptions.RequestException:
        return None
    return None

def orientar_descarte(material):
    banco_dados = {
        "pilha": "Descarte em coletores específicos de eletrônicos ou farmácias.",
        "papel": "Lixo azul. Certifique-se de que não está sujo com comida.",
        "plastico": "Lixo vermelho. Lave o recipiente.",
        "vidro": "Lixo verde. Se estiver quebrado, embrulhe em jornal."
    }
    material_limpo = material.lower().strip()
    return banco_dados.get(material_limpo, "Material não catalogado.")

if __name__ == "__main__":
    print("--- EcoTask: Descarte Consciente + Localização ---")
    cep_input = input("Digite o seu CEP para validar a localização: ")
    endereco = validar_cep(cep_input)
    if endereco:
        print(f"✅ Localização confirmada: {endereco}")
    else:
        print("❌ CEP inválido ou não encontrado.")
    item = input("\nQual material deseja descartar? ")
    print(orientar_descarte(item))
