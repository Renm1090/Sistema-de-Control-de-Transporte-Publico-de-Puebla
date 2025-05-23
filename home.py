import customtkinter as ctk
from tkinter import messagebox
from customtkinter import StringVar
from PIL import Image
import tkintermapview
from main import ClimaTiempoReal, API_KEY
import os
import random
import sys
from datetime import datetime
from main import Rutas
from main import Paradas
Rutas.cargar_rutas()

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def ventana2():
    # --- Colores y dimensiones del menú ---
    menu_bar_color = "#23293a"
    accent_color = "#17b978"
    menu_text_color = "#fff"
    initial_menu_width = 48
    expanded_menu_width = 200

    root2 = ctk.CTk()
    root2.title("INICIO")
    root2.geometry("500x600")
    root2.resizable(False, False)

    # --- Fondo  ---
    fondo3_path = resource_path("inicio.jpg")
    fondo3 = Image.open(fondo3_path).resize((500, 600), Image.LANCZOS)
    fondo3_img = ctk.CTkImage(fondo3, size=(500, 600))
    fondo3_label = ctk.CTkLabel(master=root2, image=fondo3_img, text="")
    fondo3_label.place(relwidth=1, relheight=1)
    fondo3_label.image = fondo3_img

    # --- Frame principal de páginas ---
    page_frame = ctk.CTkFrame(
        master=root2,
        fg_color="#303741",
        border_color=accent_color,
        border_width=3,
        corner_radius=20
    )
    page_frame.place(relwidth=1.0, relheight=1.0, x=initial_menu_width+10)

    # --- Menú lateral ---
    menu_bar_frame = ctk.CTkFrame(
        master=root2,
        fg_color=menu_bar_color,
        border_width=2,
        border_color=accent_color,
        width=initial_menu_width,
        corner_radius=12
    )
    menu_bar_frame.place(x=3, y=4, relheight=1)

    # --- Carga de iconos ---
    def cargar_icono(path):
        return ctk.CTkImage(Image.open(resource_path(path)).resize((16,16), Image.LANCZOS))

    taglet_ctk = cargar_icono("barra-de-menus.png")
    close_ctk = cargar_icono("equis.png")
    home_ctk = cargar_icono("hogar.png")
    route_ctk = cargar_icono("Rutas.png")
    climate_ctk = cargar_icono("clima.png")
    stops_ctk = cargar_icono("camion.png")
    logout_ctk = cargar_icono("cerrar-sesion.png")
    traficc_ctk = cargar_icono("cono-de-trafico.png")

    # --- Definición de páginas ---
    def home_page():
        for frame in page_frame.winfo_children():
            frame.destroy()

        # Fondo principal con azul vibrante
        home_page_fm = ctk.CTkFrame(master=page_frame, fg_color=menu_bar_color)
        home_page_fm.pack(fill='both', expand=True)

        # Sombra del frame central (simulada)
        shadow_fm = ctk.CTkFrame(
            master=home_page_fm, fg_color="#24ba8b", corner_radius=30
        )
        shadow_fm.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.47, relheight=0.47)

        # Frame central blanco con azul acento
        center_fm = ctk.CTkFrame(
            master=home_page_fm, 
            fg_color="white", 
            corner_radius=26, 
            border_color=accent_color, 
            border_width=4
        )
        center_fm.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.45, relheight=0.45)

        
        circle_logo = ctk.CTkFrame(
            master=center_fm,
            fg_color=accent_color,
            width=80, height=80,
            corner_radius=40,
            border_color="#1976d2",
            border_width=1
        )
        circle_logo.pack(pady=(22, 8))
        circle_logo.pack_propagate(False)  
        logo = ctk.CTkLabel(
            master=circle_logo,
            text="👋",
            font=("Arial", 38),
            text_color="white",
            fg_color="transparent"
        )
        logo.pack(expand=True, fill='both')

        

        titulo = ctk.CTkLabel(
            master=center_fm,
            text="¡Bienvenido!",
            font=("Arial", 22, "bold"),
            text_color=accent_color,
            fg_color="transparent"
        )
        titulo.pack(pady=(0, 8))

        # Descripción 
        desc = ctk.CTkLabel(
            master=center_fm,
            text="Gracias por usar la app.\nAquí podrás consultar el tráfico,\nel clima y más.",
            font=("Arial", 13),
            text_color="#444",
            fg_color="transparent"
        )
        desc.pack(pady=(0, 12))

        # Frase motivadora
        frases = [
            "¡Que tengas un excelente día! 🚀",
            "Hoy es un buen día para viajar tranquilo.",
            "Recuerda: la información es poder. 🙌",
            "Consulta el tráfico y evita contratiempos.",
            "¡Tu ciudad, tu ritmo! 😊"
        ]
        motiv = ctk.CTkLabel(
            master=center_fm,
            text=random.choice(frases),
            font=("Arial", 11, "italic"),
            text_color="#3f7cac",
            fg_color="transparent"
        )
        motiv.pack(pady=(0, 10))

        btn1 = ctk.CTkButton(
            master=center_fm, 
            text="🚦 Estado del Tráfico", 
            width=170, 
            fg_color=accent_color, 
            hover_color="#145a32", 
            font=("Arial", 13, "bold"),
            text_color="white",
            corner_radius=18,
            command=traficc_page
        )
        btn1.pack(pady=2)


        # Línea decorativa inferior
        decor = ctk.CTkLabel(
            master=center_fm,
            text="─────────────",
            text_color="#0b6781",
            font=("Arial", 13),
            fg_color="transparent"
        )
        decor.pack(pady=(10, 0))

    def route_page():
        for frame in page_frame.winfo_children():
            frame.destroy()

        route_page_fm = ctk.CTkFrame(
            master=page_frame,
            fg_color='#283655',
            border_color=accent_color,
            border_width=2,
            corner_radius=16)
        route_page_fm.place(relx=0.45, rely=0.5, anchor="center", relwidth=0.89, relheight=0.80)
        rutas_nombres = [f'{ruta.ruta}: {ruta.nombre}' for ruta in Rutas.Lista_rutas]

        title = ctk.CTkLabel(
            master=route_page_fm,
            text="Consulta Rutas",
            font=("Arial Black", 15, "bold"),
            text_color=accent_color,
            fg_color="transparent"
        )
        title.pack(pady=(8, 6))

        selector_fm = ctk.CTkFrame(route_page_fm, fg_color="transparent")
        selector_fm.pack(pady=(2, 0))
        ctk.CTkLabel(
            master=selector_fm,
            text="Selecciona una ruta:",
            font=("Arial", 9, "bold"),
            text_color=accent_color,
            fg_color="transparent"
        ).pack(side="left", padx=(0, 2))

        ruta_var = ctk.StringVar(master=route_page_fm, value=rutas_nombres[0])
        selector = ctk.CTkOptionMenu(
            master=selector_fm,
            variable=ruta_var,
            values=rutas_nombres,
            fg_color=accent_color,
            button_color=menu_bar_color,
            text_color="#222831",
            dropdown_fg_color=menu_bar_color,
            dropdown_text_color="#fff",
            font=("Arial", 9, "bold"),
            width=70
        )
        selector.pack(side="left")

        lb_framem = ctk.CTkFrame(
            master=route_page_fm,
            fg_color="#23293a",
            border_color=accent_color,
            border_width=2,
            corner_radius=8,
            width=350,
            height=200
        )
        lb_framem.pack(pady=5, padx=7)

        lb_ruta = ctk.CTkLabel(
            master=lb_framem,
            text='',
            text_color="#fff",
            font=("Arial", 18, "bold"),
            fg_color="transparent",
            justify="center",
            width=340,       
            height=180,     
            anchor='center',
            wraplength=340,
        )
        lb_ruta.pack(expand=True, fill="both")

        # --- FUNCIÓN INTERNA PARA MOSTRAR LA RUTA SELECCIONADA ---
        def mostrar_ruta(nombre_seleccionado):
            for ruta in Rutas.Lista_rutas:
                nombre_compuesto = f"{ruta.ruta}: {ruta.nombre}"
                if nombre_compuesto == nombre_seleccionado:
                    lb_ruta.configure(
                        text=f"Ruta {ruta.ruta}: {ruta.nombre}\n"
                            f"Horario: {ruta.horario}\n"
                            f"Días: {ruta.dias}\n"
                            f"Tiempo: {ruta.tiempo} min\n"
                            f"Estaciones: {ruta.estaciones}\n"
                            f"Origen: {ruta.origen}\n"
                            f"Destino: {ruta.destino}\n"
                            f"Precio: ${ruta.precio}\n"
                            f"Distancia: {ruta.distancia} km\n"
                    )
                    break

        # callback para menú selector
        def on_selector_change(*args):
            mostrar_ruta(ruta_var.get())

        # Conectar el cambio de variable al callback
        ruta_var.trace_add('write', on_selector_change)

        # Mostrar la ruta inicial
        mostrar_ruta(rutas_nombres[0])

        route_page_fm.pack(fill='both', expand=True)

    def climate_page():
        for widget in page_frame.winfo_children():
            widget.destroy()

        climate_page_fm = ctk.CTkFrame(
            master=page_frame,
            fg_color="#283655",
            border_color=accent_color,
            border_width=2,
            corner_radius=16
        )
        climate_page_fm.place(relx=0.45, rely=0.5, anchor="center", relwidth=0.89, relheight=0.80)

        ciudad_var = ctk.StringVar(value='Puebla')

        def actualizar_clima():
            clima = ClimaTiempoReal(ciudad_var.get(), API_KEY)
            exito = clima.obtener_clima()
            texto = clima.mostrar_clima() if exito else "No se pudo obtener el clima"
            lb_clima.configure(text=texto)

        titulo = ctk.CTkLabel(
            master=climate_page_fm,
            text="Consulta el Clima",
            font=("Arial Black", 15, "bold"),
            text_color=accent_color,
            fg_color="transparent"
        )
        titulo.pack(pady=(8, 6))

        entry_ciudad = ctk.CTkEntry(
            master=climate_page_fm,
            textvariable=ciudad_var,
            font=("Arial", 11, "bold"),
            border_width=2,
            border_color=accent_color,
            fg_color="#fff",
            text_color="#283655"
        )
        entry_ciudad.pack(pady=(8, 10), padx=10)

        # Frame con borde para el label de clima
        lb_frame = ctk.CTkFrame(
            master=climate_page_fm,
            fg_color="#23293a",
            border_color=accent_color,
            border_width=2,
            corner_radius=8,
        )
        lb_frame.pack(pady=4, padx=7)

        lb_clima = ctk.CTkLabel(
            master=lb_frame,
            text="",
            text_color="#fff",
            font=("Arial", 11, "bold"),
            fg_color="transparent",
            justify="center",
            width=160,
            height=45,
            anchor="center",
            wraplength=160
        )
        lb_clima.pack(expand=True, fill="both")

        btn_actualizar = ctk.CTkButton(
            master=climate_page_fm,
            text="Actualizar Clima",
            command=actualizar_clima,
            font=("Arial Black", 11, "bold"),
            fg_color=accent_color,
            hover_color="#145a32",
            text_color="#fff",
            corner_radius=8,
            height=22
        )
        btn_actualizar.pack(pady=(0, 8), padx=9)

        actualizar_clima()

    def stops_page():
        for frame in page_frame.winfo_children():
            frame.destroy()

        panel_fm = ctk.CTkFrame(
            master=page_frame,
            fg_color="#222831",
            border_color=accent_color,
            border_width=2,
            corner_radius=10
        )
        panel_fm.place(relx=0.45, rely=0.5, anchor="center", relwidth=0.89, relheight=0.80)

        rutas_nombres = [f'{ruta.ruta}: {ruta.nombre}' for ruta in Rutas.Lista_rutas]

        icon_path = resource_path("camion.png")
        title_icon = ctk.CTkImage(Image.open(icon_path).resize((14, 14)))
        titulo_fm = ctk.CTkFrame(panel_fm, fg_color="transparent")
        titulo_fm.pack(pady=3)
        ctk.CTkLabel(
            master=titulo_fm,
            image=title_icon,
            text="", width=15
        ).pack(side="left", padx=(0, 4))
        ctk.CTkLabel(
            master=titulo_fm,
            text="Paradas y Rutas",
            font=("Arial Black", 10, "bold"),
            text_color=accent_color,
            fg_color="transparent"
        ).pack(side="left")

        if not rutas_nombres:
            ctk.CTkLabel(
                master=panel_fm,
                text="No hay rutas cargadas.",
                text_color="#e74c3c",
                font=("Arial", 10, "bold"),
                fg_color="transparent"
            ).pack(pady=7)
            return

        selector_fm = ctk.CTkFrame(panel_fm, fg_color="transparent")
        selector_fm.pack(pady=(2, 0))
        ctk.CTkLabel(
            master=selector_fm,
            text="Selecciona una ruta:",
            font=("Arial", 9, "bold"),
            text_color=accent_color,
            fg_color="transparent"
        ).pack(side="left", padx=(0, 2))

        ruta_var = ctk.StringVar(master=panel_fm, value=rutas_nombres[0])
        selector = ctk.CTkOptionMenu(
            master=selector_fm,
            variable=ruta_var,
            values=rutas_nombres,
            fg_color=accent_color,
            button_color=menu_bar_color,
            text_color="#222831",
            dropdown_fg_color=menu_bar_color,
            dropdown_text_color="#fff",
            font=("Arial", 9, "bold"),
            width=70
        )
        selector.pack(side="left")

        mapa_fm = ctk.CTkFrame(panel_fm, fg_color="#364152", border_color=accent_color, border_width=2, corner_radius=6)
        mapa_fm.pack(padx=1, pady=(3, 1), expand=True, fill="both")
        mapa_widget = tkintermapview.TkinterMapView(master=mapa_fm, width=120, height=80, corner_radius=4)
        mapa_widget.pack(padx=1, pady=1, expand=True, fill="both")

        markers = []
        route_path = [None]

        def mostrar_en_mapa(nombre_seleccionado):
            for marker in markers:
                marker.delete()
            markers.clear()
            if route_path[0] is not None:
                route_path[0].delete()
                route_path[0] = None
            idx = rutas_nombres.index(nombre_seleccionado)
            ruta = Rutas.Lista_rutas[idx]
            coords = []
            for parada in ruta.paradas:
                nombre, (lat, lon) = parada
                marker = mapa_widget.set_marker(lat, lon, text=nombre)
                markers.append(marker)
                coords.append((lat, lon))
            if coords:
                mapa_widget.set_position(*coords[0])
                mapa_widget.set_zoom(13)
                if len(coords) > 1:
                    route_path[0] = mapa_widget.set_path(coords, color=accent_color, width=1)

        selector.configure(command=mostrar_en_mapa)
        mostrar_en_mapa(rutas_nombres[0])

    def traficc_page():
        for frame in page_frame.winfo_children():
            frame.destroy()

        traficc_page_fm = ctk.CTkFrame(
            master=page_frame,
            fg_color="#283655",
            border_color=accent_color,
            border_width=2,
            corner_radius=16
        )
        traficc_page_fm.place(relx=0.45, rely=0.5, anchor="center", relwidth=0.89, relheight=0.80)

        titulo = ctk.CTkLabel(
            master=traficc_page_fm,
            text="Consulta de Tráfico",
            font=("Arial", 15, "bold"),
            text_color=accent_color,
            fg_color="transparent"
        )
        titulo.pack(pady=(10, 15))

        # Verifica si hay rutas cargadas
        if not Rutas.Lista_rutas:
            messagebox.showinfo("Info", "No hay rutas cargadas.\nVerifique que el archivo rutas.json exista.")
            return

        seleccion1 = ctk.CTkLabel(
            master=traficc_page_fm,
            text="Seleccionar Ruta:",
            font=("Arial", 11, "bold"),
            bg_color="transparent"
        )
        seleccion1.pack(pady=5)

        # Variables para los OptionMenus
        seleccion_ruta = ctk.StringVar(value=Rutas.Lista_rutas[0].ruta)
        seleccion_origen = ctk.StringVar()
        seleccion_destino = ctk.StringVar()

        opciones_rutas = [ruta.ruta for ruta in Rutas.Lista_rutas]
        menu_rutas = ctk.CTkOptionMenu(
            master=traficc_page_fm,
            variable=seleccion_ruta,
            values=opciones_rutas
        )
        menu_rutas.pack(pady=5)

        # Obtener la lista de paradas inicial según la ruta seleccionada
        def get_paradas_por_ruta(ruta_nombre):
            ruta = next((r for r in Rutas.Lista_rutas if r.ruta == ruta_nombre), None)
            return [p[0] for p in ruta.paradas] if ruta and ruta.paradas else []

        paradas_init = get_paradas_por_ruta(seleccion_ruta.get())
        if paradas_init:
            seleccion_origen.set(paradas_init[0])
            seleccion_destino.set(paradas_init[-1])
        else:
            seleccion_origen.set("")
            seleccion_destino.set("")

        menu_origen = ctk.CTkOptionMenu(
            master=traficc_page_fm,
            variable=seleccion_origen,
            values=paradas_init
        )
        menu_origen.pack(pady=5)

        menu_destino = ctk.CTkOptionMenu(
            master=traficc_page_fm,
            variable=seleccion_destino,
            values=paradas_init
        )
        menu_destino.pack(pady=5)

        # Actualizar paradas al cambiar la ruta seleccionada
        def actualizar_paradas(*args):
            paradas = get_paradas_por_ruta(seleccion_ruta.get())
            menu_origen.configure(values=paradas)
            menu_destino.configure(values=paradas)
            if paradas:
                seleccion_origen.set(paradas[0])
                seleccion_destino.set(paradas[-1])
            else:
                seleccion_origen.set("")
                seleccion_destino.set("")

        seleccion_ruta.trace_add("write", actualizar_paradas)

        # Resultado en Textbox
        resultado_lb = ctk.CTkTextbox(
            master=traficc_page_fm,
            font=("Arial", 11),
            width=410,
            height=200,
            wrap="word",
            activate_scrollbars=True
        )
        resultado_lb.pack(pady=10)

        def mostrar_trafico():
            try:
                ruta = next((r for r in Rutas.Lista_rutas if r.ruta == seleccion_ruta.get()), None)
                if not ruta or not ruta.paradas:
                    messagebox.showerror("Error", "Ruta no válida o sin paradas.")
                    return

                origen = seleccion_origen.get()
                destino = seleccion_destino.get()
                if not origen or not destino:
                    messagebox.showerror("Error", "Debes seleccionar una parada de origen y una de destino.")
                    return

                nombres_paradas = [p[0] for p in ruta.paradas]
                if origen not in nombres_paradas or destino not in nombres_paradas:
                    messagebox.showerror("Error", "Paradas no válidas para esta ruta.")
                    return

                idx_origen = nombres_paradas.index(origen)
                idx_destino = nombres_paradas.index(destino)

                if idx_origen == idx_destino:
                    messagebox.showwarning("Advertencia", "El origen y el destino son la misma parada.")
                    return

                tramo = nombres_paradas[min(idx_origen, idx_destino):max(idx_origen, idx_destino)+1]
                if idx_origen > idx_destino:
                    tramo = tramo[::-1]

                tiempo_tramo_seleccionado = 0
                distancia_tramo_seleccionado = 0

                # Solo calcular si hay paradas válidas
                if ruta.paradas and len(ruta.paradas) >= 2:
                    try:
                        ruta_paradas = Paradas(ruta.paradas)
                        info_completa, _ = ruta_paradas.distancia_y_tiempo()

                        # Encontrar los tramos específicos del recorrido
                        idx_min = min(idx_origen, idx_destino)
                        idx_max = max(idx_origen, idx_destino)

                        for i in range(idx_min, idx_max):
                            if i < len(info_completa):
                                tiempo_tramo_seleccionado += info_completa[i]['tiempo']
                                distancia_tramo_seleccionado += info_completa[i]['distancia']
                    except Exception as e:
                        print(f"Error calculando tramos: {e}")
                        tiempo_tramo_seleccionado = 15.0  # 15 minutos por defecto
                        distancia_tramo_seleccionado = 5.0  # 5 km por defecto

                hora_actual = datetime.now().hour
                trafico_alto = (7 <= hora_actual <= 9) or (17 <= hora_actual <= 19)

                # Obtener clima actual
                ciudad = ruta.origen
                clima = ClimaTiempoReal(ciudad, API_KEY)
                descripcion = "despejado"
                temperatura = "N/A"
                humedad = "N/A"

                try:
                    if clima.obtener_clima():
                        descripcion = clima.datos_clima["current"]["condition"]["text"].lower()
                        temperatura = clima.datos_clima["current"]["temp_c"]
                        humedad = clima.datos_clima["current"]["humidity"]
                except Exception as e:
                    print(f"Error obteniendo clima: {e}")

                # Ajustar tiempo estimado
                tiempo_base_str = str(ruta.tiempo).replace(' min', '').replace(' minutos', '').replace('min', '').strip()
                try:
                    tiempo_base = float(tiempo_base_str)
                except:
                    tiempo_base = tiempo_tramo_seleccionado if tiempo_tramo_seleccionado > 0 else 20.0

                retraso_clima = 1.0
                retraso_trafico = 1.0

                if any(palabra in descripcion for palabra in ["rain", "lluvia", "storm", "tormenta", "shower"]):
                    retraso_clima = 1.2  # 20% más tiempo

                if trafico_alto:
                    retraso_trafico = 1.3  # 30% más tiempo en horas pico

                # Calcular tiempo ajustado para el tramo específico
                tiempo_final = max(tiempo_tramo_seleccionado, 5.0)  # Mínimo 5 minutos
                tiempo_tramo_ajustado = round(tiempo_final * retraso_clima * retraso_trafico, 1)

                # Calcular hora estimada de llegada
                hora_actual_dt = datetime.now()
                minutos_adicionales = int(tiempo_tramo_ajustado)
                horas_adicionales = minutos_adicionales // 60
                minutos_restantes = minutos_adicionales % 60

                hora_llegada_estimada = hora_actual_dt.replace(second=0, microsecond=0)
                hora_llegada_estimada = hora_llegada_estimada.replace(
                    hour=(hora_llegada_estimada.hour + horas_adicionales) % 24,
                    minute=(hora_llegada_estimada.minute + minutos_restantes) % 60
                )

                mensaje = f"🚌 Ruta {ruta.ruta} - {ruta.nombre}\n"
                mensaje += f"🕒 Hora actual: {datetime.now().strftime('%H:%M')}\n"
                mensaje += f"🕐 Llegada estimada: {hora_llegada_estimada.strftime('%H:%M')}\n"
                mensaje += f"💰 Precio: ${ruta.precio}\n"
                mensaje += f"☁️ Clima: {descripcion.title()} | 🌡️ {temperatura}°C | 💧 {humedad}%\n\n"

                mensaje += f"📏 Distancia del tramo: {round(distancia_tramo_seleccionado, 2)} km\n"
                mensaje += f"⏱️ Tiempo base del tramo: {round(tiempo_final, 1)} min\n"
                mensaje += f"⏱️ Tiempo ajustado: {tiempo_tramo_ajustado} min\n"
                if retraso_clima > 1.0:
                    mensaje += f"🌧️ Retraso por clima: +{round((retraso_clima - 1) * 100, 0)}%\n"
                if retraso_trafico > 1.0:
                    mensaje += f"🚦 Retraso por tráfico: +{round((retraso_trafico - 1) * 100, 0)}%\n"
                mensaje += f"\n🚦 Tramo seleccionado: {origen} ➡ {destino}\n"
                mensaje += f"🚏 Número de paradas: {len(tramo)}\n\n"
                mensaje += "🛑 Estado del tráfico por parada:\n\n"

                # Simplificar el estado de tráfico
                for i, parada in enumerate(tramo):
                    estado_trafico = "Fluido"
                    emoji_trafico = "✅"

                    if trafico_alto:
                        if i % 2 == 0:
                            estado_trafico = "Tráfico Alto"
                            emoji_trafico = "🚨"
                        else:
                            estado_trafico = "Tráfico Moderado"
                            emoji_trafico = "🟡"

                    mensaje += f"{emoji_trafico} {parada} - {estado_trafico}\n"

                mensaje += f"\n📍 Recorrido del tramo:\n"
                mensaje += f"🚩 Origen: {origen}\n"

                # Mostrar paradas intermedias si las hay
                paradas_intermedias = tramo[1:-1] if len(tramo) > 2 else []
                if paradas_intermedias:
                    mensaje += "🚏 Paradas intermedias:\n"
                    for parada in paradas_intermedias:
                        mensaje += f"   • {parada}\n"

                mensaje += f"🏁 Destino: {destino}\n\n"

                # Información adicional
                if len(tramo) > 2:
                    mensaje += f"ℹ️ Este recorrido incluye {len(tramo)-2} paradas intermedias\n"
                mensaje += f"🚌 Velocidad promedio estimada: 40 km/h\n"
                if trafico_alto:
                    mensaje += f"⚠️ Hora pico detectada - Se recomienda considerar tiempo extra\n"

                resultado_lb.delete("0.0", "end")
                resultado_lb.insert("0.0", mensaje)
            except Exception as e:
                messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

        # Botón para consultar tráfico
        btn_consultar = ctk.CTkButton(
            master=traficc_page_fm,
            text="🚦 Consultar Tráfico",
            command=mostrar_trafico
        )
        btn_consultar.pack(pady=10)
                
    


    # --- Switch indicador ---
    def switch_indiacation(indicator_lb, page_func):
        home_indicator_frame.configure(fg_color=menu_bar_color)
        route_indicator_frame.configure(fg_color=menu_bar_color)
        climate_indicator_frame.configure(fg_color=menu_bar_color)
        stops_indicator_frame.configure(fg_color=menu_bar_color)
        traficc_indicator_frame.configure(fg_color=menu_bar_color)
        logout_indicator_frame.configure(fg_color=menu_bar_color)
        indicator_lb.configure(fg_color=accent_color)
        page_func()

    # --- Expand/collapse menú ---
    def expand_menu():
        menu_bar_frame.place_configure(width=expanded_menu_width)
        tagle_icon_btn.configure(image=close_ctk, command=fold_menu)
        home_page_lb.grid(row=1, column=2, padx=(0,0), pady=(0,12), sticky="w")
        route_page_lb.grid(row=2, column=2, padx=(0,0), pady=(0,12), sticky="w")
        climate_page_lb.grid(row=3, column=2, padx=(0,0), pady=(0,12), sticky="w")
        stops_page_lb.grid(row=4, column=2, padx=(0,0), pady=(0,12), sticky="w")
        traficc_page_lb.grid(row=5, column=2, padx=(0,0), pady=(0,12), sticky="w")
        logout_page_lb.grid(row=6, column=2, padx=(0,0), pady=(0,12), sticky="w")


    def fold_menu():
        menu_bar_frame.place_configure(width=85)
        tagle_icon_btn.configure(image=taglet_ctk, command=expand_menu)
        home_page_lb.grid_remove()
        route_page_lb.grid_remove()
        climate_page_lb.grid_remove()
        stops_page_lb.grid_remove()
        traficc_page_lb.grid_remove()
        logout_page_lb.grid_remove()

    def logout():
        root2.destroy()
        


    # --- Botones e indicadores --- (compactos)
    row = 0
    btn_height = 48
    btn_width = initial_menu_width-4

    tagle_icon_btn = ctk.CTkButton(menu_bar_frame, image=taglet_ctk, text="", height=btn_height, width=btn_width,
                                   fg_color=menu_bar_color, hover_color="#145a32", command=expand_menu)
    tagle_icon_btn.grid(row=row, column=1, padx=(0,0), pady=(20,12), sticky="w")
    row += 1

    home_icon_btn = ctk.CTkButton(menu_bar_frame, image=home_ctk, text="", height=btn_height, width=btn_width,
                                  fg_color=menu_bar_color, hover_color="#145a32",
                                  command=lambda: switch_indiacation(home_indicator_frame, home_page))
    home_icon_btn.grid(row=row, column=1, padx=(0,0), pady=(0,12), sticky="w")
    home_indicator_frame = ctk.CTkFrame(menu_bar_frame, fg_color=accent_color, height=btn_height, width=5)
    home_indicator_frame.grid(row=row, column=0, padx=(0,0), pady=(0,12), sticky="nsw")
    home_page_lb = ctk.CTkLabel(menu_bar_frame, text="Inicio", text_color=menu_text_color, font=("Arial", 12, "bold"), width=65, anchor="w")
    row += 1

    route_icon_btn = ctk.CTkButton(menu_bar_frame, image=route_ctk, text="", height=btn_height, width=btn_width,
                                   fg_color=menu_bar_color, hover_color="#f6c90e",
                                   command=lambda: switch_indiacation(route_indicator_frame, route_page))
    route_icon_btn.grid(row=row, column=1, padx=(0,0), pady=(0,12), sticky="w")
    route_indicator_frame = ctk.CTkFrame(menu_bar_frame, fg_color=menu_bar_color, height=btn_height, width=5)
    route_indicator_frame.grid(row=row, column=0, padx=(0,0), pady=(0,12), sticky="nsw")
    route_page_lb = ctk.CTkLabel(menu_bar_frame, text="Rutas", text_color=menu_text_color, font=("Arial", 12, "bold"), width=65, anchor="w")
    row += 1

    climate_icon_btn = ctk.CTkButton(menu_bar_frame, image=climate_ctk, text="", height=btn_height, width=btn_width,
                                     fg_color=menu_bar_color, hover_color="#145a32",
                                     command=lambda: switch_indiacation(climate_indicator_frame, climate_page))
    climate_icon_btn.grid(row=row, column=1, padx=(0,0), pady=(0,12), sticky="w")
    climate_indicator_frame = ctk.CTkFrame(menu_bar_frame, fg_color=menu_bar_color, height=btn_height, width=5)
    climate_indicator_frame.grid(row=row, column=0, padx=(0,0), pady=(0,12), sticky="nsw")
    climate_page_lb = ctk.CTkLabel(menu_bar_frame, text="Clima", text_color=menu_text_color, font=("Arial", 12, "bold"), width=65, anchor="w")
    row += 1

    stops_icon_btn = ctk.CTkButton(menu_bar_frame, image=stops_ctk, text="", height=btn_height, width=btn_width,
                                   fg_color=menu_bar_color, hover_color="#145a32",
                                   command=lambda: switch_indiacation(stops_indicator_frame, stops_page))
    stops_icon_btn.grid(row=row, column=1, padx=(0,0), pady=(0,12), sticky="w")
    stops_indicator_frame = ctk.CTkFrame(menu_bar_frame, fg_color=menu_bar_color, height=btn_height, width=5)
    stops_indicator_frame.grid(row=row, column=0, padx=(0,0), pady=(0,12), sticky="nsw")
    stops_page_lb = ctk.CTkLabel(menu_bar_frame, text="Paradas\nDistancias", text_color=menu_text_color, font=("Arial", 12, "bold"), width=65, anchor="w")
    row += 1

    traficc_icon_btn = ctk.CTkButton(menu_bar_frame, image=traficc_ctk, text="", height=btn_height, width=btn_width,
                                     fg_color=menu_bar_color, hover_color="#145a32", command= lambda: switch_indiacation(traficc_indicator_frame, traficc_page))
    traficc_icon_btn.grid(row=row, column=1, padx=(0,0), pady=(0,12), sticky="w")
    traficc_indicator_frame = ctk.CTkFrame(menu_bar_frame, fg_color=menu_bar_color, height=btn_height, width=5)
    traficc_indicator_frame.grid(row=row, column=0, padx=(0,0), pady=(0,12), sticky="nsw")
    traficc_page_lb = ctk.CTkLabel(menu_bar_frame, text="Tráfico", text_color=menu_text_color, font=("Arial", 12, "bold"), width=65, anchor="w")
    row += 1   

    logout_icon_btn = ctk.CTkButton(menu_bar_frame, image=logout_ctk, text="", height=btn_height, width=btn_width,
                                    fg_color=menu_bar_color, hover_color="#e74c3c",
                                    command=logout)
    logout_icon_btn.grid(row=row, column=1, padx=(0,0), pady=(0,12), sticky="w")
    logout_indicator_frame = ctk.CTkFrame(menu_bar_frame, fg_color=menu_bar_color, height=btn_height, width=5)
    logout_indicator_frame.grid(row=row, column=0, padx=(0,0), pady=(0,12), sticky="nsw")
    logout_page_lb = ctk.CTkLabel(menu_bar_frame, text="Salir", text_color=menu_text_color, font=("Arial", 12, "bold"), width=65, anchor="w")
    row += 1

    

    # --- Oculta los labels al inicio ---
    fold_menu()
    home_page()  # Página inicial

    root2.mainloop()

ventana2()