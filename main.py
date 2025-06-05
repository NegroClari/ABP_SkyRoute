#PROYECTO SIN MODODULARIZAR

import datetime

# Usaremos listas para almacenar múltiples clientes, reservas y ventas.
# Cada elemento en la lista será un diccionario para representar los datos.

clientes_registrados = []  # Lista de clientes
reservas_pendientes = []   # Lista para almacenar reservas pendientes
ventas_finalizadas = []    # Lista para almacenar ventas ya procesadas

# Diccionario de destinos con sus precios
destinos_disponibles = {
    'BRC': {'nombre': 'San Carlos de Bariloche', 'precio': 141863},
    'MDZA': {'nombre': 'Mendoza', 'precio': 62046},
    'BSAS': {'nombre': 'Buenos Aires', 'precio': 44341},
    'SLTA': {'nombre': 'Salta', 'precio': 80163},
    'NEUQ': {'nombre': 'Neuquén', 'precio': 89854},
    'COM RIV': {'nombre': 'Comodoro Rivadavia', 'precio': 171067},
    'SANTIAGO': {'nombre': 'Santiago de Chile', 'precio': 332378},
    'JUJUY': {'nombre': 'San Salvador de Jujuy', 'precio': 133271},
    'LIMA': {'nombre': 'Lima, Perú', 'precio': 616715}
}

#Contadores de IDs
id_cliente = 0
id_reserva = 0
id_venta = 0

#Funciones para cada gestion y opciones del menu

def obtener_siguiente_id(lista_registros, clave_id): #Esta funcion es llamada en la funcion de agregar clientes nuevos y sirve para incrementar el ID
#Toma como argumento la lista clientes_registrados 
#verifica primero en la lista de registros si ya hay algun cliente ingresado y si no lo hay cambia el valor a 1
    if not lista_registros:
        return 1
    
    #Creamos una variable para guardar el ID más alto que encuentre.
    # La inicializamos en 0, asumiendo que los IDs siempre serán 1 o más.
    id_mas_alto_encontrado = 0
    
    # Paso 3: Recorremos cada 'registro' (que es un diccionario) en la lista de registros ( que trae la info de clientes_registrados).
    for registro_actual in lista_registros:
#El ciclo for va a tomar un elemento a la vez de la lista.
#En cada "vuelta" del ciclo, el elemento que se toma de la lista se guarda temporalmente en la variable registro_actual
        id_actual = registro_actual.get(clave_id, 0)  #Guardo en la variable id actual el ID del registro 
                                                    #y si clave_id no existe asume que su ID es 0. Utilizamos el GET por error en el codigo

#comparo el id actual y el id que deifinimos en 0 
        if id_actual > id_mas_alto_encontrado:
            # Si es así, actualizamos 'id_mas_alto_encontrado' con este nuevo valor.
            id_mas_alto_encontrado = id_actual
            
    # Cambio el contador al siguiente ID disponible es el 'id_mas_alto_encontrado' más 1.
    return id_mas_alto_encontrado + 1

def pausa_sistema(): #Detiene la ejecución hasta que el usuario presione Enter
    input("\nPresione Enter para continuar...")



# --- Módulo de Gestión de Clientes ---

def ver_clientes_registrados(): #Listado de los cliente registrados
    print("\n--- Ver Clientes ---")
    if not clientes_registrados: #corroboro que no este vacia mi lista para hacer la muestra
        print("No hay clientes registrados en el sistema.")
    else:
        print("Listado de Clientes:")
        for cliente in clientes_registrados:   #recorro la lista elemento por elemento y lo imprimo
            print(f"ID: {cliente['id_cliente']}, Razón Social: {cliente['razonsocial_cliente']}, CUIT: {cliente['cuit_cliente']}, Correo: {cliente['correo_cliente']}")
    pausa_sistema()

def agregar_nuevo_cliente():   #Agrego un cliente a la lista clientes_registrados.
    global id_cliente          #llamo a mi variable contador de id nombrada al principio del programa pq aqui se va a incrementar
    print("\n--- Agregar Cliente ---")
    razonsocial_cliente = input("Ingrese nombre/razón social del nuevo cliente: ")
    cuit_cliente= input("Ingrese CUIT del nuevo cliente: ")
    correo_cliente = input("Ingrese Correo de Contacto del nuevo cliente: ")

    if not razonsocial_cliente or not cuit_cliente or not correo_cliente:
        print("Error: DEBE COMPLETAR TODOS LOS CAMPOS.")
    else:
        if any(cuit['cuit_cliente'] == cuit_cliente for cuit in clientes_registrados):
            print("Error: Ya existe un cliente con el CUIT ingresado.")
            pausa_sistema()
            return

        id_cliente = obtener_siguiente_id(clientes_registrados, 'id_cliente')
        nuevo_cliente = {
            'id_cliente': id_cliente,
            'razonsocial_cliente': razonsocial_cliente,
            'cuit_cliente': cuit_cliente,
            'correo_cliente': correo_cliente,
        }
        clientes_registrados.append(nuevo_cliente)
        print(f"Cliente '{razonsocial_cliente}' (ID: {id_cliente}) agregado exitosamente.")
    pausa_sistema()

def buscar_cliente_por_id_o_cuit(identificador_busqueda):
    """
    Encuentra un cliente por su ID o CUIT.
    """
    if identificador_busqueda.isdigit():
        id_int = int(identificador_busqueda)
        for cliente in clientes_registrados:
            if cliente['id_cliente'] == id_int:
                return cliente
    
    for cliente in clientes_registrados:
        if cliente['cuit_cliente'] == identificador_busqueda:
            return cliente
    return None

def modificar_cliente_existente(): #  Permite actualizar los datos de un cliente existente.
    print("\n--- Modificar Cliente ---")
    if not clientes_registrados:
        print("No hay clientes para modificar. Agregue uno primero.")
        pausa_sistema()
        return

    identificador_cliente = input("Ingrese el ID o CUIT del cliente a modificar: ")
    cliente_encontrado = buscar_cliente_por_id_o_cuit(identificador_cliente)

    if cliente_encontrado:
        print(f"\nDatos actuales del cliente (ID: {cliente_encontrado['id_cliente']}):")
        print(f"Razón Social: {cliente_encontrado['razonsocial_cliente']}")
        print(f"CUIT: {cliente_encontrado['cuit_cliente']}")
        print(f"Correo: {cliente_encontrado['correo_cliente']}")

        print("\nIngrese los nuevos datos (deje en blanco para mantener el actual):")
        nueva_razonsocial_input = input(f"Nueva Razón Social ({cliente_encontrado['razonsocial_cliente']}): ")
        nuevo_cuit_input = input(f"Nuevo CUIT ({cliente_encontrado['cuit_cliente']}): ")
        nuevo_correo_input = input(f"Nuevo Correo ({cliente_encontrado['correo_cliente']}): ")

        if nueva_razonsocial_input:
            cliente_encontrado['razonsocial_cliente'] = nueva_razonsocial_input
        if nuevo_cuit_input:
            if any(c['cuit_cliente'] == nuevo_cuit_input and c['id_cliente'] != cliente_encontrado['id_cliente'] for c in clientes_registrados):
                print("Error: El nuevo CUIT ya pertenece a otro cliente y no se puede usar. El CUIT actual se mantuvo.")
            else:
                cliente_encontrado['cuit_cliente'] = nuevo_cuit_input
        if nuevo_correo_input:
            cliente_encontrado['correo_cliente'] = nuevo_correo_input
        
        print(f"Cliente (ID: {cliente_encontrado['id_cliente']}) modificado exitosamente.")
    else:
        print("Cliente no encontrado.")
    pausa_sistema()

def eliminar_cliente_existente(): # elimina un cliente del sistema
    print("\n--- Eliminar Cliente ---")
    if not clientes_registrados:
        print("No hay cliente para eliminar.")
        pausa_sistema()
        return

    identificador_cliente = input("Ingrese el ID o CUIT del cliente a eliminar: ")
    cliente_a_eliminar = buscar_cliente_por_id_o_cuit(identificador_cliente)

    if cliente_a_eliminar:
        confirmacion = input(f"¿Está seguro de eliminar a '{cliente_a_eliminar['razonsocial_cliente']}' (ID: {cliente_a_eliminar['id_cliente']})? (S/N): ").upper()
        if confirmacion == 'S':
            clientes_registrados.remove(cliente_a_eliminar)
            print("Cliente eliminado exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print("Cliente no encontrado.")
    pausa_sistema()

def submenu_gestionar_clientes():      # Maneja las opciones dentro del menú de Gestión de Clientes
    while True:
        # Aquí imprimimos el menú directamente
        print("\n--- Submenú Gestionar Clientes ---")
        print("1. Ver Clientes")
        print("2. Agregar Cliente")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")
        print("----------------------------------------------------------")
        opcion_clientes_elegida = input("Ingrese una opción: ") # Capturamos la opción aquí mismo

        if opcion_clientes_elegida == '1':
            ver_clientes_registrados()
        elif opcion_clientes_elegida == '2':
            agregar_nuevo_cliente()
        elif opcion_clientes_elegida == '3':
            modificar_cliente_existente()
        elif opcion_clientes_elegida == '4':
            eliminar_cliente_existente()
        elif opcion_clientes_elegida == '5':
            print("Volviendo al Menú Principal...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            pausa_sistema()

# --- Módulo de Gestión de Destinos y Reservas ---

def gestionar_destinos_y_reservas(): 
    global id_reserva
    print("\n--- Gestionar Destinos ---")
    print("Listado de destinos disponibles:")
    for sigla, info_destino in destinos_disponibles.items():
        print(f"°{sigla} ({info_destino['nombre']}) - ${info_destino['precio']:,.2f} ARS")

    destino_seleccionado_sigla = input("Ingrese siglas del destino a consultar precio (o 'SALIR' para volver): ").upper()

    if destino_seleccionado_sigla == 'SALIR':
        return

    if destino_seleccionado_sigla in destinos_disponibles:
        info_destino_elegido = destinos_disponibles[destino_seleccionado_sigla]
        preciovuelo_elegido = info_destino_elegido['precio']
        print(f"El costo de su viaje a {info_destino_elegido['nombre']} es de ${preciovuelo_elegido:,.2f} ARS")

        confirmacion_reserva = input("Ingrese Y para confirmar el boleto, ingrese N para cancelar la operación: ").upper()
        if confirmacion_reserva == 'Y':
            fecha_ida_reserva = input("Ingrese la fecha de ida para su reserva (DD-MM-AAAA): ")
            
            id_cliente_asociado_reserva = None
            if clientes_registrados:
                print("\nPara esta reserva, asocie un cliente existente:")
                ver_clientes_registrados()
                cliente_id_o_cuit_input = input("Ingrese el ID o CUIT del cliente para esta reserva (o deje en blanco para no asociar ahora): ")
                cliente_asociado_encontrado = buscar_cliente_por_id_o_cuit(cliente_id_o_cuit_input)
                if cliente_asociado_encontrado:
                    id_cliente_asociado_reserva = cliente_asociado_encontrado['id_cliente']
                    print(f"Reserva asociada al cliente: {cliente_asociado_encontrado['razonsocial_cliente']}.")
                else:
                    print("Cliente no encontrado o no se asoció cliente a la reserva en este momento.")
            else:
                print("No hay clientes registrados. Cree uno antes de asociar a la reserva.")

            id_reserva = obtener_siguiente_id(reservas_pendientes, 'id_reserva')
            nueva_reserva = {
                'id_reserva': id_reserva,
                'destino_sigla': destino_seleccionado_sigla,
                'destino_nombre': info_destino_elegido['nombre'],
                'preciovuelo': preciovuelo_elegido,
                'fecha_ida': fecha_ida_reserva,
                'id_cliente_asociado': id_cliente_asociado_reserva
            }
            reservas_pendientes.append(nueva_reserva)
            print("\n--- ¡Boleto reservado! ---")
            print("Por favor, diríjase a '3. Gestionar Ventas' para completar la compra.")
            print(f"Reserva ID: {nueva_reserva['id_reserva']} para: {nueva_reserva['destino_nombre']} el {nueva_reserva['fecha_ida']} por ${nueva_reserva['preciovuelo']:,.2f} ARS")
        elif confirmacion_reserva == 'N':
            print("Operación de reserva cancelada.")
        else:
            print("Respuesta no válida.")
    else:
        print("Destino no reconocido o no disponible.")
    pausa_sistema()

# --- Módulo de Gestión de Ventas ---

def procesar_reserva_pendiente():# Permite al usuario consultar destinos y crear nuevas reservas de vuelo
    global id_venta
    print("\n--- Procesar Reserva Pendiente ---")
    if not reservas_pendientes:
        print("No hay ninguna reserva pendiente para procesar.")
        print("Por favor, vaya a '2. Gestionar Destinos' para crear una reserva primero.")
        pausa_sistema()
        return

    print("\nReservas Pendientes:")
    for i, reserva in enumerate(reservas_pendientes):
        cliente_info_reserva = "Sin cliente asociado"
        if reserva['id_cliente_asociado']:
            cliente_relacionado = buscar_cliente_por_id_o_cuit(str(reserva['id_cliente_asociado']))
            if cliente_relacionado:
                cliente_info_reserva = f"Cliente: {cliente_relacionado['razonsocial_cliente']} (CUIT: {cliente_relacionado['cuit_cliente']})"
        print(f"{i+1}. ID Reserva: {reserva['id_reserva']}, Destino: {reserva['destino_nombre']}, Fecha Ida: {reserva['fecha_ida']}, Precio: ${reserva['preciovuelo']:,.2f} ARS. {cliente_info_reserva}")

    try:
        idx_reserva_elegida = int(input("Ingrese el NÚMERO de la reserva a procesar: ")) - 1
        if not (0 <= idx_reserva_elegida < len(reservas_pendientes)):
            print("Número de reserva inválido.")
            pausa_sistema()
            return
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        pausa_sistema()
        return

    reserva_a_procesar = reservas_pendientes[idx_reserva_elegida]

    cliente_para_venta = None
    if reserva_a_procesar['id_cliente_asociado']:
        cliente_para_venta = buscar_cliente_por_id_o_cuit(str(reserva_a_procesar['id_cliente_asociado']))
    
    if not cliente_para_venta:
        print("\nEsta reserva no tiene un cliente asociado válido. Debe asociar uno para completar la venta.")
        if input("¿Desea AGREGAR un nuevo cliente o SELECCIONAR uno existente ahora? (S/N): ").upper() == 'S':
            while True:
                print("\n1. Agregar un nuevo cliente")
                print("2. Seleccionar un cliente existente")
                sub_opcion_cliente_venta = input("Ingrese su opción: ")
                if sub_opcion_cliente_venta == '1':
                    agregar_nuevo_cliente()
                    if clientes_registrados:
                        cliente_para_venta = clientes_registrados[-1]
                        reserva_a_procesar['id_cliente_asociado'] = cliente_para_venta['id_cliente']
                        print(f"Reserva ahora asociada al nuevo cliente: {cliente_para_venta['razonsocial_cliente']}")
                    break
                elif sub_opcion_cliente_venta == '2':
                    ver_clientes_registrados()
                    id_o_cuit_cliente_asociar = input("Ingrese ID o CUIT del cliente a asociar: ")
                    cliente_seleccionado = buscar_cliente_por_id_o_cuit(id_o_cuit_cliente_asociar)
                    if cliente_seleccionado:
                        cliente_para_venta = cliente_seleccionado
                        reserva_a_procesar['id_cliente_asociado'] = cliente_para_venta['id_cliente']
                        print(f"Reserva ahora asociada al cliente: {cliente_para_venta['razonsocial_cliente']}")
                        break
                    else:
                        print("Cliente no encontrado.")
                else:
                    print("Opción no válida.")
        
        if not cliente_para_venta:
            print("No se pudo asociar un cliente a la reserva. Venta cancelada.")
            pausa_sistema()
            return

    print(f"\n--- Detalles de la Reserva a Procesar (ID: {reserva_a_procesar['id_reserva']}) ---")
    print(f"Cliente: {cliente_para_venta['razonsocial_cliente']} (CUIT: {cliente_para_venta['cuit_cliente']})")
    print(f"Destino: {reserva_a_procesar['destino_nombre']}")
    print(f"Fecha de Ida: {reserva_a_procesar['fecha_ida']}")
    print(f"Precio: ${reserva_a_procesar['preciovuelo']:,.2f} ARS")

    confirmacion_venta = input("\n¿Confirmar la venta de esta reserva? (S/N): ").upper()
    if confirmacion_venta == 'S':
        id_venta = obtener_siguiente_id(ventas_finalizadas, 'id_pasaje')
        
        venta_registrada_data = {
            'id_pasaje': id_venta,
            'id_cliente_asociado': cliente_para_venta['id_cliente'],
            'razonsocial_cliente': cliente_para_venta['razonsocial_cliente'],
            'cuit_cliente': cliente_para_venta['cuit_cliente'],
            'correo_cliente': cliente_para_venta['correo_cliente'],
            'destino': reserva_a_procesar['destino_nombre'],
            'precio': reserva_a_procesar['preciovuelo'],
            'fecha_venta': datetime.date.today().strftime("%d-%m-%Y"),
            'fecha_vuelo': reserva_a_procesar['fecha_ida']
        }
        ventas_finalizadas.append(venta_registrada_data)

        reservas_pendientes.pop(idx_reserva_elegida)

        print("\n--- ¡Venta de Reserva Procesada con Éxito! ---")
        print(f"ID de Venta: {venta_registrada_data['id_pasaje']}")
        print(f"Cliente: {venta_registrada_data['razonsocial_cliente']}")
        print(f"Destino: {venta_registrada_data['destino']}")
        print(f"Precio: ${venta_registrada_data['precio']:,.2f} ARS")
        print(f"Fecha de Venta: {venta_registrada_data['fecha_venta']}")
        print(f"Fecha de Vuelo: {venta_registrada_data['fecha_vuelo']}")
        print(f"Se enviará a su correo: {venta_registrada_data['correo_cliente']} el cupón de pago e indicaciones para finalizar la venta.")
    else:
        print("Procesamiento de reserva cancelado.")
    pausa_sistema()

def cancelar_reserva_pendiente():
    """Permite al usuario cancelar una reserva que aún no ha sido vendida."""
    print("\n--- Cancelar Reserva Pendiente ---")
    if not reservas_pendientes:
        print("No hay ninguna reserva pendiente para cancelar.")
        pausa_sistema()
        return

    print("\nReservas Pendientes:")
    for i, reserva in enumerate(reservas_pendientes):
        cliente_info_reserva = "Sin cliente asociado"
        if reserva['id_cliente_asociado']:
            cliente_relacionado = buscar_cliente_por_id_o_cuit(str(reserva['id_cliente_asociado']))
            if cliente_relacionado:
                cliente_info_reserva = f"Cliente: {cliente_relacionado['razonsocial_cliente']}"
        print(f"{i+1}. ID Reserva: {reserva['id_reserva']}, Destino: {reserva['destino_nombre']}, Fecha Ida: {reserva['fecha_ida']}, Precio: ${reserva['preciovuelo']:,.2f} ARS. {cliente_info_reserva}")

    try:
        idx_reserva_cancelar = int(input("Ingrese el NÚMERO de la reserva a cancelar: ")) - 1
        if not (0 <= idx_reserva_cancelar < len(reservas_pendientes)):
            print("Número de reserva inválido.")
            pausa_sistema()
            return
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        pausa_sistema()
        return

    reserva_a_cancelar = reservas_pendientes[idx_reserva_cancelar]
    
    confirmacion_cancelacion = input(f"¿Está seguro de cancelar la reserva ID {reserva_a_cancelar['id_reserva']} para {reserva_a_cancelar['destino_nombre']} ({reserva_a_cancelar['fecha_ida']})? (S/N): ").upper()
    if confirmacion_cancelacion == 'S':
        reservas_pendientes.pop(idx_reserva_cancelar)
        print("Reserva cancelada exitosamente. Derecho de cancelación de compra (Ley 24.240 de Defensa al Consumidor y en el Código Civil y Comercial de la Nación (Ley 26.994)).")
    else:
        print("Cancelación de reserva abortada.")
    pausa_sistema()

def submenu_gestionar_ventas():
    """Maneja las opciones dentro del menú de Gestión de Ventas."""
    while True:
        # Aquí imprimimos el menú directamente
        print("\n--- Submenú Gestionar Ventas ---")
        print("1. Procesar reserva pendiente")
        print("2. Cancelar reserva pendiente")
        print("3. Volver al Menú Principal")
        print("----------------------------------------------------------")
        opcion_ventas_elegida = input("Ingrese una opción: ") # Capturamos la opción aquí mismo

        if opcion_ventas_elegida == '1':
            procesar_reserva_pendiente()
        elif opcion_ventas_elegida == '2':
            cancelar_reserva_pendiente()
        elif opcion_ventas_elegida == '3':
            print("Volviendo al Menú Principal...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            pausa_sistema()

# --- Módulo de Consulta de Ventas ---

def consultar_ventas_finalizadas():
    """Muestra un listado de todas las ventas que han sido registradas."""
    print("\n--- Consultar Ventas ---")
    if not ventas_finalizadas:
        print("No hay ventas registradas aún en el sistema.")
        print("Por favor, procese una reserva en '3. Gestionar Ventas' para registrar una venta.")
    else:
        print("Listado de Ventas Registradas:")
        for venta in ventas_finalizadas:
            print(f"\n--- Detalles de Venta ID: {venta['id_pasaje']} ---")
            print(f"Cliente: {venta['razonsocial_cliente']} (CUIT: {venta['cuit_cliente']})")
            print(f"Destino: {venta['destino']}")
            print(f"Precio: ${venta['precio']:,.2f} ARS")
            print(f"Fecha de Venta: {venta['fecha_venta']}")
            print(f"Fecha de Vuelo: {venta['fecha_vuelo']}")
            print(f"Correo de Contacto: {venta['correo_cliente']}")
    pausa_sistema()

# --- Módulo de Botón de Arrepentimiento ---

def boton_arrepentimiento_venta(): #cancelar una venta ya finalizada, eliminándola del registro.
    print("\n--- Botón de Arrepentimiento ---")
    if not ventas_finalizadas:
        print("No hay ninguna venta registrada de la cual arrepentirse.")
        print("Para usar esta función, primero debe haber una venta procesada.")
        pausa_sistema()
        return

    print("\nVentas Registradas (para arrepentimiento):")
    for i, venta in enumerate(ventas_finalizadas):
        print(f"{i+1}. ID Venta: {venta['id_pasaje']}, Cliente: {venta['razonsocial_cliente']}, Destino: {venta['destino']}, Fecha Venta: {venta['fecha_venta']}")

    try:
        idx_venta_cancelar = int(input("Ingrese el NÚMERO de la venta a cancelar (arrepentirse): ")) - 1
        if not (0 <= idx_venta_cancelar < len(ventas_finalizadas)):
            print("Número de venta inválido.")
            pausa_sistema()
            return
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        pausa_sistema()
        return

    venta_a_cancelar = ventas_finalizadas[idx_venta_cancelar]
    
    print(f"La venta seleccionada (ID: {venta_a_cancelar['id_pasaje']}) es para {venta_a_cancelar['razonsocial_cliente']} con destino {venta_a_cancelar['destino']}.")
    confirmacion_arrepentimiento = input("¿Está seguro que desea cancelar esta venta? (S/N): ").upper()
    
    if confirmacion_arrepentimiento == 'S':
        ventas_finalizadas.pop(idx_venta_cancelar)
        print("¡Venta cancelada exitosamente! Los datos de la venta han sido eliminados.")
        print("Recuerde consultar las políticas de cancelación de vuelos.")
    elif confirmacion_arrepentimiento == 'N':
        print("Operación de arrepentimiento cancelada.")
    else:
        print("Respuesta no válida.")
    pausa_sistema()

# --- Función Principal del Programa ---

def main():
    """Función principal que ejecuta el sistema SkyRoute."""
    while True:
        # Menú Principal
        print("\n--- Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes ---")
        print("1. Gestionar Clientes")
        print("2. Gestionar Destinos")
        print("3. Gestionar Ventas")
        print("4. Consultar Ventas")
        print("5. Botón de Arrepentimiento")
        print("6. Salir")
        print("----------------------------------------------------------")
        opcion_principal_elegida = input("Ingrese una opción: ")

        if opcion_principal_elegida == '1':
            submenu_gestionar_clientes()
        elif opcion_principal_elegida == '2':
            gestionar_destinos_y_reservas()
        elif opcion_principal_elegida == '3':
            submenu_gestionar_ventas()
        elif opcion_principal_elegida == '4':
            consultar_ventas_finalizadas()
        elif opcion_principal_elegida == '5':
            boton_arrepentimiento_venta()
        elif opcion_principal_elegida == '6':
            print("Saliendo de SkyRoute - Sistema de Gestión de Pasajes. ¡Vuelva pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            pausa_sistema()

# Punto de entrada del programa
if __name__ == "__main__":
    main()
      
