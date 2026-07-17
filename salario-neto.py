# programa para calcular salario neto
salario_bruto = float(input("salario bruto: "))
porcentaje = float(input("& impuestos: "))
deducciones = float(input("deducciones: "))
impuesto = salario_bruto * (porcentaje / 100)
salario_neto = salario_bruto - impuesto - deducciones
print("salario neto:", salario_neto)