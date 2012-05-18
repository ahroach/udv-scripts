from numpy import *
from pylab import *

rin=7.06
rout = 20.30

#Plots geometric parameters as functions of the radius or depth along the
#ultrasound beam.
#The relevant angles are A, which describes the opening half-angle of a
#cone centered around the radial unit vector on which the ultrasound beam
#lies, and B, which describes the beam's position on that cone.
#B=0 corresponds to the top-most trajectory, B=90 is the right-most
#trajectory, and B=-90 is the left-most trajectory.

def plot_r_vs_d(A=20.3, B=90, offset=0, r2=rout, dmin=0.0, dmax=rout):
    d = linspace(dmin,dmax,num=100)
    r = zeros(d.size)
    
    sinA = sin(pi*A/180.)
    sinB = sin(pi*B/180.)
    cosA = cos(pi*A/180.)
    
    for i in range(0, d.size):
        depth = d[i] - offset
        r[i] = sqrt((depth*sinA*sinB)**2 + (r2 - depth*cosA)**2)

    plot(d,r)

    dclosest = r2*cosA/(sinA**2*sinB**2 + cosA**2)
    axvline(dclosest, ls='--', lw=1, color='k')
    
    xlabel("depth [cm]")
    ylabel("r [cm]")


def plot_d_vs_r(A=20.3, B=90, offset=0, r2=rout, dmin=0.0, dmax=rout):
    sinA = sin(pi*A/180.)
    sinB = sin(pi*B/180.)
    cosA = cos(pi*A/180.)

    rmin = abs(r2*sinA*sinB/sqrt(sinA**2*sinB**2 + cosA**2))
    r = linspace(rmin, r2, num=200)
    d = zeros(r.size)


    for i in range(0, r.size):
        d[i] = ((r2*cosA - sqrt(r[i]**2*(sinA**2*sinB**2 + cosA**2) -
                                r2**2*sinA**2*sinB**2)) /
                (sinA**2*sinB**2 + cosA**2))
    

    plot(r,d)
    ylabel("depth [cm]")
    xlabel("r [cm]")


def plot_theta_vs_d(A=20.3, B=90, offset=0, r2=rout,
                    dmin=0.0, dmax=rout):
    d = linspace(dmin,dmax,num=100)
    theta = zeros(d.size)
    
    sinA = sin(pi*A/180.)
    sinB = sin(pi*B/180.)
    cosA = cos(pi*A/180.)
    
    for i in range(0, d.size):
        depth = d[i] - offset
        r = sqrt((depth*sinA*sinB)**2 + (r2 - depth*cosA)**2)
        theta[i] = math.asin(depth*sinA*sinB/r)
    
    plot(d,theta)

    dclosest = r2*cosA/(sinA**2*sinB**2 + cosA**2)
    axvline(dclosest, ls='--', lw=1, color='k')

    xlabel("depth [cm]")
    ylabel("theta [rad]")


def plot_theta_vs_r(A=20.3, B=90, r2=rout):
    
    sinA = sin(pi*A/180.)
    sinB = sin(pi*B/180.)
    cosA = cos(pi*A/180.)

    rmin = abs(r2*sinA*sinB/sqrt(sinA**2*sinB**2 + cosA**2)) + 1e-8
    r = linspace(rmin, r2, num=100)
    theta = zeros(r.size)
    
    for i in range(0, r.size):
        d = ((r2*cosA - sqrt(r[i]**2*(sinA**2*sinB**2 + cosA**2) -
                             r2**2*sinA**2*sinB**2)) /
             (sinA**2*sinB**2 + cosA**2))
        theta[i] = arcsin(d*sinA*sinB/r[i])
    
    plot(r,theta)
    xlabel("r [cm]")
    ylabel("theta [rad]")


def plot_velocity_contribs_r(A=20.3, B=90, r2=rout):
    sinA = sin(A*pi/180.)
    sinB = sin(B*pi/180.)
    cosA = cos(A*pi/180.)
    cosB = cos(B*pi/180.)
    alpha = arctan(sinA*sinB/cosA)

    rmin = abs(r2*sinA*sinB/sqrt(sinA**2*sinB**2 + cosA**2)) + 1e-8
    r = linspace(rmin, r2, num=100)
    
    vrcoeff = zeros(r.size)
    vtcoeff = zeros(r.size)
    vzcoeff = zeros(r.size)
    
    for i in range(0,r.size):
        d = ((r2*cosA - sqrt(r[i]**2*(sinA**2*sinB**2 + cosA**2) -
                            r2**2*sinA**2*sinB**2)) /
             (sinA**2*sinB**2 + cosA**2))
        theta = arcsin(d*sinA*sinB/r[i])
        xi = theta + alpha
        vrcoeff[i] = -sqrt(1-sinA**2*cosB**2)*cos(xi)
        vtcoeff[i] = sqrt(1-sinA**2*cosB**2)*sin(xi)
        vzcoeff[i] = sinA*cosB

    plot(r,vrcoeff, label=r"$v_r$ coefficient")
    plot(r,vtcoeff, label=r"$v_\theta$ coefficient")
    plot(r,vzcoeff, label=r"$v_z$ coefficient")

    xlabel("r [cm]")
    legend(loc='best')


def plot_velocity_contribs_d(A=20.3, B=90, offset=0, r2=rout,
                             dmin=0.0, dmax=rout):
    
    d = linspace(dmin,dmax,num=200)
    r = zeros(d.size)
    vrcoeff = zeros(d.size)
    vtcoeff = zeros(d.size)
    vzcoeff = zeros(d.size)

    sinA = sin(A*pi/180.)
    sinB = sin(B*pi/180.)
    cosA = cos(A*pi/180.)
    cosB = cos(B*pi/180.)
    alpha = arctan(sinA*sinB/cosA)
    
    for i in range(0, d.size):
        depth = d[i] - offset
        r[i] = sqrt((depth*sinA*sinB)**2 + (r2 - depth*cosA)**2)
        
        theta = arcsin(depth*sinA*sinB/r[i])
        xi = theta + alpha
        vrcoeff[i] = -sqrt(1-sinA**2*cosB**2)*cos(xi)
        vtcoeff[i] = sqrt(1-sinA**2*cosB**2)*sin(xi)
        vzcoeff[i] = sinA*cosB

    plot(d,vrcoeff, label=r"$v_r$ coefficient")
    plot(d,vtcoeff, label=r"$v_\theta$ coefficient")
    plot(d,vzcoeff, label=r"$v_z$ coefficient")

    dclosest = r2*cosA/(sinA**2*sinB**2 + cosA**2)
    axvline(dclosest, ls='--', lw=1, color='k')

    xlabel("depth [cm]")
    legend(loc='best')
