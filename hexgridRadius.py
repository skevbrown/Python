
import numpy as np
import matplotlib.pyplot as plt
import math
import cmath as cm
#from scipy.integrate import odeint
#from mpl_toolkits.mplot3d import Axes3D

def rect(r, theta):
    """theta in radians

    returns tuple; (float, float); (x,y)
    """
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x,y

def polar(x, y):
    """returns r, theta(radians)
    """
    r, theta = cm.polar( complex(x,y) );
    return r, theta



polarvec = np.vectorize(polar); # Vectorize these func's to operate on vectors
rectvec  = np.vectorize(rect);


dotsperquad = 20
introw = np.arange(0,dotsperquad); halfrow = np.arange(0.5,dotsperquad,1.0);
column = np.arange(0,dotsperquad*np.sqrt(3)/2,np.sqrt(3)/2)
totalRows = dotsperquad*dotsperquad

inthalf = np.concatenate([introw,halfrow ],axis=0)

print(len(inthalf)); print( column)



xaxis = np.concatenate( [[inthalf]*int(dotsperquad/2) ])
xaxis = xaxis.flatten()
#xaxis = np.concatenate( [xaxis,xaxis, xaxis*-1, xaxis*-1] );
xaxis = xaxis.flatten()
#print( xaxis )

yaxis = []
for value in column:
    yaxis = np.concatenate( [yaxis, [ value ] * dotsperquad  ]  )
    yaxis = yaxis.flatten()

#yaxis = np.concatenate( [yaxis,yaxis*-1, yaxis, yaxis*-1] );
yaxis = yaxis.flatten()

print( len(yaxis) )

hexMatr = np.zeros( len(xaxis), dtype=[('xaxis','f8'), ('yaxis','f8'),('rad','f8'),('angle','f8'),('angdeg','f8') ]  )
hexMatr['xaxis'] = xaxis; hexMatr['yaxis'] = yaxis;
r, theta = polarvec(hexMatr['xaxis'], hexMatr['yaxis']  )
hexMatr['rad'] = r
#hexMatr['rad'] = np.sqrt( hexMatr['xaxis']**2 +  hexMatr['yaxis']**2 )


hexMatr['angle'] = theta; hexMatr['angdeg'] = theta*180/np.pi;

hexMatr.sort(order='xaxis')

angleVec = hexMatr['angdeg']


print(hexMatr[0:200] )

angSet1 = []

for ii in range(0,len(hexMatr) ):
    if hexMatr['angdeg'][ii] < 61:
        angSet1.append(hexMatr['angdeg'][ii])

angSet1uniq = np.unique(angSet1)
angSet2uniq = angSet1uniq[ np.arange(0, len(angSet1uniq), 4 ) ]
angSet3uniq = angSet1uniq[ np.arange(1, len(angSet1uniq), 4 ) ]
angSet4uniq = angSet1uniq[ np.arange(2, len(angSet1uniq), 4 ) ]


plt.figure()
plt.plot(xaxis,yaxis,'b.', markersize=3.5 )
for ii in range(0,len(angSet2uniq)):
    xpnt, ypnt = rect(10.0, angSet2uniq[ii]*np.pi/180 )
    pltArray = np.array([ [0,xpnt], [0, ypnt] ] )
    plt.plot(pltArray[0,:],pltArray[1,:], 'r', linewidth=0.6 )
#for ii in range(0,len(angSet3uniq)):
#    xpnt, ypnt = rect(10.0, angSet3uniq[ii]*np.pi/180 )
#    pltArray = np.array([ [0,xpnt], [0, ypnt] ] )
#    plt.plot(pltArray[0,:],pltArray[1,:], 'b', linewidth=0.6 )
for ii in range(0,len(angSet4uniq)):
    xpnt, ypnt = rect(10.0, angSet4uniq[ii]*np.pi/180 )
    pltArray = np.array([ [0,xpnt], [0, ypnt] ] )
    plt.plot(pltArray[0,:],pltArray[1,:], 'g', linewidth=0.6 )



plt.xlim(-2,dotsperquad+1); plt.ylim(-2,dotsperquad+1) ;
plt.gca().set_aspect('equal', adjustable='box')

plt.figure()
plt.plot(hexMatr['rad'],angleVec,'r.', markersize=3.7)
#plt.xlim(20,25)


plt.figure()
plt.plot( [ 10 ] * len(angleVec), angleVec,'r.', markersize=3.7)



plt.show()

#print(np.arccos(0.5) )

