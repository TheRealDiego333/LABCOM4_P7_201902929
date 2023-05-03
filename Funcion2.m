pkg load signal;

[x, fs] = audioread('grabacion.wav');
Ganancias = [1, -3, 2, 5, -2, 3, 4, -4, -1, 0];

Ecualizador(Ganancias,x,fs);
