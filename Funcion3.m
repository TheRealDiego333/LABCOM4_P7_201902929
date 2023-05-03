pkg load signal;

[x, fs] = audioread('grabacion.wav');

AnalisisFrecuencia(x,fs);
