import os
import matplotlib.pyplot as plt

#for loading and visualizing audio files
import librosa
import librosa.display

def main():
    audio_fpath = "./nraven/"
    audio_clips = os.listdir(audio_fpath)

    for i in range(len(audio_clips)):
        x, sr = librosa.load(audio_fpath + audio_clips[i], sr=44100)
        # loads an audio file as a floating point time series. sr is the target sampling rate

        duration = int(librosa.get_duration(x, sr))
        for j in range(duration):
            spectrogram(audio_fpath + audio_clips[i], j, j, j+2)

def spectrogram(finalPath, filename, start, stop):

    x, sr = librosa.load(finalPath, offset=start, duration=stop, sr=44100)
    
    X = librosa.stft(x) # short-time fourier transform
    # STFT represents a signal in time-frequency domain by computing
    # discrete Fourier transforms (DFT) over short overlapping windows
    # this function returns a complex-valued matrix D such that:
    # abs(D[f,t]) = the magnitude of frequency bin f at frame t
    
    Xdb = librosa.amplitude_to_db(abs(X)) # this converts an amplitude spectrogram
    # to a dB-scaled spectrogram (``S`` measured in dB)

    plt.figure() # width and hieight in inches
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar() # Creates a colorbar for a ScalarMappable instance

    #Save image file
    plt.savefig("nraven%s.png" % filename)

main()
