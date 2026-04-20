from app import orientar_descarte, validar_cep

def test_descarte_papel():
    assert "Lixo azul" in orientar_descarte("papel")

# NOVO: Teste de Integração com a API ViaCEP
def test_integracao_viacep_valido():
    # Testando com o CEP da Praça da Sé
    resultado = validar_cep("01001000")
    assert resultado is not None
    assert "Praça da Sé" in resultado

def test_viacep_invalido():
    assert validar_cep("00000000") is None
