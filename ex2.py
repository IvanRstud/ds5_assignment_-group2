import matplotlib.pyplot as plt
import numpy as np



def draw_mandel(width: int):
    height = width 

    '''''''''
     sice we want the height to be equal to width so we can just put the as equal 
     and whatever input was in the functionn that will represent the height an dwith 

    '''''''''
    x = np.linspace(-1.5, 0.5, width + 1)
    y = np.linspace(-1, 1, height + 1)

    '''''''''
    lispace will divide the y and x axes to the equal 'width' number of equal spaces
    '''''''''''

    x_r, y_i = np.meshgrid(x, y)
    c = x_r + 1j * y_i  


    '''''''''''
     np.meshgrid make sure that our x and y points are represented as real and imag numbers
     wish give the opportunity of creating a complex number 'c'
    '''''''''''
    complx = np.zeros((len(y), len(x)))

    '''''''''''
    we make an array of zeros in the lenght of number of x and y numbers 
    '''''''''''
    for i in range(len(y)):  
        '''''''''
        select i from range of len(y) whic is widht 
        '''''''''       
        for j in range(len(x)): 
            '''''''''
        select i from range of len(x) whic is widht 
        '''''''''       
            z = 0                   
            h = c[i, j]
            for k in range(100):
                z = z**2 + h    
                if abs(z) > 2:  #we make sure that abs(z) is greater to 2 so that the equence diverges
                    complx[i, j] = k
                    break        
    plt.imshow(complx , extent=[x.min(), x.max(), y.min(), y.max()], cmap='hot', origin='lower')
    plt.title('Mandelbrot Set Visualization')
    plt.show()

draw_mandel(500)


        

   
