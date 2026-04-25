from app import orientar_descarte, validar_cep

def test_descarte():
    assert "Lixo azul" in orientar_descarte("papel")

def test_viacep_integracao():
    # Teste de integracao real
    resultado = validar_cep("01001000")
    assert resultado is not None
    assert "Se" in resultado or "S" in resultado
