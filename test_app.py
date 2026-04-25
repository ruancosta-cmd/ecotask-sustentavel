from app import orientar_descarte, validar_cep

def test_descarte():
    assert "azul" in orientar_descarte("papel")

def test_api_viacep():
    # Teste de integracao real
    res = validar_cep("01001000")
    assert res is not None
