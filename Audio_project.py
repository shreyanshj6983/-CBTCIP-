import sounddevice as sd
from scipy.io.wavfile import write

def record(time, file_name):
    fs = 44100  
    seconds = time  
    
    print("Recording started for ",seconds," seconds of audio...")
    my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    
    write(file_name, fs, my_recording)
    print("Audio saved as : ",file_name)

record(5, "recorded.wav")
