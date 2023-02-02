import serial
from matplotlib import pyplot as plt

x = []
y = []
data = []
with serial.Serial ('COMx', 115200) as s_port:
    for lineline in s_port:
        try: 
            data = line.strip().split(',')
            float(data[0])
            float(data[1])
          
        except ValueError:
            continue # go to the next iteration of the loop
        
    s_port.write (b'something') # Write bytes, not a string


plt.xlabel(header[0])
plt.ylabel(header[1])
plt.scatter(x,y)
plt.show()

# runs step response tests
    # send characters through USB serial port to Micropython board
    # read the resulting data
    # plot the step response with correctly labeled axes and titles











                
