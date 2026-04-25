import requests

def validar_cep(cep):
    cep = cep.replace("-", "").strip()
    if len(cep) != 8 or not cep.isdigit():
        return None
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" not in dados:
                return f"{dados['logradouro']}, {dados['bairro']} - {dados['localidade']}/{dados['uf']}"
    except requests.exceptions.RequestException:
        return None
    return None

def orientar_descarte(material):
    banco = {"pilha": "Coletores de eletrônicos.", "papel": "Lixo azul.", "vidro": "Lixo verde."}
    return banco.get(material.lower().strip(), "Material não catalogado.")

if __name__ == "__main__":
    print("--- EcoTask Intermediário ---")
    c = input("CEP: ")
    end = validar_cep(c)
    print(f"Endereço: {end}" if end else "CEP inválido.")
    m = input("Material: ")
    print(orientar_descarte(m))
