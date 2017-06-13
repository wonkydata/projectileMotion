
# coding: utf-8

# In[4]:

# projectileDistance - calculator for finding projectile distances to target, given velocity and angle 
#
# V: velocity is vertical and horizontal. Vertical velocity is a constant (g) gravity. Wind resistance not calculated
# horizontal velocity is user entered (velocity at origin or V0)
#
# R: alternative: R = (v^2/g)*sin(2*a)
# Ag: acceleration of gravity seen as a constant 9.81 m/s^2 (Newton's law)
# 
# Y = Height of object in any X (distance) along path of trajectory.
# Y = y0 * (x*tan(a)) - (g*x^2)/ (2(v * cos(a))^2)
# In Py: y = yOrig * (x *math.tan(a)) - (g * x**2)/(2*(v * cos(a))**2)

import matplotlib.pyplot as plot 
import numpy as np 
import math
import scipy.constants as const
import time
import sys

# Reference https://www.physicsforums.com/threads/using-python-to-calculate-projectile-motion-with-resistance.848512/



# In[ ]:


# Spinning cursor
def spinning_cursor():
    x = 0
    
    while x < 6:
        for cursor in '\\|/-':
            time.sleep(0.1)
            # Use '\r' to move cursor back to line beginning
            # Or use '\b' to erase the last character
            sys.stdout.write('\r{}'.format(cursor))
            # Force Python to write data into terminal.
            sys.stdout.flush()
            x += 1
    sys.stdout.flush()
    return('')


def main():
    
    while True:
    
        # Newton's constant for the vertical velocity of gravity in m/s
        g = 9.81

        while True:
            velo = input('Type in your Velocity? (m/s) ')

            if float(velo) > 299792458:
                print('Faster than the Millenium Falcon? Chewy is impressed... and also not... ')
                print(' ')
                continue 
            if float(velo) > 16260:
                print('Faster than New Horizons spacecraft on it\'s way to Pluto? Maybe not... ')
                print(' ')
                continue
            if float(velo) > 1219:
                print('Faster than the fastest bullet? Superman?... Nope. ')
                print(' ')
                continue
            else:
                #we're happy with the value given.
                #we're ready to exit the loop.
                break

        while True:
            angl = input('What is your Angle? (in degrees) ')

            if float(angl) >  90:
                print('Are you trying to send it behind you? ')
                print(' ')
                continue 

            else:
                #we're happy with the value given.
                #we're ready to exit the loop.
                break

        if float(angl) >  89:
                print('You\'re sending it vertical. Ouch! ')
                print(' ')



        while True:

            dist = input('Guess where it will land (meters) ')

            if float(dist) < 0:
                print('Can\'t go into the past... Positive number please... ')
                print(' ')
                continue 

            if float(dist) < 1:
                print('No Zero distance please. ')
                print(' ')
                continue 

            else:
                #we're happy with the value given.
                #we're ready to exit the loop.
                break

        if float(dist) == 1:
            print(' ')
            print('Wow. 1 meter? OK. ')
            print(' ')


        print (' ')
        print ('--------------------------------')
        print ('Velocity ',velo, ' m/s')
        print ('Angle ', angl,' degrees', round(math.radians(float(angl)),3),' radians')
        print ('Estimated Distance (ED) ', dist, ' meters')
        print ('')

        # Fill vars for R formula
        ivelo = float(velo)
        iangl = float(angl)    
        dbliangl = 2*iangl

        # Sin looks for radians
        # The Range formula: distR = (v^2/g)*sin(2*a)
        # T = distance/velocity == distR/ivelo
        sinangle = math.sin(math.radians(dbliangl))
        ivelosq = ivelo**2

        # Range formula
        distR = (ivelosq/float(g)) * sinangle

        print('++++++++++++++++++++++++++++++++', spinning_cursor())
        print('')
        print('Actual Range = ', round(distR,2), ' meters.')
        print('Time to target = ', round(distR/ivelo,2), ' seconds.')
        print('Angle needed for ED: ', round(math.degrees((1/2 * (math.asin((g*float(dist))/ivelosq)))),2))

        aNeeded = round((1/2 * (math.asin((g*float(dist))/ivelosq))),2)

        # specific values test for Trig formulas
        # R: alternative: R = (v^2/g)*sin(2*a)
        # testing with R = (42^2/9.81) * sin(2*7.0)
        # answer should be 43.501
        ###
        #specificVals = ((math.pow(42,2)/9.81)*math.sin(2*(math.radians(7.0))))
        #print(' ')
        #print('specificVals test ',specificVals)
        #print('sin of 2*7 angle ', math.sin(2*7.0))
        #print(' ')

        rDiff = float(distR) - float(dist)
        rAvg = (float(distR) + float(dist))/2
        prDiff = round(((rDiff/rAvg ) * 100),2)

        thresH = float(5.0)

        # **
        # Print accuracy to user
        print(' ')
        if rDiff < 0:
            print('Your Range estimate was OVER by ', round(-(rDiff),2),' meters, or ', -(prDiff),'%')
            if -rDiff < float(thresH):
                print('Nice work!')
            else:
                print('Try again!! ')
        else:
            print('Your Range estimate was UNDER by ', round((rDiff),2),' meters, and within ', (round((prDiff),2)),'%')
            if round(rDiff) < float(thresH):
                print('Nice work!')
            else:
                print('Try again!! ')

        #############################################
        # Plot the paraballa using matplotlib.pyplot
        t = np.linspace(0, 2, num=dist) # Set time as 'continous' parameter.

        ix = math.radians(iangl)
        theta = [ix, aNeeded] # ix is angle entered, aNeeded is angle required for estimated distance
        v = ivelo

        for i in theta: # Calculate trajectory for each angle in list

            x1 = []
            y1 = []
            for k in t:
                x = ((v*k)*np.cos(i)) # get positions at every point in time
                y = ((v*k)*np.sin(i))-((0.5*g)*(k**2))
                x1.append(x)
                y1.append(y)

            p = [i for i, j in enumerate(y1) if j < 0] # Don't fall through the floor 
            for i in sorted(p, reverse = True):
                del x1[i]
                del y1[i]

            plot.plot(x1, y1) # Plot for every angle

        # Format and plot a plot    
        plot.xlabel('Distance (m)')
        plot.ylabel('Height (m)')    
        plot.title('Your throw in blue, predicted in red')

        print(' ')
        print('## Here\'s how your throw would look ##')
        plot.show() # And show on one graphic       
    
        #####
        print(' ')   
        tryAgain = input('Try again? (y/n) ')       

        yES = ['y','Y','Yes','YES','yes']
        nO = ['n','N','No','NO','no']
 
        if tryAgain in yES:
            continue 
        if tryAgain in nO:
            break 
        else:
            print('Goodbye')
            break


       
if __name__ == '__main__':
    main()


# #### 

# In[ ]:




# In[ ]:



