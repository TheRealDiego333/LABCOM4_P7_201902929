import numpy as np
import scipy.signal as signal
from scipy.signal import ellip, cheby2, firwin, lfilter
from scipy.io import wavfile
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def Ecualizador(Ganancias, x, fs=16000):

    if len(Ganancias) != 10:
        print("El vector de ganancias debe tener una longitud de 10")
        return

    if fs == None:
        fs = 48000
        print("No ha ingresado la frecuencia de muestreo fs, por lo tanto tomara el valor por default fs=48000 Hz")
        print("Esto provocara una mala grabación de las funciones finales si no coinciden los fs")
    
    G = Ganancias
    fac = 1 # Normalización de la frecuencia

    # Frecuencias de corte para Filtros
    Wn1 =  fac*np.array([0.01098, 0.02150]) # filtro banda 1
    Wn2 =  fac*np.array([0.02150, 0.04150]) # filtro banda 2
    Wn3 =  fac*np.array([0.05250, 0.07250]) # filtro banda 3
    Wn4 =  fac*np.array([0.08500, 0.11500]) # filtro banda 4
    Wn5 =  fac*np.array([0.11500, 0.18300]) # filtro banda 5
    Wn6 =  fac*np.array([0.19400, 0.29700]) # filtro banda 6
    Wn7 =  fac*np.array([0.30000, 0.40500]) # filtro banda 7
    Wn8 =  fac*np.array([0.41000, 0.60500]) # filtro banda 8
    Wn9 =  fac*np.array([0.60000, 0.76040]) # filtro banda 9
    Wn10 = fac*np.array([0.77000, 0.92465]) # filtro banda 10

    # filtros butter
    b1, a1 = signal.butter(2, Wn1, 'bandpass')
    y1 = signal.filtfilt(b1, a1, x)
    wavfile.write('filtro1.wav', fs, y1)

    b2, a2 = signal.butter(3, Wn2, 'bandpass')
    y2 = signal.filtfilt(b2, a2, x)
    wavfile.write('filtro2.wav', fs, y2)

    # filtros cheby1
    b3, a3 = signal.cheby1(5, 10, Wn3, 'bandpass')
    y3 = signal.filtfilt(b3, a3, x)
    wavfile.write('filtro3.wav', fs, y3)
        
    b4, a4 = signal.cheby1(5, 10, Wn4, 'bandpass')
    y4 = signal.filtfilt(b4, a4, x)
    wavfile.write('filtro4.wav', fs, y4)

    #filtros ellip

    [b5,a5] = ellip(5,10,500,Wn5, 'bandpass')
    y5 = lfilter(b5,a5,x)
    wavfile.write('filtro5.wav', fs, y5)

    [b6,a6] = ellip(5,1,200,Wn6, 'bandpass')
    y6 = lfilter(b6,a6,x)
    wavfile.write('filtro6.wav', fs, y6)

    #filtros cheby2

    [b7,a7] = cheby2(10,50,Wn7, 'bandpass')
    y7 = lfilter(b7,a7,x)
    wavfile.write('filtro7.wav', fs, y7)

    [b8,a8] = cheby2(10,40,Wn8, 'bandpass')
    y8 = lfilter(b8,a8,x)
    wavfile.write('filtro8.wav', fs, y8)

    #filtros tipo fir

    y9 = y8.copy()
    y10 = y9.copy()
    b9 = firwin(60,Wn9, pass_zero='bandpass')
    ym9 = np.convolve(b9,x)
    wavfile.write('filtro9.wav', fs, y9)

    b10 = firwin(60,Wn10, pass_zero= 'bandpass')
    ym10 = np.convolve(b10,x)
    wavfile.write('filtro10.wav', fs, y10)

    #Arreglo de vectores

    y9 = np.zeros(len(x))
    y10 = np.zeros(len(x))
    for i in range(len(x)):
        y9[i] = ym9[i]
        y10[i] = ym10[i]
    y9 = np.transpose(y9)
    y10 = np.transpose(y10)


    # Arreglo de vector de ganancias para orientación de vector
    v = G.shape
    if v[0] == 10:
        G = G.T

    y = G[0]*y1 + G[1]*y2 + G[2]*y3 + G[3]*y4 + G[4]*y5 + G[5]*y6 + G[6]*y7 + G[7]*y8 + G[8]*y9 + G[9]*y10 

    # guardando el archivo de audio
    wavfile.write('y.wav', fs, y)

    # Graficas
    # Funciones
    figure(12)
    n = range(len(x))
    plt.subplot(2,1,1)
    plt.stem(n, x)
    plt.title('x[n]')
    plt.subplot(2,1,2)
    plt.stem(n, y)
    plt.title('y[n]')

    figure(1)
    w1, h1 = signal.freqz(b1, a1)
    plt.plot(w1/np.pi, np.abs(h1))
    plt.title('FILTRO CON FRECUENCIA CENTRAL EN:  31.5 Hz')

    figure(2)
    w2, h2 = signal.freqz(b2, a2)
    plt.plot(w2/np.pi, np.abs(h2))
    plt.title('FILTRO CON FRECUENCIA CENTRAL EN:  63 Hz')

    figure(3)
    w3, h3 = signal.freqz(b3, a3)
    plt.plot(w3/np.pi, np.abs(h3))
    plt.title('FILTRO CON FRECUENCIA CENTRAL EN: 125 Hz')

    figure(4)
    w4, h4 = signal.freqz(b4, a4)
    plt.plot(w4/np.pi, np.abs(h4))
    plt.title('FILTRO CON FRECUENCIA CENTRAL EN:  250 Hz')

    figure(5)
    w5, h5 = signal.freqz(b5, a5)
    plt.plot(w5/np.pi, np.abs(h5))
    plt.title('FILTRO CON FRECUENCIA CENTRAL EN:  500 Hz')

    figure(6)
    w6, h6 = signal.freqz(b6, a6)
    plt.plot(w6/np.pi, np.abs(h6))
    plt.title('FILTRO CON FRECUENCIA CENTRAL EN:  1 kHz')

    figure(7)
    w7, h7 = signal.freqz(b7, a7)
    plt.plot(w7/np.pi, np.abs(h7))
    plt.title('FILTRO CON FRECUENCIA CENTRAL EN:  2 kHz')

    figure(8)
    w8, h8 = signal.freqz(b8, a8)
    plt.plot(w8/np.pi, np.abs(h8))
    plt.title('FILTRO CON FRECUENCIA CENTRAL EN:  4 kHz')

    figure(9)
    w9, h9 = signal.freqz(b9, 1)
    plt.plot(w9/np.pi, np.abs(h9))
    plt.title('FILTRO CON FRECUENCIA CENTRAL EN:  8 kHz')
    plt.show()

    figure(10)
    w10, h10 = signal.freqz(b10, 1)
    plt.plot(w10/np.pi, np.abs(h10))
    plt.title('FILTRO CON FRECUENCIA CENTRAL EN:  16 kHz')
    plt.show()

    figure(11)
    plt.plot(w1/np.pi, np.abs(h1))
    plt.plot(w2/np.pi, np.abs(h2))
    plt.plot(w3/np.pi, np.abs(h3))
    plt.plot(w4/np.pi, np.abs(h4))
    plt.plot(w5/np.pi, np.abs(h5))
    plt.plot(w6/np.pi, np.abs(h6))
    plt.plot(w7/np.pi, np.abs(h7))
    plt.plot(w8/np.pi, np.abs(h8))
    plt.plot(w9/np.pi, np.abs(h9))
    plt.title('RELACION TOTAL DE FILTROS GON GANANCIA UNITARIA')
    plt.show()




fs, x = wavfile.read('grabacion.wav')
ganancias = np.array([1, -3, 2, 5, -2, 3, 4, -4, -1, 0])

Ecualizador(ganancias,x,fs)