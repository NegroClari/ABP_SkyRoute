#BUCLE DEL MENU PRINCIPAL
cliente_existe=False
# Variables globales para el cliente, ventas y destino
razonsocial_cliente = ""
cuit_cliente = ""
correo_cliente = ""
boletoreserva=False
preciovuelo=0
reserva_pendiente = False
reserva_destino = ""
reserva_precio = 0
reserva_fecha_ida = ""
venta_registrada = False
venta_cliente_rs = ""
venta_cliente_cuit = ""
venta_destino = ""
venta_precio = 0
venta_fecha = ""
#contadores
id_cliente = 0
venta_id_unico=0


while True:
    print("--- Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes ---")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Consultar Ventas")
    print("5. Botón de Arrepentimiento")
    print("----------------------------------------------------------")
    # Pedimos al usuario que ingrese su opción
    opcion_principal = input("Ingrese una opción: ")

    # ANALIZO PRIMER OPCION DEL BUCLE PRINCIPAL
    if opcion_principal=='1':
        print("Gestionar Clientes")
        print("1. Ver Clientes")
        print("2. Agregar Cliente")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")
        opcion_clientes = input("Ingrese una opcion:")

        #OPCION 1 SUB MENU 
        if opcion_clientes=='1':
            print("\n--- Ver Clientes ---")
            if not cliente_existe:
                print("No hay registro de cliente.") 
            else:
                print(f"A continuacion datos del ultimo cliente registrado: {razonsocial_cliente}, {cuit_cliente}, {correo_cliente}")
            input("Presione Enter para continuar...")

        #OPCION 2 SUB MENU 
        elif opcion_clientes=='2':
            print("\n--- Agregar Cliente ---")
            razonsocial_cliente = input("Ingrese nombre del nuevo cliente: ")
            cuit_cliente = input("Ingrese CUIT del nuevo cliente: ")
            correo_cliente= input("Ingrese Correo de Contacto del nuevo cliente: ")
            
            # VERIFICO QUE TODOS LOS DATOS HAYAN SIDO INGRESADO Y NINGUNO ESTE EN BLANCO
            if not razonsocial_cliente or not cuit_cliente or not correo_cliente:
                print("Error: DEBE COMPLETAR TODOS LOS CAMPOS")
            else: 
                id_cliente += 1 # Incrementar el contador
            
                print(f"Datos ingresados para el Cliente ID {id_cliente}: {razonsocial_cliente}, {cuit_cliente}, {correo_cliente}")
                cliente_existe=True
                input("Presione ENTER para guardar sus datos y volver al menu principal")
        
        #OPCION 3 SUB MENU
        elif opcion_clientes == '3':
            print("\n--- Modificar Cliente Actual ---")
            if not cliente_existe:
                print("No hay cliente para modificar. Agregue uno primero.")
            else:
                # Mostramos el ID del cliente actual
                print(f"Datos actuales del cliente (ID: {id_cliente}):")
                print(f"Razón Social: {razonsocial_cliente}")
                print(f"CUIT: {cuit_cliente}")
                print(f"Correo: {correo_cliente}")
                print("\nIngrese los nuevos datos (deje en blanco para mantener el actual):")
                
                nueva_razonsocial = input(f"Nueva Razón Social ({razonsocial_cliente}): ")
                if nueva_razonsocial:
                    razonsocial_cliente = nueva_razonsocial 
                
                nuevo_cuit = input(f"Nuevo CUIT ({cuit_cliente}): ")
                if nuevo_cuit:
                    cuit_cliente = nuevo_cuit
                    
                nuevo_correo = input(f"Nuevo Correo ({correo_cliente}): ")
                if nuevo_correo:
                    correo_cliente = nuevo_correo 
                
                print(f"Cliente (ID: {id_cliente}) modificado exitosamente.")
            input("Presione Enter para volver al menu principal")
        
        #OPCION 4 SUB MENU
        elif opcion_clientes == '4':
            print("\n--- Eliminar Cliente Actual ---")
            if not cliente_existe:
                print("No hay cliente para eliminar.")
            else:
                confirmacion = input(f"¿Está seguro de eliminar a '{razonsocial_cliente}' (ID: {id_cliente})? (S/N): ").upper()
                if confirmacion == 'S':
                    razonsocial_cliente = ""
                    cuit_cliente = ""
                    correo_cliente = ""
                    cliente_existe = False
                  
                    print("Cliente eliminado. Volver al MENU PRINCIPAL")
                else:
                    print("Operación cancelada.")
            input("Presione Enter para continuar...")
        #OPCION 5 SUB MENU
        elif opcion_clientes == '5':
            pass 
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
   
    #2 OPC BUCLE PRINCIPAL
    elif opcion_principal=='2':
        print("GESTIONAR DESTINOS")
        print("Listado de destinos disponibles:\n °BRC (san carlos de bar.) \n °MDZA (mendoza) \n °BSAS (buenos aires) \n °SLTA (salta)\n °NEUQ (neuquen) \n °COM RIV (comodoro rivadavia) \n °SANTIAGO (santiago de chile) \n °JUJUY (san salvador de jujuy) \n °LIMA (lima peru)")      
        destino = input("Ingrese siglas del destino a consultar precio: ").upper() 
        if destino == 'BRC':
            print("El costo de su viaje es de $141.863 ARS")
            preciovuelo=141863
        elif destino == 'MDZA':
            print("El costo de su viaje es de $62.046 ARS")
            preciovuelo=62046
        elif destino == 'BSAS':
            print("El costo de su viaje es de $44.341 ARS")
            preciovuelo=44341
        elif destino == 'SLTA':
            print("El costo de su viaje es de $80.163 ARS")
            preciovuelo=80163
        elif destino == 'NEUQ':
            print("El costo de su viaje es de $89.854 ARS")
            preciovuelo=89854
        elif destino == 'COM RIV':
            print("El costo de su viaje es de $171.067 ARS")
            preciovuelo=171067
        elif destino == 'SANTIAGO':
            print("El costo de su viaje es de $332.378 ARS")
            preciovuelo=332378
        elif destino == 'JUJUY':
            print("El costo de su viaje es de $133.271 ARS")
            preciovuelo=133271
        elif destino == 'LIMA':
            print("El costo de su viaje es de $616.715 ARS")
            preciovuelo=616715
        else:
            print("Destino no reconocido o no disponible.")
        if preciovuelo > 0: 
            respuesta_reserva = input("Ingrese S para confirmar el boleto, ingrese N para cancelar la operación: ").upper()
            
            if respuesta_reserva == 'S':
                fecha_vuelo = input("Ingrese la fecha de ida para su reserva (DD-MM-AAAA): ")
                
                # Almacenamos los datos de la reserva en las variables globales que definimos al principio del programa
                reserva_destino = destino
                reserva_precio = preciovuelo
                reserva_fecha_ida = fecha_vuelo
                reserva_pendiente = True # Marcamos que hay una reserva en espera
                
                print("\n--- ¡Boleto reservado! ---")
                print("Por favor, diríjase a '3. Gestionar Ventas' para completar la compra.")
                print(f"Reserva para: {reserva_destino} el {reserva_fecha_ida} por ${reserva_precio} ARS")
            elif respuesta_reserva == 'N':
                print("Operación de reserva cancelada.")
            else:
                print("Respuesta no válida.")
        input("Presione Enter para continuar...")
   
   #BUCLE PRINCIPAL OPCION 3 
    elif opcion_principal == '3':
        print("\n--- GESTIONAR VENTAS ---")
        print("1. Procesar reserva pendiente")
        print("2. Cancelar reserva pendiente y volver al Menú Principal")
        opcion_ventas=input("Seleccione su gestion")
        
        #Bucle 1 gestionar ventas
        if opcion_ventas == '1': # Procesar reserva
            print("\n--- Procesar Reserva Pendiente ---")
            if not reserva_pendiente:
                print("No hay ninguna reserva pendiente para procesar.")
                print("Por favor, vaya a '2. Gestionar Destinos' para crear una reserva primero.")
            else:
                print("\n--- Detalles de la Reserva Pendiente ---")
                print(f"Destino: {reserva_destino}")
                print(f"Fecha de Ida: {reserva_fecha_ida}")
                print(f"Precio: ${reserva_precio:,.2f} ARS")
                confirmacion_venta = input("\n¿Confirmar la venta de esta reserva? (S/N): ").upper()
            if confirmacion_venta == 'S':
                venta_cliente_rs =razonsocial_cliente
                venta_cliente_cuit = cuit_cliente 
                venta_destino = reserva_destino
                venta_precio = reserva_precio
                venta_fecha = reserva_fecha_ida
                venta_id_unico += 1 #contador id ventas
                venta_registrada = True
                        
            # Limpiamos la reserva pendiente, ya que fue procesada
                reserva_pendiente = False
                reserva_destino = ""
                reserva_precio = 0
                reserva_fecha_ida = ""

                print("\n--- ¡Venta de Reserva Procesada con Éxito! ---")
                print(f"ID de Venta: {venta_id_unico}")
                print(f"Destino: {venta_destino}")
                print(f"Precio: ${venta_precio:,.2f} ARS")
                print(f"Fecha: {venta_fecha}")
                print(f"Se enviara a su correo:",{correo_cliente},"el cupon de pago e indicaciones para finalizar la venta")
            else:
                print("Procesamiento de reserva cancelado.")
                input("Presione Enter para volver al menú de Ventas...")
        elif opcion_ventas == '2': # Cancelar reserva pendiente
            print("\n--- Cancelar Reserva Pendiente ---")
            if not reserva_pendiente:
                print("No hay ninguna reserva pendiente para cancelar.") 
            else:
                confirmacion_cancelar = input(f"¿Está seguro de cancelar la reserva para {reserva_destino} ({reserva_fecha_ida})? (S/N): ").upper()
                if confirmacion_cancelar == 'S':
                    # Limpiamos los datos de la reserva y la bandera
                    reserva_pendiente = False
                    reserva_destino = ""
                    reserva_precio = 0.0
                    reserva_fecha_ida = ""
                    print("Reserva cancelada exitosamente.Derecho de cancelacion de compra (Ley 24.240 de Defensa al Consumidor y en el Código Civil y Comercial de la Nación (Ley 26.994)")
                else:
                    print("Cancelación de reserva abortada.")
                input("Presione Enter para volver al Menú Principal.")
#BUCLE PRINCIPAL OPCION 4 
    elif opcion_principal == '4':
        print("\n--- CONSULTAR VENTAS ---")
        # Verificamos si la bandera 'venta_registrada' es True
        if not venta_registrada:
            print("No hay ventas registradas aún en el sistema.")
            print("Por favor, procese una reserva en '3. Gestionar Ventas' para registrar una venta.")
        else:
            print("\n--- Detalles de la ÚLTIMA Venta Registrada ---")
            print(f"Cliente: {venta_cliente_rs} (CUIT: {venta_cliente_cuit})")
            print(f"ID de Venta: {venta_id_unico}")
            print(f"Destino: {venta_destino}")
            print(f"Precio: ${venta_precio:,.2f} ARS") 
            print(f"Fecha de Venta: {venta_fecha}")
        input("Presione Enter para continuar...")
# BUCLE PRINCIPAL OPCION 5
    elif opcion_principal == '5':
        print("\n--- Botón de Arrepentimiento ---")
        if not venta_registrada:
            print("No hay ninguna venta registrada de la cual arrepentirse.")
            print("Para usar esta función, primero debe haber una venta procesada.")
        else:
            print(f"La última venta registrada (ID: {venta_id_unico}) es para {venta_cliente_rs} con destino {venta_destino}.")
            confirmacion_arrepentimiento = input("¿Está seguro que desea cancelar esta venta? (S/N): ").upper()
            
            if confirmacion_arrepentimiento == 'S':
                # Reseteamos las variables de la última venta
                
                venta_registrada = False
                venta_cliente_rs = ""
                venta_cliente_cuit = ""
                venta_destino = ""
                venta_precio = 0
                venta_fecha = ""
                venta_id_unico = 0 
                
                print("¡Venta cancelada exitosamente! Los datos de la última venta han sido eliminados.")
            elif confirmacion_arrepentimiento == 'N':
                print("Operación de arrepentimiento cancelada.")
            else:
                print("Respuesta no válida.")
        input("Presione Enter para continuar...")
#Si no ingresa una opcion del menu principal.

    else:
        print("Opción no válida. Intente de nuevo.")
      