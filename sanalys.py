import numpy as np    #need to pyplot work
import pyaudio as pa  #for works with microphone 
import struct 
import matplotlib.pyplot as plt #for graph


###############################################################################
#                          Audio signal recieving                             #
###############################################################################

buf = 1024 * 2 #lengh of buffer
fr = pa.paInt16
ch = 1     #adress of microphone on pc
hz = 44100     # RATE in Hz

p = pa.PyAudio()    

stream = p.open(        #streaming params:
    format = fr,
    channels = ch,
    rate = hz,
    input=True,
    output=True,
    frames_per_buffer=buf
)

###############################################################################
#                        Work with GUI and plot                               #
###############################################################################




fig,ax = plt.subplots()
x = np.arange(0,2*buf,2)
line, = ax.plot(x, np.random.rand(buf),'b')
ax.set_ylim(-35000,35000)          #amplitude, may to change
ax.ser_xlim = (0,buf)
fig.show()

while 1:     #audio chanel
    data = stream.read(buf)
    dataInt = struct.unpack(str(buf) + 'h', data)
    line.set_ydata(dataInt)
    fig.canvas.draw()
    fig.canvas.flush_events()
   
