from app import orientar_descarte

def test_descarte_correto():
    # Testa o caminho feliz (papel no lixo azul)
    assert "Lixo azul" in orientar_descarte("papel")

def test_material_vazio():
    # Testa erro de entrada vazia
    assert "Erro" in orientar_descarte("")

def test_material_desconhecido():
    # Testa um caso de material que não temos no banco
    assert "não catalogado" in orientar_descarte("pneu")
