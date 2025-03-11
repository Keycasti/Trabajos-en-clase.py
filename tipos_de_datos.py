#mensaje de bienvenida
print("bienvenido al sistema de calculo de empleados")
nombre_trabajador=input("ingrese el nombre del trabajador: ")
horas_trabajadas=int(input("ingrese las horas trabajadas:"))
tarifa_por_hora=int(input("ingrese la tarifa por hora:"))
pago_total = horas_trabajadas * tarifa_por_hora
print("el pago total es:$",pago_total)