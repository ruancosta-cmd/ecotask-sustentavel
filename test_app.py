from app import orientar_descarte, validar_cep

def test_descarte_papel():
    assert "Lixo azul" in orientar_descarte("papel")

def test_integracao_viacep_valido():
    # Este é o teste de integração exigido pelo professor
    resultado = validar_cep("01001000")
    assert resultado is not None
