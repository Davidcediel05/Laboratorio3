# Laboratorio3
## Problema del coctel.
### Descripcion 
<p>
En este proyecto se busca aislar una voz especifica en un entorno con ruido de multiples voces en el escenario de una fiesta, donde se capta las señales de audio atraves de microfonos y son analizadas por medio de tecnicas de separacion aplicando algoritmos para desenredar las voces y extraer la voz deseada con la mayor claridad. con el fin de reproducir por separado el
audio de cada una de las voces capturadas. 
  
</p>  


### Procedimiento.
<p>
Para este laboratorio el objetivo es recrear el problema de la fiesta de coctel, donde existen 2 fuentes sonoras capturadas por un arreglo de 2 micrófonos, en este caso, de acuerdo con la siguiente metodología. Se conectaron dos microfonos del celular los cuales fueron distribuidos verticalmente a 3 metros de los colaboradores, los colaboradores se encontraban mirándose de frente, simulando una conversación tipo coctel. Dichas grabaciones cuentan con 10 segundos de ruido del espacio insonoro y 39 seg de grabación dentro de la conversación.
Es necesario utilizar metodos matematicos que nos permitan analizar y separar la señal, utilizaremos el analisis de componentes independientes para eliminar las interferencias entre las voces, la tecnica de Beamforing que mejora la calidad de la señal en un entorno ruidoso y  para el analisis usamos las transformadas de furier. 

![image](https://github.com/user-attachments/assets/d1b09ffb-6834-49d8-b450-d92470a3362a)
![image](https://github.com/user-attachments/assets/879d1e41-1746-4c05-ad1a-fb205e03bf7d)




</p>

 ### Relacion señal-ruido
<p>
La relación señal-ruido es una métrica fundamental en el procesamiento de señales, puesto que permite evaluar la calidad de una señal en presencia de ruido, esta medida  compara la potencia de la señal útil con la potencia del ruido presente en un sistema.
La formula general para calcular el SNR en Decibelios (dB) es:
  


Donde:

- Pseñal es la potencia de la señal.
- Pruido es la potencia del ruido.

Se calculo el SNR de cada señal, asi mismo atraves de una función de la librería librosa y el siguiente comando librosa.load(), se identifica la frecuencia de muestreo del audio, posterior al proceso de análisis temporal y espectral (cuyas graficas desarrollaremos mas adelante) y el análisis de componentes independientes, igual a el análisis por Beamforming que permitirán asilar la señal de interés y asi calcular el SNR y comparar el desempeño de separación

![image](https://github.com/user-attachments/assets/4d15dde4-3835-419e-b3d5-2d3f4f4437f1)

**Implementación en el Código:**

`import librosa
archivo = r"C:\Users\juany\OneDrive\Escritorio\LabSeñales\Lab3\CedielSeñal.wav"  # Nombre del archivo
_, sr = librosa.load(archivo, sr=None)  # Carga sin modificar la frecuencia
print(f"Frecuencia de muestreo original: {sr} Hz")`

</p>

#### Frecuencia de muestreo.
<p>
Es la cantidad de muestras tomadas por unidad de tiempo, para convertir una señal análoga a digital. En audio la frecuencia de muestreo determina la precisión del audio digital.
Según el teorema de Nyquist, la frecuencia de muestreo debe ser al menos el doble de la frecuencia más alta contenida en la señal original. Dado que el oído humano puede percibir sonidos en un rango de 20 Hz a 20.000 Hz, se requiere una frecuencia de muestreo mínima de 40.000 Hz para capturar. para este laboratorio seleccionamos la frecuencia estandar de 44.1 kHz que cumple el teorema de nyquist, esta frecuencia es superior al doble de la frecuencia maxima audible de 20kHz. 
Por parte de la adquisición para el procesamiento de estas señales se realizo con una frecuencia de muestreo 48kHz, con esta información nos permite también saber que se puede capturar frecuencias de 24kHz, cumpliendo con el criterio de Nyquist para señales de audio, Ademas por tema de la cuantificación se siguió el estándar de los archivos WAV, la cual representa valores flotantes de 32 bits, lo que nos permite asegurar una buena conversión digital.

**Implementación en el Código:**

`audio1, sr1 = librosa.load(r'C:\Users\Usuario\Downloads\Lab3\CedielSeñal.wav',sr=48000)
audio2, sr2 = librosa.load(r'C:\Users\Usuario\Downloads\Lab3\lab3juanyAmb.wav',sr=48000)
ruido1, sr3 = librosa.load(r'C:\Users\Usuario\Downloads\Lab3\CedielAmb.wav',sr=48000)
ruido2, sr4 = librosa.load(r'C:\Users\Usuario\Downloads\Lab3\lab3juanyAmb.wav',sr=48000)`

El tiempo de captura como ya fue mencionado de cada señal fue de 39 a 40 segundos, por lo cual por medio de relleno de ceros (Padding) se igualo ambas señales que nos permitirá mezclar o separación sin perdidas de información. 

`longitud_max = max(len(audio1), len(audio2))
audio1 = np.pad(audio1, (0, longitud_max - len(audio1)))
audio2 = np.pad(audio2, (0, longitud_max - len(audio2)))
audio_mix = np.vstack((audio1, audio2)).T`

El calculo del SNR se calculo antes y despues de aplicar técnicas de procesamiento, como lo son (ICA) Y (BEAMFORMING), con el propósito de evaluar las voces y mejorar la calidad tras la reducción de interferencias y ruido.

`# Calcular la relación señal-ruido (SNR)
def snr_calculo(señal, ruido):
    pseñal = np.mean(señal ** 2)
    pruido = np.mean(ruido ** 2)
    snr = 10 * np.log10(pseñal / pruido)
    return snr`
`snr1 = snr_calculo(audio1, ruido1)
snr2 = snr_calculo(audio2, ruido2)
print(f"SNR Cediel: {snr1} dB")
print(f"SNR Juany: {snr2} dB")`

`# Asegurar que ambas señales de ruido tengan la misma longitud
longitud_max_ruido = max(len(ruido1), len(ruido2))
ruido1 = np.pad(ruido1, (0, longitud_max_ruido - len(ruido1)))
ruido2 = np.pad(ruido2, (0, longitud_max_ruido - len(ruido2)))
señal_suma = ruido1 + ruido2`

`# Calcular SNR final
SNR_FINAL_BEAM = snr_calculo(beamformed_signal, señal_suma)
SNR_FINAL_ICA = snr_calculo(señal_ica, señal_suma)`

</p>

#### Transformada de Fourier.
<P>
Una transformacion es una operacion que convierte una señal desde un dominio a otro dominio, la transformada de fourier convierte una señal del dominio del tiempo hacie el dominio de la frecuencia. Lo cual permite analizar las señales en dominios alternativos lo cual permite identificar las caracteristicas como frecuencias.
</p>
    
#### Transformada rapida de Fourier.

<P>
Esta transformación es una herramienta crucial para analizar y manipular el contenido espectral del audio, esto es fundamental para aplicaciones como la separación de fuentes.
Aplicación. La Transformada Rápida de Fourier (FFT) procesa una señal de audio en el dominio del tiempo, donde se representa la amplitud de la onda sonora a lo largo del tiempo, y la transforma en el dominio de la frecuencia. Esto permite visualizar la intensidad de cada componente de frecuencia presente en la señal original, es decir, identificar qué frecuencias conforman el sonido. En el caso del laboratorio, donde se analizan dos fuentes con diferentes timbres de voz, la FFT permite reconocer los rangos de frecuencia característicos de cada tipo de voz, donde una voz aguda ocuparia un rango de frecuencia alto, mientras que una voz gruesa ocuparia un rango de frecuencias bajas. 
</p>

**Implementación en el Código:**


#### Densidad espectral.

Mide la distribucion de energia de la señal en funcion de la frecuencia. se espera que nos muestre la contribucion de mas frecuencias en la señal.




**Implementación en el Código:**
    `def compute_psd(signal, Fs):
    freqs, psd_ch1 = welch(signal[:, 0], Fs, nperseg=1024)
    freqs, psd_ch2 = welch(signal[:, 1], Fs, nperseg=1024)
    return freqs, psd_ch1, psd_ch2`
    
</p>


### Metodos de separacion de fuentes.

<p>
  
Para este laboratorio utilizamos:
-El analisis de componentes independiente (ICA): Este metodo separa señales mezcladas en multiples fuentes independientes. el cual usa la tecnica matematica FastICA (optimizacion basada en independencia estadistica), a la salida podemos observar varias señales separadas, donde se observa que corresponde a cada fuente distinta. 
-Singular Value Descomposition (BEAMFORMING): Su funcion es mejorar la calida de una señal especifica en presencia de ruido, Analiza valores aplicados a matrices de señales. a la salida se observa una señal optimizada con mejor (SNR). En el entorno del laboratorio este metodo permite enfocar la captura de audio hacia una fuente especifica.

Beamforming
![image](https://github.com/user-attachments/assets/d8645396-2185-4a2c-aea5-a8eda78f764b)

**Implementación en el Código:**
  
    `# Beamforming
def calcular_retraso(distancias, velocidad, sr):
    return tuple(int(d / velocidad * sr) for d in distancias)`

`distancias = [0, 3.0]  # Distancia entre micrófonos en metros
velocidad_sonido = 343  # Velocidad del sonido en m/s
retraso = calcular_retraso(distancias, velocidad_sonido, sr1)`


Donde para hallar el retraso, debemos tener en cuenta la distancia, la velocidad de sonido, cabe resaltar que la velocidad se halla a través de esta fórmula, v=331.3+0.606⋅T donde la temperatura del salón era de 20c° el día de grabación, por parte de las distancias, ambos micrófonos están a 3 metros, por lo tanto, el cálculo del retraso se da por 
Retraso=3433.0×48000=419.5 muestras
Esto nos esta diciendo que el micrófono recibirá la señal con 419 muestras de diferencia respeto a la original 
Posterior a eso.

`def beamforming(signals, delay):
    num_mics = signals.shape[1]
    beamformed_signal = np.zeros(len(signals))
    for i, delay_i in enumerate(delay):
        beamformed_signal += np.roll(signals[:, i], -delay_i)
    return beamformed_signal / num_mics`

Lo subrayado nos ayuda a desplazar la señal en el tiempo de acuerdo con el retraso, lo cual compensa el retardo de la señal del segundo micrófono, Después de corregir los retrasos, se promedian las señales de los micrófonos para obtener la señal final.

`# Asegurar que ambas señales tengan la misma longitud
longitud_max = max(len(audio1), len(audio2))
audio1 = np.pad(audio1, (0, longitud_max - len(audio1)))
audio2 = np.pad(audio2, (0, longitud_max - len(audio2)))
audio_mix = np.vstack((audio1, audio2)).T`

Se ajustan las señales a la misma longitud para poder procesarlas juntas, posterior a eso se guarda la señal filtrada y el audio correspondiente.

`# Aplicar beamforming
beamformed_signal = beamforming(audio_mix, retraso)
output_file = r'C:\Users\Usuario\Downloads\Lab3\señal_beamformed.wav'
sf.write(output_file, beamformed_signal, sr1)`

`graficar_señal(beamformed_signal, 'Señal después de Beamforming', 'orange')
graficar_espectro(beamformed_signal, sr1, 'Señal Beamforming', 'orange')
graficar_psd(beamformed_signal, sr1, 'Señal Beamforming', 'orange')`




ICA
![image](https://github.com/user-attachments/assets/71e2859d-bbc0-4fc9-899b-18eca6654c47)

`# Aplicar Análisis de Componentes Independientes (ICA)
ica = FastICA(n_components=2)
señales_separadas = ica.fit_transform(audio_mix)
señal_ica = señales_separadas[:, 0]`

Ica nos permite encontrar fuentes independientes en señales mezcladas, es decir separa señales superpuestas
Finalmente se calcula el SNR después de beamforming y después de ICA, con el fin de comparar que método nos ayude a reducir el ruido y mejorar la señal


</p>


### Analisis temporal y frecuencial de las señales.

<p>
  
#### Dominio del tiempo.
-Las señales presentan variaciones de amplitud a lo largo del tiempo, mostrando características propias de cada fuente de audio.
-La señal de Juany tiene mayor variabilidad en amplitud en comparación con la de Cediel, lo que podría indicar diferencias en la 
 intensidad del sonido o en la presencia de ruido.
-En las muestras se observan fluctuaciones, lo que indica la influencia de interferencias o ruido ambiental.

#### Dominio de la frecuencia.
- Se utilizaron escalas lineales y logarítmicas, para representar el espectro de las señales. 
- En el espectro lineal, se identifican picos dominantes en bajas frecuencias, lo que muestra la mayor parte de la energía concentrada en componentes graves.
- El espectro logarítmico se visualiza las diferencias en niveles de energía en distintas bandas de frecuencia, donde se destaca la presencia de ruido en altas frecuencias.

![image](https://github.com/user-attachments/assets/3aea22ea-760e-4564-af04-aaf41beb1e90)
![image](https://github.com/user-attachments/assets/eddca05d-8318-43b9-8736-378e49e10859)

#### Dominio del tiempo.
-Las señales iniciales muestran variaciones en su amplitud, influenciadas por el ruido presente.
-La señal después de beamforming evidencia una reducción del ruido, al mejorar la alineación de las fuentes de interés.
-La señal tras ICA logra una separación efectiva de componentes, reduciendo aún más la interferencia y resaltando patrones más claros.

#### Dominio de la frecuencia.
- En el espectro lineal, tanto la señal de beamforming como la de ICA tienen componentes de baja frecuencia.
- En el espectro logarítmico, ICA muestra una distribución más uniforme en altas frecuencias, mostrando una mejor preservación del contenido espetral.
- Beamforming atenuó algunas frecuencias,logrando una señal más enfocada, pero ICA obtuvo una mayor mejora en la SNR.

![image](https://github.com/user-attachments/assets/defc5ea7-9826-4d82-96ee-2a34de3196b7)
![image](https://github.com/user-attachments/assets/662612e4-d1bb-4456-9d5b-7daf0283e43a)


</p>



### Requisitos
<p>
Para ejecutar el código, es necesario instalar Python e importar las siguientes librerías:

- import librosa
- import numpy as np
- import matplotlib,pyplot as plt
- import soundfile as sf
- from colorama import Fore, init
- import shutil
- from sklearn.descomposition import
- FastICA
  
Tener instalado un compilador, que para este caso se utilizo spyder.  
</p>

### Estructura del proyecto

- tfourier(): Transformada de fourier.
- 01.dat y 01.hea: Archivos de datos de la señal EMG.
- sklearn.decomposition.FastICA: separa las fuentes de audio mezcladas.  
- numpy: permite realizar operaciones matemáticas eficientes en matrices y arreglos.
- matplotlib: biblioteca estándar para crear visualizaciones.
- scipy: funciones para el diseño y aplicación de filtros.
- pyroomacoustics.Beamformer: enfoca la captura de audio en una direccion especifica. 


### Ejecución

- Asegúrate de que los archivos de datos están en la misma carpeta que los scripts.
-	Ejecuta Lab2.py o LAB2final.py para analizar la señal:
- python Lab2.py
  

### Conclusión
<p>

</p>

### Bibliografia

- Heras Rodríguez, MDL (2024). La transformada rápida de Fourier: fundamentos y aplicaciones (Tesis de licenciatura).
- Di Persia, LE (2017). Separación ciega de fuentes sonoras: revisión histórica y desarrollos recientes.
- González, J., Forero, E., Jiménez, F. y Mariño, I. (2013). Atenuación de rizado en la densidad espectral de potencia calculada en una señal de ritmo cardíaco. Matemática , 11 (2), 22-26.


### Licencia

Este proyecto es de uso académico y educativo.

### Contacto
<p>
Si tienes alguna pregunta o sugerencia, no dudes en contactarme:
</p>

- **Nombre:** [Juan David Cediel Farfan][Juan Yael Barriga Roa]
- **Email:** [est.juand.cediel@unimilitar.edu.co][est.juan.barriga@unimilitar.edu.co]
- **GitHub:** [David05Cediel][JuanYBR]

