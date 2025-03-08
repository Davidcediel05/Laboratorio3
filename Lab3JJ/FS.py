import librosa
archivo = r"C:\Users\juany\OneDrive\Escritorio\LabSeñales\Lab3\CedielSeñal.wav"  # Nombre del archivo
_, sr = librosa.load(archivo, sr=None)  # Carga sin modificar la frecuencia
print(f"Frecuencia de muestreo original: {sr} Hz")

