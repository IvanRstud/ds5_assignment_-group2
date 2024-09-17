import matplotlib.pyplot as plt
import numpy as np

def draw_mandel(width):
    height = width 
    x = np.linspace(-1.5, 0.5, width + 1)
    y = np.linspace(-1, 1, height + 1)
    x_r, y_i = np.meshgrid(x, y)
    c = x_r + 1j * y_i  
    complx = np.zeros((len(y), len(x)))
    for i in range(len(y)):          
        for j in range(len(x)):      
            z = 0                   
            h = c[i, j]
            for k in range(100):
                z = z**2 + h    
                if abs(z) > 2:  
                    complx[i, j] = k
                    break        
    plt.imshow(complx , extent=[x.min(), x.max(), y.min(), y.max()], cmap='hot', origin='lower')
    plt.title('Mandelbrot Set Visualization')
    plt.show()

draw_mandel(500)


        

   
