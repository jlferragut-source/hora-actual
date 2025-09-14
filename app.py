from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/hora_actual', methods=['GET', 'POST'])
def get_current_time():
    try:
        # Llamar a la API de World Time para obtener la hora
        response = requests.get('http://worldtimeapi.org/api/timezone/Europe/Madrid')
        data = response.json()
        
        # Extraer y formatear la fecha y hora
        datetime_str = data['datetime']
        hora_str = datetime_str[11:16] # "HH:MM"
        
        # Crear el mensaje final para Wildix
        message = f"La hora actual es: {hora_str}"
        
        # Devolver la respuesta en el formato que Wildix espera
        return jsonify({"message": message})
    except Exception as e:
        # Manejar errores y devolver un mensaje genérico
        return jsonify({"message": "Lo siento, no pude obtener la hora en este momento."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
