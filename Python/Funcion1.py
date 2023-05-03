import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la duración y frecuencia de muestreo de la grabación
duracion_grabacion = 5  # duración de la grabación en segundos
frecuencia_muestreo = 44100  # frecuencia de muestreo en Hz

# Grabación de audio

x = sd.rec(int(duracion_grabacion * frecuencia_muestreo), samplerate=frecuencia_muestreo, channels=1)
sd.wait()

# Visualización de la forma de onda del audio grabado

plt.plot(x)
plt.title('Forma de onda del audio grabado')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.show()

# Cálculo de la duración y frecuencia fundamental del audio grabado
duracion_audio = len(x) / frecuencia_muestreo
frecuencia_fundamental = 1 / duracion_audio
print(f"Duración del audio grabado: {duracion_audio:.2f} segundos")
print(f"Frecuencia fundamental del audio grabado: {frecuencia_fundamental:.2f} Hz")