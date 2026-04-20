from app import orientar_descarte, validar_cep

def test_descarte_papel():
    assert "Lixo azul" in orientar_descarte("papel")

def test_integracao_viacep_valido():
    # Teste de integração real com a API
    resultado = validar_cep("01001000")
    assert resultado is not None
    assert "Praça da Sé" in resultado
