from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/hora_actual', methods=['GET', 'POST'])
def get_current_time():
    try:
        # 1. Llamar a la API de World Time para obtener el JSON completo
        response = requests.get('http://worldtimeapi.org/api/timezone/Europe/Madrid')
        data = response.json()
        
        # 2. Extraer la cadena de la fecha y hora
        datetime_str = data['datetime']
        
        # 3. Formatear la cadena para obtener solo la hora (HH:MM)
        # Por ejemplo, de "2025-09-14T18:30:58.798228+02:00" a "18:30"
        hora_str = datetime_str[11:16] 
        
        # 4. Crear el mensaje final en un formato que Wildix entienda
        message = f"La hora actual es: {hora_str}"
        
        # 5. Devolver la respuesta en un JSON simple con el campo "message"
        return jsonify({"message": message})
    except Exception as e:
        # Manejo de errores
        return jsonify({"message": "Lo siento, no pude obtener la hora en este momento."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
