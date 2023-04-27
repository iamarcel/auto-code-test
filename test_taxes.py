import taxes

def test_calculate_taxes():
    assert taxes.calculate_taxes(1000) == 200
    assert taxes.calculate_taxes(5000) == 1000
    assert taxes.calculate_taxes(7500) == 1500
    assert taxes.calculate_taxes(10000) == 2000
    assert taxes.calculate_taxes(15000) == 3000
    assert taxes.calculate_taxes(20000) == 4000
    assert taxes.calculate_taxes(25000) == 5000
    assert taxes.calculate_taxes(30000) == 6000
    assert taxes.calculate_taxes(35000) == 7000
    assert taxes.calculate_taxes(40000) == 8000
    assert taxes.calculate_taxes(45000) == 9000
    assert taxes.calculate_taxes(50000) == 10000
    assert taxes.calculate_taxes(55000) == 11000
    assert taxes.calculate_taxes(60000) == 12000
    assert taxes.calculate_taxes(65000) == 13000
    assert taxes.calculate_taxes(70000) == 14000
    assert taxes.calculate_taxes(75000) == 15000
    assert taxes.calculate_taxes(80000) == 16000
    assert taxes.calculate_taxes(85000) == 17000
    assert taxes.calculate_taxes(90000) == 18000
    assert taxes.calculate_taxes(95000) == 19000
    assert taxes.calculate_taxes(100000) == 20000
    print("All tests passed!")
