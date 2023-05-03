function [x] = grabaraudio(t,fs)
% Función para grabar un archivo de audio con el nombre "grabacion".
% Devuelve un vector x y su frecuencia de muestreo y almacena la señal grabada en la carpeta "grabaraudio".

recObj = audiorecorder(fs, 16, 1); % Crea un objeto grabador de audio
disp('Comenzando a grabar');
recordblocking(recObj, t); % Grabar durante t segundos
disp('Grabación finalizada');
x = getaudiodata(recObj); % Obtiene los datos grabados

audiowrite('grabacion.wav', x, fs); % Guarda el archivo de audio en la carpeta actual

% Reproduce la señal grabada
[y,fs] = audioread('grabacion.wav');
sound(y,fs);

end
