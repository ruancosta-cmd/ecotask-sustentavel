from app import orientar_descarte, validar_cep

def test_fluxo_descarte():
    assert "Lixo azul" in orientar_descarte("papel")

def test_integracao_viacep():
    # Valida se a aplicação consegue falar com a API externa
    assert validar_cep("01001000") is not None
