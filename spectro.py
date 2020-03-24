import os
import matplotlib.pyplot as plt

#for loading and visualizing audio files
import librosa
import librosa.display

def main():
    audio_fpath = "./nraven/"
    audio_clips = os.listdir(audio_fpath)

    for i in range(len(audio_clips)):
        spectrogram(audio_fpath + audio_clips[i], i)

def spectrogram(finalPath, i):
    x, sr = librosa.load(finalPath, sr=44100)
    
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(14, 5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar()

    plt.figure(figsize=(14, 5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar()

    #Save image file
    plt.savefig("nraven%s.png" % i)

main()
