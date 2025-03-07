# Laboratorio3
## Problema del coctel.
### Descripcion 
<p>
En este proyecto se busca aislar una voz especifica en un entorno con ruido de multiples voces en el escenario de una fiesta, donde se capta las señales de audio atraves de microfonos y son analizadas por medio de tecnicas de separacion aplicando algoritmos para desenredar las voces y extraer la voz deseada con la mayor claridad. con el fin de reproducir por separado el
audio de cada una de las voces capturadas. 
  
</p>

#### Convolucion
<p>
La convolución es una operación matemática que combina dos funciones para describir la superposición entre ambas. En el procesamiento de señales se emplea para conocer que le sucede a una señal despues de pasar por un determinado dispositivo, detectan patrones que despues clasifican.
La convolucion define como un sistema modifica su señal de entrada utilizando su respuesta al impulso, es muy util para observar los sistemas lineales e invariantes en el tiempo. su principal funcion es combinar señales para describir sistemas. 
   
   - Para la funcion X (n)=[1,0,0,0,9,7,1,3,6,4] y H(n)=[5,6,0,0,6,1,6]

![convolucion](https://github.com/user-attachments/assets/e805c1e4-1338-4bb0-a83e-253e18b22434)
![image](https://github.com/user-attachments/assets/f3854a79-c290-470d-8498-688884937d94)
![image](https://github.com/user-attachments/assets/c94812bc-a9ba-4021-bc34-b5553adeb9d0)

   - Para la funcion  X(n)=[1,0,2,5,4,6,1,2,4,5] y H(n)=[5,6,0,0,6,1,1].

![convolucion](https://github.com/user-attachments/assets/fbf02378-4bff-4958-9f1c-56d1ae458709)
![convolucion a mano](https://github.com/user-attachments/assets/df538c97-d4b2-42da-b779-d0d6c04b8592)
![image](https://github.com/user-attachments/assets/49a80bf7-a9ca-4e20-9552-2b931b2d83ba)

Se puede observar las gráficas de convolución tanto con los datos del colaborador Juan David Cediel y Juan Yael Barriga, a continuación, se explicará que significa cada grafica.

- **Primera gráfica (Señal x[n]):**
Se puede visualizar una señal de entrada que tiene valores discretos en ciertos puntos, son valores significativos en ciertas posiciones, se puede inferir que la señal no presenta una uniformidad y por lo tanto no es periódica
- **Segunda gráfica (Señal h[n]):**
Representa la respuesta al impulso del sistema, esta señal indica el sistema posee varios múltiples puntos en el tiempo
- **Tercera gráfica(Convolución(x[n](h[n]x[n])( h[n]x[n])(h[n])):**
Esta tercera grafica es la convolución entre las dos graficas, nos señala que la señal resultante tiene mayor cantidad de puntos con valores mas grandes, es decir, esta grafica es el resultado muestra como la señal de entrada se ve afectada con la señal de salida.
</p>

#### Correlacion. 

<p>
La correlacion se encarga de medir la similitud entre señales, indica que tanto se parece una señal a la otra mientras una se desplaza respecto a la otra.
Hay dos tipos de correlacion.

-Autocorrelacion: Mide la periodicidad de una señal por lo tanto es la correlacion de una señal consigo misma.

-Correlacion cruzada: Se encarga de medir similitudes entre señales diferentes.

![correlacion](https://github.com/user-attachments/assets/7aab1564-8a08-4425-a7a5-9ce1ad945e74)

En la gráfica de correlación, podemos observar picos que indican que las señales estan alineadas entre ellas. Si las señales son independientes, la correlación debería ser baja en todos los puntos.

</p>


**Implementación en el Código:**

   `def compute_correlation(x1, x2):
    return np.correlate(x1, x2, mode='full')`
    

#### Señal en el tiempo.

![image](https://github.com/user-attachments/assets/be8fa0cc-e944-441b-a4ff-54e7b4940d6a)

<p>
Por parte de la señal en el tiempo se trata de una señal de ECG que muestra su evolución en función del tiempo en la cual podemos ver el ciclo cardiaco en dos diferentes canales, se puede observar picos regulares y patrones repetitivos, sin embargo la gráfica presenta cierta alteración en su forma que podemos indicar ruido
</p>

#### Transformada de Fourier.
<P>
Una transformacion es una operacion que convierte una señal desde un dominio a otro dominio, la transformada de fourier convierte una señal del dominio del tiempo hacie el dominio de la frecuencia. Lo cual permite analizar las señales en dominios alternativos lo cual permite identificar las caracteristicas como frecuencias.
    
![Transformada](https://github.com/user-attachments/assets/c25e9f11-98b8-4c6a-a32e-95b9b742499c)

La transformada de Fourier descompone la señal en componentes de frecuencia para un ECG, la mayoría se concentra en frecuencia bajas <50Hz Según Sörnmo, L., & Laguna, P. (2005) , podemos ver en al imagen que la mayoría de frecuencias se concentran en el rango de 0.5 a 50 Hz 
</p>

**Implementación en el Código:**

   `def compute_fourier(signal, Ts):
    N = len(signal)
    frequencies = fftfreq(N, Ts)
    spectrum = np.abs(fft(signal, axis=0))
    return frequencies, spectrum`

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





</p>

### Análisis Estadístico de la Señal

<p>
El análisis estadístico de la señal EMG permite extraer información relevante sobre su comportamiento, lo que es fundamental para diversas aplicaciones biomédicas. Algunos de los aspectos analizados incluyen:
</p>

- **La Media:**  De una señal es una medida fundamental que proporciona información sobre el valor promedio de los datos. 
- **Desviación estándar:** La desviación estándar de una señal es una medida de variabilidad de los datos.
- **Mediana:** Es el valor que se encuentra en medio de un conjunto de numeros ordenados de menor a mayor, se utiliza para resumir un conjunto de valores en un solo numero.
  
![metricas](https://github.com/user-attachments/assets/1567894b-3018-4208-961a-3eed286d741d)

**Implementación en el Código:**
    `def compute_statistics(signal):
    stats = {
        "mean": np.mean(signal, axis=0),
        "median": np.median(signal, axis=0),
        "std": np.std(signal, axis=0),
        "min": np.min(signal, axis=0),
        "max": np.max(signal, axis=0),}`

**Histograma:** Es una herramienta grafica que nos permite analizar las propiedades estadísticas y visuales de una señal, para su procesamiento y mejora.
- Visualizar la distribución de amplitudes
- Identificar características estadísticas
- Detectar ruido o anomalías
- Análisis de contraste en imágenes
- Compresión de datos
- Diseño de filtros

![histograma](https://github.com/user-attachments/assets/5b75aa83-3ab9-47df-817e-2d77e70bae2e)

El histograma muestra una distribución normal , centra en cero  y con valores positivos y negativos por lo cual podemos inferir que se realizó la transformada de manera correcta.

### Requisitos
<p>
Para ejecutar el código, es necesario instalar Python e importar las siguientes librerías:
  
- sklearn.decomposition.FastICA: separa las fuentes de audio mezcladas.  
- numpy: permite realizar operaciones matemáticas eficientes en matrices y arreglos.
- matplotlib: biblioteca estándar para crear visualizaciones.
- scipy: funciones para el diseño y aplicación de filtros.
- pyroomacoustics.Beamformer: enfoca la captura de audio en una direccion especifica. 
  
Tener instalado un compilador, que para este caso se utilizo spyder.  
</p>

### Estructura del proyecto
- load_signal(): Carga y procesamiento de la señal.
- compute_statistics(): Analisis estadistico.
- tfourier(): Transformada de fourier.
- _psd(): Densidad espectral.
- plot_signals(),plot_fourier(), plot_psd(),plot_histogram(): visualizacion.
- Lab2.py: Lee y visualiza la señal ECG desde un archivo
- LABfinal.py: Versión optimizada del procesamiento de señales ECG.  
- 01.dat y 01.hea: Archivos de datos de la señal EMG.


### Ejecución

- Asegúrate de que los archivos de datos están en la misma carpeta que los scripts.
-	Ejecuta Lab2.py o LAB2final.py para analizar la señal:
- python Lab2.py
  

### Conclusión
<p>
Este proyecto nos permite identificar las métricas estadísticas de una señal de EMG en condiciones normales, para posteriormente analizar el comportamiento de esta señal agregando diferentes tipos de ruidos y con ello calcular su SNR lo cual nos ayuda a comprender el fundamento y el impacto de estos ruido.
</p>

### Bibliografia

- Sartori, P., Rozowykniat, M., Siviero, L., Barba, G., Peña, A., Mayol, N., Acosta, D., Castro, J., & Ortiz, A. (2015). Artefactos y artificios frecuentes en tomografía computada y resonancia magnética. Revista Argentina de Radiología / Argentinian Journal Of Radiology, 79(4), 192-204. https://doi.org/10.1016/j.rard.2015.04.005
- Svantek. (2023, 27 septiembre). Ruido de impulso | ¿Cómo medir? | Consultores Svantek. SVANTEK - Sound And Vibration. https://svantek.com/es/servicios/ruido-de-impulso/#:~:text=El%20ruido%20de%20impulso%20se,inferior%20a%201%20segundo)%C2%BB.
- Learn Statistics Easily. (2024, 24 julio). Qué es: Ruido Gaussiano - APRENDE ESTADÍSTICAS FÁCILMENTE. LEARN STATISTICS EASILY. https://es.statisticseasily.com/glossario/what-is-gaussian-noise/


### Licencia

Este proyecto es de uso académico y educativo.

### Contacto
<p>
Si tienes alguna pregunta o sugerencia, no dudes en contactarme:
</p>

- **Nombre:** [Juan David Cediel Farfan][Juan Yael Barriga Roa]
- **Email:** [est.juand.cediel@unimilitar.edu.co][est.juan.barriga@unimilitar.edu.co]
- **GitHub:** [David05Cediel][JuanYBR]

