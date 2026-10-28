import pytest 
from src.inventario import clasificar_stock , detectar_sobrestock

 
def test_stock_agotado(): 
    assert clasificar_stock(0, 20) == "AGOTADO" 
 
def test_stock_critico(): 
    assert clasificar_stock(7, 20) == "CRITICO" 
 
def test_stock_bajo(): 
    assert clasificar_stock(15, 20) == "BAJO" 
 
def test_stock_normal(): 
    assert clasificar_stock(30, 20) == "NORMAL" 
 
def test_stock_invalido(): 
    with pytest.raises(ValueError): 
        clasificar_stock(-2, 20) 

def test_hay_sobrestock():
    assert detectar_sobrestock(150, 100) == True

def test_no_hay_sobrestock():
    assert detectar_sobrestock(80, 100) == False