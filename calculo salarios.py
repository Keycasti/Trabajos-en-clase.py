print("Bienvenido al sistema de calculo de calculo de pago por empleados")
while True:
    nombre_trabajador = input("Ingrese el nombre del trabajador (o escriba 'salir' para terminar):")
    if nombre_trabajador.lower()=="salir":
        break
    
    try:
        horas_trabajadas = int(input("Ingrese el numero de horas trabajadas: "))
        tarifa_por_hora = int(input("Ingrese el valor de la tarifa por hora: "))
        llegadas_tarde = int(input("Ingrese el numero de veces que llego tarde: "))
    except ValueError:
        print("Error: por favor, ingrese solo numero.")
        continue
    
    if horas_trabajadas > 40:
        horas_extras = horas_trabajadas - 40
        horas_extras = horas_extras * (tarifa_por_hora* 1.2)
        pago_total = (40 * tarifa_por_hora) +  "pago_horas_extras"
    else:
        pago_total = horas_trabajadas * tarifa_por_hora
        
        if pago_total > 600000:
            pago_total += 50000 # Bonificacion
            
            if llegadas_tarde >= 3:
                pago_total -= pago_total *0.05 # Descuento del 5%
                
                print(f"El pago total para {nombre_trabajador } es: ${pago_total:.2f}")
                print("--------------------------------------------------")
        
        
        
         
        
        