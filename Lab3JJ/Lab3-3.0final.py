import librosa
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from sklearn.decomposition import FastICA
from scipy.signal import welch

# Cargar archivos de audio
audio1, sr1 = librosa.load(r'C:\Users\juany\OneDrive\Escritorio\LabSeñales\Lab3\CedielSeñal.wav',sr=48000)
audio2, sr2 = librosa.load(r'C:\Users\juany\OneDrive\Escritorio\LabSeñales\Lab3\lab3juanySeñal.wav',sr=48000)
ruido1, sr3 = librosa.load(r'C:\Users\juany\OneDrive\Escritorio\LabSeñales\Lab3\CedielAmb.wav',sr=48000)
ruido2, sr4 = librosa.load(r'C:\Users\juany\OneDrive\Escritorio\LabSeñales\Lab3\lab3juanyAmb.wav',sr=48000)


# Mostrar frecuencias de muestreo
print(f"Frecuencia de muestreo de Cediel: {sr1} Hz")
print(f"Frecuencia de muestreo de Juany: {sr2} Hz")

# Calcular la relación señal-ruido (SNR)
def snr_calculo(señal, ruido):
    pseñal = np.mean(señal ** 2)
    pruido = np.mean(ruido ** 2)
    snr = 10 * np.log10(pseñal / pruido)
    return snr

snr1 = snr_calculo(audio1, ruido1)
snr2 = snr_calculo(audio2, ruido2)
print(f"SNR Cediel: {snr1} dB")
print(f"SNR Juany: {snr2} dB")

# Graficar señales
def graficar_señal(señal, titulo, color):
    plt.figure(figsize=(12, 6))
    plt.title(titulo)
    plt.plot(señal, color=color)
    plt.xlabel('Muestras')
    plt.ylabel('Amplitud (dB)')
    plt.tight_layout()
    plt.show()

graficar_señal(audio1, 'Señal Cediel', 'blue')
graficar_señal(audio2, 'Señal Juany', 'yellow')


# Análisis espectral
def graficar_espectro(señal, sr, titulo, color):
    freqs = np.fft.rfftfreq(len(señal), 1/sr)
    espectro = np.abs(np.fft.rfft(señal))
    
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.title(f'Espectro Lineal de {titulo}')
    plt.plot(freqs, espectro, color=color)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud')
    
    plt.subplot(2, 1, 2)
    plt.title(f'Espectro Logarítmico de {titulo}')
    plt.plot(freqs, 20 * np.log10(espectro + 1e-10), color=color)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud (dB)')
    plt.tight_layout()
    plt.show()
#Analisis en funcion de la frecuencia
def graficar_psd(señal, sr, titulo, color):
    freqs, psd = welch(señal, sr, nperseg=1024)
    plt.figure(figsize=(12, 6))
    plt.semilogy(freqs, psd, color=color)
    plt.title(f'Densidad Espectral de Potencia de {titulo}')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Densidad espectral de potencia [V^2/Hz]')
    plt.tight_layout()
    plt.show()

graficar_espectro(audio1, sr1, 'Cediel', 'blue')
graficar_espectro(audio2, sr2, 'Juany', 'yellow')


graficar_psd(audio1, sr1, 'Cediel', 'blue')
graficar_psd(audio2, sr2, 'Juany', 'yellow')


# Beamforming
def calcular_retraso(distancias, velocidad, sr):
    return tuple(int(d / velocidad * sr) for d in distancias)

distancias = [3.0, 3.0]  # Distancia entre micrófonos en metros
velocidad_sonido = 343  # Velocidad del sonido en m/s
retraso = calcular_retraso(distancias, velocidad_sonido, sr1)

def beamforming(signals, delay):
    num_mics = signals.shape[1]
    beamformed_signal = np.zeros(len(signals))
    for i, delay_i in enumerate(delay):
        beamformed_signal += np.roll(signals[:, i], -delay_i)
    return beamformed_signal / num_mics

# Asegurar que ambas señales tengan la misma longitud
longitud_max = max(len(audio1), len(audio2))
audio1 = np.pad(audio1, (0, longitud_max - len(audio1)))
audio2 = np.pad(audio2, (0, longitud_max - len(audio2)))
audio_mix = np.vstack((audio1, audio2)).T

# Aplicar beamforming
beamformed_signal = beamforming(audio_mix, retraso)
output_file = r'C:\Users\juany\OneDrive\Escritorio\LabSeñales\Lab3\señal_beamformed.wav'
sf.write(output_file, beamformed_signal, sr1)

graficar_señal(beamformed_signal, 'Señal después de Beamforming', 'orange')
graficar_espectro(beamformed_signal, sr1, 'Señal Beamforming', 'orange')
graficar_psd(beamformed_signal, sr1, 'Señal Beamforming', 'orange')

# Aplicar Análisis de Componentes Independientes (ICA)
ica = FastICA(n_components=2)
señales_separadas = ica.fit_transform(audio_mix)
señal_ica = señales_separadas[:, 0]

# Normalizar señal ICA
señal_ica = señal_ica / np.max(np.abs(señal_ica))

output_file_ica = r'C:\Users\juany\OneDrive\Escritorio\LabSeñales\Lab3\señal_ica.wav'

sf.write(output_file_ica, señal_ica, sr1)

graficar_señal(señal_ica, 'Señal después de ICA', 'cyan')
graficar_espectro(señal_ica, sr1, 'Señal ICA', 'cyan')
graficar_psd(señal_ica, sr1, 'Señal ICA', 'cyan')

# Asegurar que ambas señales de ruido tengan la misma longitud
longitud_max_ruido = max(len(ruido1), len(ruido2))
ruido1 = np.pad(ruido1, (0, longitud_max_ruido - len(ruido1)))
ruido2 = np.pad(ruido2, (0, longitud_max_ruido - len(ruido2)))
señal_suma = ruido1 + ruido2

# Calcular SNR final
SNR_FINAL_BEAM = snr_calculo(beamformed_signal, señal_suma)
SNR_FINAL_ICA = snr_calculo(señal_ica, señal_suma)

print(f"SNR FINAL después de Beamforming: {SNR_FINAL_BEAM} dB")
print(f"SNR FINAL después de ICA: {SNR_FINAL_ICA} dB")
