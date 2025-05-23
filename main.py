
import json
import os
import requests
from geopy.distance import geodesic

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RUTAS_JSON = os.path.join(SCRIPT_DIR, "rutas.json")
API_KEY = "3bfa287862fe47ecaba12644251605"

DEBUG = True

class Rutas:
    Lista_rutas = []

    def __init__(self, ruta, nombre, horario, dias, tiempo, estaciones, origen, destino, precio, distancia, paradas=None):
        self.ruta = ruta
        self.nombre = nombre
        self.horario = horario
        self.dias = dias
        self.tiempo = tiempo
        self.estaciones = estaciones
        self.origen = origen
        self.destino = destino
        self.precio = precio
        self.distancia = distancia
        self.clima = None
        self.hora_salida = None
        self.hora_llegada = None
        self.paradas = paradas or []
        
        Rutas.Lista_rutas.append(self)
        

    @classmethod
    def cargar_rutas(cls):
        cls.Lista_rutas = []
        
        if DEBUG:
            print(f"🔍 Cargando rutas desde {RUTAS_JSON}")
            print(f"🔍 El archivo existe: {os.path.exists(RUTAS_JSON)}")
            
        if os.path.exists(RUTAS_JSON):
            try:
                with open(RUTAS_JSON, "r", encoding="utf-8") as file:
                    if DEBUG:
                        print("🔍 Leyendo el archivo JSON...")
                        
                    data = json.load(file)
                    
                    if DEBUG:
                        print(f"🔍 Datos cargados, número de rutas: {len(data)}")
                    
                    for ruta_data in data:
                        Rutas(
                            ruta_data["ruta"],
                            ruta_data["nombre"],
                            ruta_data["horario"],
                            ruta_data["dias"],
                            ruta_data["tiempo"],
                            ruta_data["estaciones"],
                            ruta_data["origen"],
                            ruta_data["destino"],
                            ruta_data["precio"],
                            ruta_data["distancia"],
                            ruta_data.get("paradas", [])
                        )
                print(f"✅ Rutas cargadas correctamente. {len(cls.Lista_rutas)} rutas disponibles.")
            except json.JSONDecodeError as e:
                print(f"⚠️ Error al leer el archivo JSON: {e}")
            except Exception as e:
                print(f"⚠️ Error inesperado: {e}")
        else:
            print("⚠️ El archivo JSON no existe. Asegúrate de que el archivo rutas.json esté en la misma carpeta que este script.")
        
        return Rutas.Lista_rutas
        
    @classmethod
    def guardar_rutas(cls):
        data = []
        for ruta in Rutas.Lista_rutas:
            data.append({
                "ruta": ruta.ruta,
                "nombre": ruta.nombre,
                "horario": ruta.horario,
                "dias": ruta.dias,
                "tiempo": ruta.tiempo,
                "estaciones": ruta.estaciones,
                "origen": ruta.origen,
                "destino": ruta.destino,
                "precio": ruta.precio,
                "distancia": ruta.distancia,
                "paradas": ruta.paradas
            })
        with open(RUTAS_JSON, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("✅ Rutas guardadas correctamente.")

class Paradas:
    Lista_paradas = []
    
    def __init__(self, paradas):
        self.paradas = paradas
        self.velocidad = 40  # km/h
        Paradas.Lista_paradas.append(self)
    
    def obtener_paradas(self):
        return self.paradas
    
    def contar_paradas(self):
        return len(self.paradas)
    
    def distancia_y_tiempo(self):
        info = []
        distancia_total = 0
        
        if not self.paradas or len(self.paradas) < 2:
            return [], 0
        
        for i in range(len(self.paradas) - 1):
            parada_actual = self.paradas[i]
            parada_siguiente = self.paradas[i + 1]

            if len(parada_actual) < 2 or len(parada_siguiente) < 2:
                continue
                
            coordenadas_actual = parada_actual[1]
            coordenadas_siguiente = parada_siguiente[1]

            distancia = round(geodesic(coordenadas_actual, coordenadas_siguiente).kilometers, 2)
            distancia_total += distancia

            # Calcular tiempo basado en velocidad promedio de transporte urbano
            tiempo = round((distancia / self.velocidad) * 60, 1)
            
            # Añadir tiempo de parada (1-2 minutos por parada)
            tiempo_parada = 1.5
            tiempo_total_tramo = round(tiempo + tiempo_parada, 1)
            
            info.append({
                "de": parada_actual[0],
                "a": parada_siguiente[0],
                "distancia": distancia,
                "tiempo": tiempo_total_tramo,
                "tiempo_viaje": tiempo,
                "tiempo_parada": tiempo_parada
            })
        
        return info, round(distancia_total, 2)

class ClimaTiempoReal:
    def __init__(self, ciudad, api_key):
        self.ciudad = ciudad
        self.api_key = api_key
        self.datos_clima = None

    def obtener_clima(self):
        url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={self.ciudad}&aqi=no"
        try:
            respuesta = requests.get(url, timeout=10)
            respuesta.raise_for_status()
            self.datos_clima = respuesta.json()
            return True
        except requests.exceptions.RequestException as err:
            print(f"Error al obtener el clima: {err}")
            return False

    def mostrar_clima(self):
        if self.datos_clima:
            descripcion = self.datos_clima['current']['condition']['text']
            temperatura = self.datos_clima['current']['temp_c']
            humedad = self.datos_clima['current']['humidity']
            ciudad = self.datos_clima['location']['name']
            return f"📍 Ciudad: {ciudad}\n☁️ Clima: {descripcion}\n🌡️ Temperatura: {temperatura}°C\n💧 Humedad: {humedad}%"
        else:
            return "❌ No se pudo obtener el clima."
        
class Clima_trafico:
    def __init__(self, ciudad, api_key):
        self.ciudad = ciudad
        self.api_key = api_key
        self.datos_clima = None
        self.datos_trafico = None
        
    def obtener_clima(self):
        url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={self.ciudad}&aqi=no"
        try:
            respuesta = requests.get(url, timeout=10)
            respuesta.raise_for_status()
            self.datos_clima = respuesta.json()
            return True
        except requests.exceptions.RequestException as err:
            print(f"Error al obtener el clima: {err}")
            return False