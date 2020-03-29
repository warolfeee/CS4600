import os
import matplotlib.pyplot as plt

import librosa #for loading and visualizing audio files
import librosa.display

def main():
    audio_fpath = "./nraven/"
    audio_clips = os.listdir(audio_fpath)

    filename = 0

    for i in range(len(audio_clips)):
        x, sr = librosa.load(audio_fpath + audio_clips[i], sr=None)
        # loads an audio file as a floating point time series. sr is the target sampling rate

        duration = int(librosa.get_duration(x, sr))
        for j in range(duration-2):
            spectrogram(audio_fpath + audio_clips[i], filename, j, 2)
            filename += 1

def spectrogram(finalPath, filename, start, stop):

    x, sr = librosa.load(finalPath, offset=float(start), duration=float(stop), sr=None)

    X = librosa.stft(x) # short-time fourier transform
    # STFT represents a signal in time-frequency domain by computing
    # discrete Fourier transforms (DFT) over short overlapping windows
    # this function returns a complex-valued matrix D such that:
    # abs(D[f,t]) = the magnitude of frequency bin f at frame t

    Xdb = librosa.amplitude_to_db(abs(X)) # this converts an amplitude spectrogram
    # to a dB-scaled spectrogram (``S`` measured in dB)

    plt.figure(figsize=(4,6)) # width and hieight in inches
    p = librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')

    #Save image file
    plt.savefig("nraven%s.png" % filename)

main()
