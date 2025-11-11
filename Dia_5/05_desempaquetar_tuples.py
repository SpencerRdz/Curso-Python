precios_cafe = [("Espresso", 1.5), ("Cappuccino", 2.5), ("Latte", 3.0)]

def cafe_mas_caro(precios):
    precio_mayor = 0
    cafe_caro = ""
    for cafe, precio in precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro = cafe
        else:
            pass

    return cafe_caro, precio_mayor


cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El café más caro es {cafe} y cuesta ${precio}")