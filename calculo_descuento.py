def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamadas a la función
monto_1 = 1000
monto_2 = 1500
porcentaje_1 = 15

# Primera llamada con el descuento predeterminado
descuento_1 = calcular_descuento(monto_1)
print(f"Descuento en la compra de ${monto_1}: ${descuento_1}")
print(f"Monto final a pagar: ${monto_1 - descuento_1}")

# Segunda llamada con un porcentaje personalizado
descuento_2 = calcular_descuento(monto_2, porcentaje_1)
print(f"Descuento en la compra de ${monto_2} con {porcentaje_1}% de descuento: ${descuento_2}")
print(f"Monto final a pagar: ${monto_2 - descuento_2}")
