from app import orientar_descarte, validar_cep

def test_simples():
    assert orientar_descarte("papel") == "Lixo azul"

def test_api_integracao():
    # Teste de integracao real com a API ViaCEP
    resultado = validar_cep("01001000")
    assert resultado is not None
    assert "Praça da Sé" in resultado or "Praca da Se" in resultado
