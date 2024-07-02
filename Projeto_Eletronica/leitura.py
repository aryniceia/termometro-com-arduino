import serial
import csv
from datetime import datetime
import time  # Para adicionar uma pausa no loop

# Configuração da porta serial
ser = serial.Serial('COM3', 9600, timeout=1)
ser.flushInput()  # Limpa o buffer de entrada da porta serial

# Configuração do arquivo CSV
csv_file = open('dados_temperatura.csv', mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Datetime', 'Temperature'])

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            if "Temperatura" in line:
                # Extrai os valores de temperatura
                parts = line.split(' ')
                temperature = parts[1]
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                csv_writer.writerow([current_time, temperature])
                csv_file.flush()  # Garante que os dados sejam salvos no arquivo
                print(f"{current_time} - Temperature: {temperature} °C")
        time.sleep(0.1)  # Adiciona uma pausa curta para evitar uso excessivo da CPU

finally:
    csv_file.close()
    ser.close()