from app import orientar_descarte, validar_cep

def test_descarte():
    assert "Lixo azul" in orientar_descarte("papel")

def test_viacep():
    # Teste de integração real
    assert validar_cep("01001000") is not None
