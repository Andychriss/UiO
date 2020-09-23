import numpy as np
from numpy import sin, pi
from scipy.integrate import solve_ivp


g = 9.81

class Pendulum():
    def __init__(self, theta, L = 1, M = 1):
        self.theta = theta
        self.L = L
        self.M = M
        

    def __call__(self, t, y):
        #return derivative of y
        omega, theta = y
        f = [-(g/self.L)*sin(theta), omega]
        return f

    
    def solve(self, y0, T, dt, angles):
        self.angles = angles
        if angles == 'deg':
            y0 = y0*(pi/180)

        t = (0, T)
        time = T/dt
        time = np.linspace(0, T, int(time))
        sol = solve_ivp(self.__call__, t, y0, t_eval=time)
        sol.t = np.array(sol.t)
        sol.y = np.array(sol.y)

    @property
    def t(i, dt)
        t = i * dt
        t = np.array(t)
    
    @property
    def theta(theta, t)
        theta = theta*t
        theta = np.array(theta)
    
    @property
    def omega(omega, t)
        omega = omega*t
        omega = np.array(omega)


    
