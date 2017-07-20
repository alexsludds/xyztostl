import numpy as np
with open('test2sphere.txt',"w+") as f:
    for i in range(-5,6):
        for j in range(-5,6):
            if(16-i*i-j*j>=0):
                k = np.sqrt(16-i*i-j*j)
                f.write(str(i) + "," + str(j) + "," + str(k)+"\n")