import serial
from matplotlib import pyplot as plt

x = []
y = []
data = []
with serial.Serial ('COMx', 115200) as s_port:
    s_port.write (b'0.1\r\n') # Write bytes, not a string
   
   # every line through loop reads a new line
   while True: # use an exception from last line to breakout
        s_port.readline() # results in a string
    
        try: 
            data = line.strip().split(',')
            float(data[0])
            float(data[1])
          
        except ValueError, IndexError:
            break # breaks out of loop
        else:
            x.appennd(float(data[0]))
            y.append(float(data[1]))
          
            



plt.xlabel('Time')
plt.ylabel('Something')
plt.scatter(x,y)
plt.show()

# runs step response tests
    # send characters through USB serial port to Micropython board
    # read the resulting data
    # plot the step response with correctly labeled axes and titles











                
