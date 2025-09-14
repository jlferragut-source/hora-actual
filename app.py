from flask import Flask, jsonify
import datetime
import pytz # Importa la librería pytz

app = Flask(__name__)

@app.route('/api/hora_actual', methods=['GET', 'POST'])
def get_current_time():
    try:
        # 1. Define la zona horaria de Madrid
        madrid_tz = pytz.timezone('Europe/Madrid')

        # 2. Obtiene la hora actual, pero en la zona horaria de Madrid
        now = datetime.datetime.now(madrid_tz)

        # 3. Formatea la hora y la fecha a un string legible
        hora_str = now.strftime("%H:%M") # Formato HH:MM

        # 4. Crea el mensaje para Wildix
        message = f"La hora actual en Madrid es: {hora_str}"

        # 5. Devuelve la respuesta
        return jsonify({"message": message})
    except Exception as e:
        return jsonify({"message": "Lo siento, no pude obtener la hora en este momento."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
