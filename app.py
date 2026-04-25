import requests

def validar_cep(cep):
    """Consulta a API ViaCEP para validar o endereço."""
    cep = str(cep).replace("-", "").strip()
    if len(cep) != 8 or not cep.isdigit():
        return None
    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" not in dados:
                logradouro = dados.get('logradouro', '')
                localidade = dados.get('localidade', '')
                return f"{logradouro}, {localidade}"
    except requests.exceptions.RequestException:
        return None
    return None

def orientar_descarte(material):
    """Retorna a cor do lixo para cada material."""
    banco_dados = {
        "pilha": "Coletores especificos",
        "papel": "Lixo azul",
        "plastico": "Lixo vermelho",
        "vidro": "Lixo verde"
    }
    return banco_dados.get(material.lower().strip(), "Material nao catalogado")

if __name__ == "__main__":
    print("EcoTask")
