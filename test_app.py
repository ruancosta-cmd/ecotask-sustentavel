from app import orientar_descarte, validar_cep

def test_fluxo_descarte():
    assert "Lixo azul" in orientar_descarte("papel")

def test_integracao_viacep():
    # Testa a comunicação real com a API pública
    resultado = validar_cep("01001000")
    assert resultado is not None
    assert "Praça da Sé" in resultado
