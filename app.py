from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/api/hora_actual', methods=['GET', 'POST'])
def get_current_time():
    try:
        # Obtener la hora y fecha actual del sistema del servidor
        now = datetime.datetime.now()
        
        # Formatear la hora y la fecha a un string legible
        hora_str = now.strftime("%H:%M") # Formato HH:MM
        
        # Crear el mensaje para Wildix
        message = f"La hora actual es: {hora_str}"
        
        # Devolver la respuesta en el formato que Wildix espera
        return jsonify({"message": message})
    except Exception as e:
        # Manejar errores
        return jsonify({"message": "Lo siento, no pude obtener la hora en este momento."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

