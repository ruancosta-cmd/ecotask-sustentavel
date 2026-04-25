import requests


def validar_cep(cep):
    """Valida o CEP usando a API ViaCEP."""
    cep_limpo = str(cep).replace("-", "").strip()
    if len(cep_limpo) != 8 or not cep_limpo.isdigit():
        return None
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                logradouro = data.get('logradouro', '')
                localidade = data.get('localidade', '')
                return f"{logradouro}, {localidade}"
    except Exception:
        return None
    return None


def orientar_descarte(material):
    """Retorna a cor do lixo para o material."""
    materiais = {
        "papel": "Lixo azul",
        "plastico": "Lixo vermelho",
        "vidro": "Lixo verde",
        "pilha": "Coletores especificos"
    }
    return materiais.get(material.lower().strip(), "Nao catalogado")


if __name__ == "__main__":
    print("EcoTask Rodando")