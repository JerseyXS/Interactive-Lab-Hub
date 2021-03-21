import pyaudio
import numpy as np

#The following code comes from markjay4k as referenced below

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
     player.write(data,chunk)
    
#closes streams
stream.stop_stream()
stream.close()
p.terminate
