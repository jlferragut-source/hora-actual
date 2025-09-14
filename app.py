from flask import Flask, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/api/hora_actual', methods=['GET', 'POST'])
def get_current_time():
    try:
        # Define la zona horaria de Madrid
        madrid_tz = pytz.timezone('Europe/Madrid')
        
        # Obtiene la hora y fecha actual en la zona horaria de Madrid
        now = datetime.datetime.now(madrid_tz)
        
        # Formatea los datos a strings legibles
        hora_str = now.strftime("%H:%M") 
        dia_semana_str = now.strftime("%A") 
        mes_str = now.strftime("%B") 
        dia_mes_str = now.strftime("%d") 

        # Traduce el día de la semana y el mes al español
        dias_espanol = {
            "Monday": "lunes",
            "Tuesday": "martes",
            "Wednesday": "miércoles",
            "Thursday": "jueves",
            "Friday": "viernes",
            "Saturday": "sábado",
            "Sunday": "domingo"
        }
        meses_espanol = {
            "January": "enero",
            "February": "febrero",
            "March": "marzo",
            "April": "abril",
            "May": "mayo",
            "June": "junio",
            "July": "julio",
            "August": "agosto",
            "September": "septiembre",
            "October": "octubre",
            "November": "noviembre",
            "December": "diciembre"
        }

        dia_semana_es = dias_espanol.get(dia_semana_str)
        mes_es = meses_espanol.get(mes_str)

        # Crea el mensaje final para Wildix
        message = f"Hoy es {dia_semana_es}, {dia_mes_str} de {mes_es}. La hora actual es: {hora_str}."
        
        # Devuelve la respuesta en formato JSON
        return jsonify({"message": message})
    except Exception as e:
        return jsonify({"message": "Lo siento, no pude obtener la información en este momento."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
