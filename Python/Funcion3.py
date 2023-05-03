from scipy.io import wavfile
import numpy as np
from scipy.signal import freqz, butter, lfilter

import matplotlib.pyplot as plt


def AnalisisFrecuencia(x,fs):
    if len(x.shape) == 1:
        x = x.reshape(-1, 1)
        
    # ajuste de escala para frecuencia
    fac = 1
    
    # Frecuancias de corte para Filtros
    Wn  = fac * np.array([0.2, 0.5])
    Wn1 = fac * np.array([0.2, 0.26])
    Wn2 = fac * np.array([0.26, 0.32])
    Wn3 = fac * np.array([0.32, 0.38])
    Wn4 = fac * np.array([0.38, 0.44])
    Wn5 = fac * np.array([0.44, 0.50])
    
    # Calculo de coeficientes para filtros
    b, a = butter(20, Wn,'bandpass' )
    b1, a1 = butter(10, Wn1,'bandpass' )
    b2, a2 = butter(10, Wn2,'bandpass' )
    b3, a3 = butter(10, Wn3,'bandpass' )
    b4, a4 = butter(10, Wn4,'bandpass' )
    b5, a5 = butter(10, Wn5,'bandpass' )
    
    # Aplicación de filtros
    y = lfilter(b, a, x, axis=0)
    y1 = lfilter(b1, a1, y, axis=0)
    y2 = lfilter(b2, a2, y, axis=0)
    y3 = lfilter(b3, a3, y, axis=0)
    y4 = lfilter(b4, a4, y, axis=0)
    y5 = lfilter(b5, a5, y, axis=0)
    
    # calculo de energía
    epsilon = 1e-10
    energiatotal = np.sum(np.abs(x[:, 0]) + epsilon)

    energiade2a5 = np.sum(np.sqrt(y[:, 0] ** 2))
    energia1 = np.sum(np.sqrt(y1[:, 0] ** 2))
    energia2 = np.sum(np.sqrt(y2[:, 0] ** 2))
    energia3 = np.sum(np.sqrt(y3[:, 0] ** 2))
    energia4 = np.sum(np.sqrt(y4[:, 0] ** 2))
    energia5 = np.sum(np.sqrt(y5[:, 0] ** 2))
    
    # energia totales para cada banda
    E = [energiatotal, energiade2a5, energia1, energia2, energia3, energia4, energia5]
    
    # Calculo de porcentajes
    p = energiade2a5 / energiatotal
    p1 = energia1 / energiade2a5
    p2 = energia2 / energiade2a5
    p3 = energia3 / energiade2a5
    p4 = energia4 / energiade2a5
    p5 = energia5 / energiade2a5
    
    P = [p1, p2, p3, p4, p5]
    porcentajes = P
    print("Energia", E)
    print("Porcentajes", porcentajes)
    
    # Funciones finales de audio
    y = y1 + y2 + y3 + y4 + y5

    # Cálculo de coeficientes para eliminación de bandas en audio, si la
    # banda es aceptada el coeficiente será 1 y si no será 0
    G = [0, 0, 0, 0, 0]  # definición de vector de coeficientes
    for i in range(5):
        if P[i] > 0.25:   # porcentaje de aceptación
            G[i] = 1      # ganancia unitaria
    yfinal = G[0]*y1 + G[1]*y2 + G[2]*y3 + G[3]*y4 + G[4]*y5

    # Guardando archivos de audio en la carpeta contenedora de la función
    wavfile.write('y.wav', fs, y.astype('float32'))
    wavfile.write('yfinal.wav', fs, yfinal.astype('float32'))

    # Graficas
    # Funciones
    import matplotlib.pyplot as plt

    # Primera figura
    plt.figure(1)
    n = range(len(x))
    plt.stem(n, x[:, 0])
    plt.title('x[n]')

    # Segunda figura
    plt.figure(2)
    n = range(len(x))
    plt.stem(n, y.flatten())
    plt.title('y[n]')

    # Tercera figura
    plt.figure(3)
    n = range(len(x))
    plt.stem(n, yfinal.flatten())
    plt.title('yfinal[n]')

    # Filtro de 2 a 5 KHz

    plt.figure(4)
    b, a = butter(4, [2000, 5000], btype='bandpass', fs=16000)
    w, h = freqz(b, a, fs=fs)
    plt.plot(w, abs(h) )
    plt.title('FILTRO PARA BANDA PRINCIPAL (2.0-5.0)KHz')

    # Filtros aplicados a la banda
    plt.figure(5)
    b1, a1 = butter(4, [2000, 2600], btype='bandpass', fs=16000)
    w1, h1 = freqz(b1, a1, fs=fs)
    plt.plot(w1, abs(h1))
    plt.title('PRIMER FILTRO: (2.0-2.6)KHz')

    plt.figure(6)
    b2, a2 = butter(4, [2600, 3200], btype='bandpass', fs=16000)
    w2, h2 = freqz(b2, a2, fs=fs)
    plt.plot(w2, abs(h2))
    plt.title('SEGUNDO FILTRO: (2.6-3.2)KHz')

    plt.figure(7)
    b3, a3 = butter(4, [3200, 3800], btype='bandpass', fs=16000)
    w3, h3 = freqz(b3, a3, fs=fs)
    plt.plot(w3, abs(h3))
    plt.title('TERCER FILTRO: (3.2-3.8)KHz')

    plt.figure(8)
    b4, a4 = butter(4, [3800, 4200], btype='bandpass', fs=16000)
    w4, h4 = freqz(b4, a4, fs=fs)
    plt.plot(w4, abs(h4))
    plt.title('CUARTO FILTRO: (3.8-4.2)KHz')

    plt.figure(9)
    b5, a5 = butter(4, [3200,  5000], btype='bandpass', fs=16000)
    w5, h5 = freqz(b5, a5, fs=fs)
    plt.plot(w5, abs(h5))
    plt.title('QUINTO FILTRO: (3.2-5.0)KHz')


    # Graficar la relación total de filtros
    plt.figure(10)
    plt.title('RELACION TOTAL DE FILTROS')
    plt.plot(w, abs(h))
    plt.plot(w1, abs(h1))
    plt.plot(w2, abs(h2))
    plt.plot(w3, abs(h3))
    plt.plot(w4, abs(h4))
    plt.plot(w5, abs(h5))

    plt.show()

fs, x = wavfile.read('grabacion.wav')
AnalisisFrecuencia(x,fs)