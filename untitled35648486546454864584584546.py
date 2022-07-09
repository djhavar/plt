import numpy as np
import matplotlib.pyplot as plt

def pdf(x):
    mean = np.mean(x)
    std = np.std(x)
    y_out = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x-mean)**2 / (2 * std**2))
    return y_out

x = np.arange(-7,7,0.05)

y = pdf(x)

plt.style.use('seaborn')
plt.figure(figsize =(5,5))
plt.plot(x,y,  color= 'red', 
        linestyle = 'dashed')
plt.scatter(x,y, marker='.', s=25, color ='red')
plt.show()