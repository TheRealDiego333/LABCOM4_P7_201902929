% Configuración de la duración y frecuencia de muestreo de la grabación
duracion_grabacion = 5; % duración de la grabación en segundos
frecuencia_muestreo = 44100; % frecuencia de muestreo en Hz

% Grabación de audio
x = grabaraudio(duracion_grabacion, frecuencia_muestreo);

% Visualización de la forma de onda del audio grabado
plot(x);
title('Forma de onda del audio grabado');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Cálculo de la duración y frecuencia fundamental del audio grabado
duracion_audio = length(x) / frecuencia_muestreo;
frecuencia_fundamental = 1 / duracion_audio;
fprintf('Duración del audio grabado: %.2f segundos\n', duracion_audio);
fprintf('Frecuencia fundamental del audio grabado: %.2f Hz\n', frecuencia_fundamental);

