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
                    dmin=0.0, dmax=rout, degs=0):
    d = linspace(dmin,dmax,num=100)
    theta = zeros(d.size)
    
    sinA = sin(pi*A/180.)
    sinB = sin(pi*B/180.)
    cosA = cos(pi*A/180.)
    
    for i in range(0, d.size):
        depth = d[i] - offset
        r = sqrt((depth*sinA*sinB)**2 + (r2 - depth*cosA)**2)
        theta[i] = math.asin(depth*sinA*sinB/r)

    if(degs):
        conversionfactor = 180.0/pi
    else:
        conversionfactor = 1.0
    
    plot(d, theta*conversionfactor)

    dclosest = r2*cosA/(sinA**2*sinB**2 + cosA**2)
    axvline(dclosest, ls='--', lw=1, color='k')

    xlabel("depth [cm]")
    ylabel("theta [rad]")


def plot_theta_vs_r(A=20.3, B=90, r2=rout, degs=0):
    
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

    if(degs):
        conversionfactor = 180.0/pi
    else:
        conversionfactor = 1.0
    
    plot(r, theta*conversionfactor)
    xlabel("r [cm]")
    ylabel("theta [rad]")

def plot_r_and_theta_vs_d(A=20.3, B=90, offset=0, r2=rout,
                          dmin=0.0, dmax=rout):
    d = linspace(dmin,dmax,num=200)
    r = zeros(d.size)
    theta = zeros(d.size)    

    sinA = sin(pi*A/180.)
    sinB = sin(pi*B/180.)
    cosA = cos(pi*A/180.)
    
    for i in range(0, d.size):
        depth = d[i] - offset
        r[i] = sqrt((depth*sinA*sinB)**2 + (r2 - depth*cosA)**2)
        theta[i] = math.asin(depth*sinA*sinB/r[i])

    fig = figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(d,r, 'b-', label=r"$r$")
    ax1.set_xlabel("Measurement depth [cm]")
    ax1.set_ylabel("Radius [cm]", color='b')    
    ax1.set_xlim(dmin, dmax)
    for ticklabel in ax1.get_yticklabels():
        ticklabel.set_color('b')

    ax2 = ax1.twinx()
    ax2.plot(d, theta*180.0/pi, 'g-', label=r"$\theta$")
    ax2.set_ylabel("Azimuth [degs]", color='g', rotation=270)
    ax2.set_xticks(arange(dmin, dmax+2, 2))
    ax2.set_xlim(dmin, dmax)
    for ticklabel in ax2.get_yticklabels():
        ticklabel.set_color('g')


    dclosest = r2*cosA/(sinA**2*sinB**2 + cosA**2)
    ax1.axvline(dclosest, ls='--', lw=1, color='k')


    
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

    plot(r,vrcoeff, label=r"$u_r$")
    plot(r,vtcoeff, label=r"$u_\theta$")
    plot(r,vzcoeff, label=r"$u_z$")

    title(r"$v_{udv} = \vec{v} \cdot \hat{u} = u_r v_r + u_{\theta} v_{\theta} + u_z v_z$")

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

    plot(d,vrcoeff, label=r"$u_r$")
    plot(d,vtcoeff, label=r"$u_{\theta}$")
    plot(d,vzcoeff, label=r"$u_z$")

    title(r"$v_{udv} = \vec{v} \cdot \hat{u} = u_r v_r + u_{\theta} v_{\theta} + u_z v_z$")

    dclosest = r2*cosA/(sinA**2*sinB**2 + cosA**2)
    axvline(dclosest, ls='--', lw=1, color='k')

    xlabel("depth [cm]")
    legend(loc='best')
