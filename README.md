# Laboratorio3
## Problema del coctel.
### Descripcion 
<p>
En este proyecto se busca aislar una voz especifica en un entorno con ruido de multiples voces en el escenario de una fiesta, donde se capta las señales de audio atraves de microfonos y son analizadas por medio de tecnicas de separacion aplicando algoritmos para desenredar las voces y extraer la voz deseada con la mayor claridad. con el fin de reproducir por separado el
audio de cada una de las voces capturadas. 
  
</p>  

#### Frecuencia de muestreo.
<p>
Es la cantidad de muestras tomadas por unidad de tiempo, para convertir una señal análoga a digital. En audio la frecuencia de muestreo determina la precisión del audio digital.
Según el teorema de Nyquist, la frecuencia de muestreo debe ser al menos el doble de la frecuencia más alta contenida en la señal original. Dado que el oído humano puede percibir sonidos en un rango de 20 Hz a 20.000 Hz, se requiere una frecuencia de muestreo mínima de 40.000 Hz para capturar. para este laboratorio seleccionamos la frecuencia estandar de 44.1 kHz que cumple el teorema de nyquist, esta frecuencia es superior al doble de la frecuencia maxima audible de 20kHz. 
</p>

### Procedimiento.
<p>
Para realizar este laboratorio es necesario utilizar metodos matematicos que nos permitan separar y analizar la señal, teniendo en cuenta que 
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

![PSD](https://github.com/user-attachments/assets/6cf1c39a-3479-45b4-8c7d-7a4d0827176b)

La PSD muestra un pico máximo por debajo de 50 Hz y se va disminuyendo progresivamente, lo cual indica que es coherente para un ECG. En caso de que hubiera aumentado en altas frecuencias podría indicar que hay presencia de ruido

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

</p>



### Relacion señal-ruido
<p>
La relación señal-ruido es una métrica fundamental en el procesamiento de señales, puesto que permite evaluar la calidad de una señal en presencia de ruido, esta medida  compara la potencia de la señal útil con la potencia del ruido presente en un sistema.
La formula general para calcular el SNR en Decibelios (dB) es:

Donde:

- Pseñal es la potencia de la señal.
- Pruido es la potencia del ruido.

    
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

