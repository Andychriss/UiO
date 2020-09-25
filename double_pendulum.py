import numpy as np
from numpy import sin, cos, pi
from scipy.integrate import solve_ivp

G = 9.81

class DoublePendulum():
    def __init__(self, M1=1, L1=1, M2=1, L2=1):
        self.M1 = M1
        self.L1 = L1
        self.M2 = M2
        self.L2 = L2

    def __call__(self, t, y):
        #return derivative of y
        theta1, omega1, theta2, omega2, = y
        thetaD = theta2 - theta1
        f = [(omega1, self.M2 * self.L1 * omega1**2 * sin(thetaD) * cos(thetaD) 
        + self.M2 * G * sin(theta2)*cos(thetaD) 
        + self.M2*self.L2*omega2**2 * sin(thetaD) 
        - (self.M1 + self.M2)*G*sin(theta1)) / (self.M1 + self.M2) * self.L1 - self.M2*self.L1*cos(thetaD)**2, 

        (-self.M2 * self.L2 * omega2**2 * np.sin(thetaD) * np.cos(thetaD) \
        + (self.M1 + self.M2) * G * np.sin(theta1) * np.cos(thetaD) \
        - (self.M1 + self.M2) * self.L1 * omega1**2 * np.sin(thetaD) \
        - (self.M1 + self.M2) * G * np.sin(theta2)) / ((self.M1 + self.M2) * self.L2 - self.M2 * self.L1 * np.cos(thetaD)**2)]
        return f
    
    def solve(self, y0, T, dt, angles="rad"):
        self.angles = angles
        if angles == 'deg':
            y0 = y0*(pi/180)

        t = (0, T)
        time = T/dt
        time = np.linspace(0, T, int(time))
        sol = solve_ivp(self.__call__, t, y0, t_eval=time)

        self.solution_t = np.array(sol.t)
        self.solution_theta1 = np.array(sol.y[0])
        self.solution_omega1 = np.array(sol.y[1])
        self.solution_theta2 = np.array(sol.y[2])
        self.solution_omega2 = np.array(sol.y[3])

        self.x1 = self.L1 * sin(self.solution_theta1)
        self.y1 = -self.L1 * cos(self.solution_theta1)
        self.x2 = self.x1 + self.L2 * sin(self.solution_theta2)
        self.y2 = self.y1 -self.L2 * cos(self.solution_theta2)

    @property
    def x1(self):
        return self.x1

    @property
    def y1(self):
        return self.y1
    
    @property
    def x2(self):
        return self.x1

    @property
    def y2(self):
        return self.y1



    @property
    def t(self):
        return self.solution_t

    @property
    def theta(self):
        return self.solution_theta1
    
    @property
    def theta2(self):
        return self.solution_theta2

    @property
    def omega1(self):
        return self.solution_omega1
    
    @property
    def omega2(self):
        return self.solution_omega2
