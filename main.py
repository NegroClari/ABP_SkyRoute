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

# --- Funciones de Utilidad Comunes ---

def obtener_siguiente_id(lista_registros, clave_id):
    """
    Genera el siguiente ID único basado en el máximo ID existente
    en una lista de diccionarios.
    """
    if not lista_registros:
        return 1
    return max(registro.get(clave_id, 0) for registro in lista_registros) + 1

def pausa_sistema():
    """Detiene la ejecución hasta que el usuario presione Enter."""
    input("\nPresione Enter para continuar...")

def mostrar_menu_generico(titulo_menu, opciones_menu):
    """
    Presenta un menú con opciones y solicita la selección del usuario.

    Args:
        titulo_menu (str): El título que aparecerá en la parte superior del menú.
        opciones_menu (list): Una lista de cadenas, donde cada cadena es una opción del menú.

    Returns:
        str: La opción numérica ingresada por el usuario.
    """
    print(f"\n--- {titulo_menu} ---")
    for i, opcion_texto in enumerate(opciones_menu, 1):
        print(f"{i}. {opcion_texto}")
    print("----------------------------------------------------------")
    return input("Ingrese una opción: ")

# --- Módulo de Gestión de Clientes ---

def ver_clientes_registrados():
    """Muestra un listado detallado de todos los clientes en el sistema."""
    print("\n--- Ver Clientes ---")
    if not clientes_registrados:
        print("No hay clientes registrados en el sistema.")
    else:
        print("Listado de Clientes:")
        for cliente in clientes_registrados:
            print(f"ID: {cliente['id_cliente']}, Razón Social: {cliente['razonsocial_cliente']}, CUIT: {cliente['cuit_cliente']}, Correo: {cliente['correo_cliente']}")
    pausa_sistema()

def agregar_nuevo_cliente(): #Funcion para agregar clientes y guardartos luego en lista registro_clientes
    global id_cliente
    print("\n--- Agregar Cliente ---")
    razonsocial_cliente = input("Ingrese nombre/razón social del nuevo cliente: ")
    cuit_cliente= input("Ingrese CUIT del nuevo cliente: ")
    correo_cliente = input("Ingrese Correo de Contacto del nuevo cliente: ")

    if not razonsocial_cliente or not cuit_cliente or not correo_cliente:
        print("Error: DEBE COMPLETAR TODOS LOS CAMPOS.")
    else:
        # Validar si el CUIT ya existe
        if any(cuit['cuit_cliente'] == cuit_cliente for cuit in clientes_registrados): #analizo con un ciclo for dato por dato si el cuit ingresado existe en la lista en la posicion 'cuit_cliente'
            print("Error: Ya existe un cliente con el CUIT ingresado.")
            pausa_sistema()   #llamo funcion para que el cliente apriete enter para continuar y vuelve atras
            return

        id_cliente = obtener_siguiente_id(clientes_registrados, 'id_cliente') #Actualizo la variable global contador de id cliente 
        #creo un diccionario que guarde los datos de mi cliente
        nuevo_cliente = {
            'id_cliente': id_cliente,
            'razonsocial_cliente': razonsocial_cliente,
            'cuit_cliente': cuit_cliente,
            'correo_cliente': correo_cliente,
        }
        clientes_registrados.append(nuevo_cliente) #Agrego los datos en el diccionario nuevo cliente a la lista clientes_registrados
        print(f"Cliente '{razonsocial_cliente}' (ID: {id_cliente}) agregado exitosamente.") #muestra lo recien ingresado 
    pausa_sistema()

def buscar_cliente_por_id_o_cuit(identificador_busqueda):  #Encuentra un cliente por su ID  o por CUIT.
    if identificador_busqueda.isdigit(): # buscar por ID (solo si el identificador_busqueda es numérico)
        id_int = int(identificador_busqueda) #ingreso del id por teclado y lo convierte en entero
        for cliente in clientes_registrados: # recorre la lista n veces(cliente) en la lista clientes registrados
            if cliente['id_cliente'] == id_int:  #si en esa vuelta encuentra el mismo en la posicion de la lista id cliente
                return cliente    #lo muestra
    
    # 2. Si no se encontró por ID busca por CUIT 
    for cliente in clientes_registrados: #recorre la lista nveces( clientes) en la lista clientes registrados
        if cliente['cuit_cliente'] == identificador_busqueda: #busca la coincidencia de esa N vuelta en esa posicion de la lista
                                                              #que coincida con el cuit ingresado
            return cliente # lo muestra
            
    # 3. Si no se encontró ni por ID ni por CUIT, retornar None
    return None

def modificar_cliente_existente(): #Permite actualizar los datos de un cliente existente.
    print("\n--- Modificar Cliente ---")  
    if not clientes_registrados:  #verifica si la lista esta vacia
        print("No hay clientes para modificar. Agregue uno primero.")
        pausa_sistema()   #llamo la funcion para que regrese al menu anterior
        return 

    identificador_cliente = input("Ingrese el ID o CUIT del cliente a modificar: ")  #ingreso de datos por teclado del cliente que quiero modificar
    cliente_encontrado = buscar_cliente_por_id_o_cuit(identificador_cliente) #una vez ingresado lo envio a la funcion buscar cliente. La cual me
                                                                            #devuelve los datos del cliente. Guardo los datos en cliente encontrado

    if cliente_encontrado: #si lo encuentra muestra sus datos en cada posicion de la lista clientes registrados
        print(f"\nDatos actuales del cliente (ID: {cliente_encontrado['id_cliente']}):")
        print(f"Razón Social: {cliente_encontrado['razonsocial_cliente']}")
        print(f"CUIT: {cliente_encontrado['cuit_cliente']}")
        print(f"Correo: {cliente_encontrado['correo_cliente']}")
 #ingresar por teclado los nuevos datos de la modificacion. a cada dato lo indico en la posicion de la lista y con el diccionario que corresponde
        print("\nIngrese los nuevos datos (deje en blanco para mantener el actual):")
        nueva_razonsocial_input = input(f"Nueva Razón Social ({cliente_encontrado['razonsocial_cliente']}): ")
        nuevo_cuit_input = input(f"Nuevo CUIT ({cliente_encontrado['cuit_cliente']}): ")
        nuevo_correo_input = input(f"Nuevo Correo ({cliente_encontrado['correo_cliente']}): ")
#Si valida nuevo ingreso lo reemplaza en la posicion del cliente que queremos
        if nueva_razonsocial_input:
            cliente_encontrado['razonsocial_cliente'] = nueva_razonsocial_input
        
        # Validar y actualizar CUIT
        if nuevo_cuit_input:
            cuit_duplicado = False  #creo esta variable booleana para ccambiarla si el cuit ya existe
# Recorrer todos los clientes registrados de la lista para verificar si el CUIT es el mismo y si no es el cliente que estamos modificando
            for cliente_existente in clientes_registrados: 
                if cliente_existente['cuit_cliente'] == nuevo_cuit_input and \
                   cliente_existente['id_cliente'] != cliente_encontrado['id_cliente']:    # Esta condición verifica si el CUIT del cliente 
                                                                                            #que estamos revisando en esta iteración 
                                                                                            #(cliente_existente['cuit_cliente']) es igual 
                                                                                            # al nuevo CUIT que el usuario quiere asignar un (nuevo_cuit_input). y 
                                                                                            # verifica que un CUIT duplicado si lo encuentro en un cliente
                                                                                            #  diferente al que estoy intentando modificar ahora
                    cuit_duplicado = True  #si se cumplen las condiciones se cambia el valor de la variable booleana y sale
                    break

            if cuit_duplicado: #si cuit duplicado es TRUE
                print("Error: El nuevo CUIT ya pertenece a otro cliente y no se puede usar. El CUIT actual se mantuvo.")
            else:
                cliente_encontrado['cuit_cliente'] = nuevo_cuit_input  #Si sigue siendo False le da el valor del nuevo cuit ingresado
                                                                        #a la lista en la posicion corespondiente
        
        # Actualizar correo
        if nuevo_correo_input:
            cliente_encontrado['correo_cliente'] = nuevo_correo_input
           
        print(f"Cliente (ID: {cliente_encontrado['id_cliente']}) modificado exitosamente.")
     
    else: #si no encuentra el cliente que queremos modificar
        print("Cliente no encontrado.")
    
    pausa_sistema() # La pausa siempre va al final, sin importar el resultado
def eliminar_cliente_existente():
    """Elimina un cliente del sistema."""
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

def submenu_gestionar_clientes():
    """Maneja las opciones dentro del menú de Gestión de Clientes."""
    while True:
        opciones_clientes = [
            "Ver Clientes",
            "Agregar Cliente",
            "Modificar Cliente",
            "Eliminar Cliente",
            "Volver al Menú Principal"
        ]
        opcion_clientes_elegida = mostrar_menu_generico("Submenú Gestionar Clientes", opciones_clientes)

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
    """Permite al usuario consultar destinos y crear nuevas reservas de vuelo."""
    global id_reserva_counter
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
        print(f"El costo de su viaje a {info_destino_elegido['nombre']} es de ${preciovuelo_elegido} ARS")

        confirmacion_reserva = input("Ingrese Y para confirmar el boleto, ingrese N para cancelar la operación: ").upper()
        if confirmacion_reserva == 'Y':
            fecha_ida_reserva = input("Ingrese la fecha de ida para su reserva (DD-MM-AAAA): ")
            
            # Asociar cliente a la reserva
            id_cliente_asociado_reserva = None
            if clientes_registrados:
                print("\nPara esta reserva, asocie un cliente existente:")
                ver_clientes_registrados() # Muestra los clientes para que el usuario elija
                cliente_id_o_cuit_input = input("Ingrese el ID o CUIT del cliente para esta reserva (o deje en blanco para no asociar ahora): ")
                cliente_asociado_encontrado = buscar_cliente_por_id_o_cuit(cliente_id_o_cuit_input)
                if cliente_asociado_encontrado:
                    id_cliente_asociado_reserva = cliente_asociado_encontrado['id_cliente']
                    print(f"Reserva asociada al cliente: {cliente_asociado_encontrado['razonsocial_cliente']}.")
                else:
                    print("Cliente no encontrado o no se asoció cliente a la reserva en este momento.")
            else:
                print("No hay clientes registrados. Cree uno antes de asociar a la reserva.")

            id_reserva_counter = obtener_siguiente_id(reservas_pendientes, 'id_reserva')
            nueva_reserva = {
                'id_reserva': id_reserva_counter,
                'destino_sigla': destino_seleccionado_sigla,
                'destino_nombre': info_destino_elegido['nombre'],
                'preciovuelo': preciovuelo_elegido,
                'fecha_ida': fecha_ida_reserva,
                'id_cliente_asociado': id_cliente_asociado_reserva # Guarda el ID del cliente
            }
            reservas_pendientes.append(nueva_reserva)
            print("\n--- ¡Boleto reservado! ---")
            print("Por favor, diríjase a '3. Gestionar Ventas' para completar la compra.")
            print(f"Reserva ID: {nueva_reserva['id_reserva']} para: {nueva_reserva['destino_nombre']} el {nueva_reserva['fecha_ida']} por ${nueva_reserva['preciovuelo']} ARS")
        elif confirmacion_reserva == 'N':
            print("Operación de reserva cancelada.")
        else:
            print("Respuesta no válida.")
    else:
        print("Destino no reconocido o no disponible.")
    pausa_sistema()

# --- Módulo de Gestión de Ventas ---

def procesar_reserva_pendiente(): # Funcion que convierte una reserva pendiente en una venta finalizada.
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

    # Asegurarse de que la reserva tenga un cliente asociado antes de la venta
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
                    agregar_nuevo_cliente() # Llama a la función para agregar
                    if clientes_registrados: # Asume que el último agregado es el deseado
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
        
        if not cliente_para_venta: # Si después de los intentos, no hay cliente
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
        id_venta_counter = obtener_siguiente_id(ventas_finalizadas, 'id_pasaje')
        
        venta_registrada_data = {
            'id_pasaje': id_venta_counter,
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

        # Eliminar la reserva de la lista de pendientes ya que se vendió
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
        opciones_ventas = [
            "Procesar reserva pendiente",
            "Cancelar reserva pendiente",
            "Volver al Menú Principal"
        ]
        opcion_ventas_elegida = mostrar_menu_generico("Submenú Gestionar Ventas", opciones_ventas)

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

def boton_arrepentimiento_venta():
    """Permite cancelar una venta ya finalizada, eliminándola del registro."""
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
        opciones_menu_principal = [
            "Gestionar Clientes",
            "Gestionar Destinos",
            "Gestionar Ventas",
            "Consultar Ventas",
            "Botón de Arrepentimiento",
            "Salir"
        ]
        opcion_principal_elegida = mostrar_menu_generico("Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes", opciones_menu_principal)

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
