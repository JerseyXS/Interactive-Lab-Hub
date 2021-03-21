import pyaudio
import numpy as np

def audio_datalist_set_volume(datalist, volume):
    """ Change value of list of audio chunks """
    sound_level = (volume / 100.)

    for i in range(len(datalist)):
        chunk = np.fromstring(datalist[i], np.int16)

        chunk = chunk * sound_level

        datalist[i] = chunk.astype(np.int16)

chunk=4096
RATE=44100

p=pyaudio.PyAudio()

#input stream setup
stream=p.open(format = pyaudio.paInt16,rate=RATE,channels=1, input_device_index = 2, input=True, frames_per_buffer=chunk)

#the code below is from the pyAudio library documentation referenced below
#output stream setup
player=p.open(format = pyaudio.paInt16,rate=RATE,channels=1, output=True, frames_per_buffer=chunk)

while True:            #Used to continuously stream audio
     data=np.fromstring(stream.read(chunk,exception_on_overflow = False),dtype=np.int16)
     audio_datalist_set_volume(data, 90)
     player.write(data,chunk)
    
#closes streams
stream.stop_stream()
stream.close()
p.terminate
