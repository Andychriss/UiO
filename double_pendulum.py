import numpy as np
from numpy import sin, cos, pi

class DoublePendulum()
    def __init__(self, M1=1, L1=1, M2=1, L2=1):
    self.M1 = M1
    self.L1 = L1
    self.M2 = M2
    self.L2 = L2

    def __call__(self, t, y):
        #return derivative of y
        theta1, omega1, theta2, omega2, = y
        thetaD = theta2 - theta1
        f = [(omega1, self.M2 * self.L1 * omega1**2 * sin(thetaD) * cos(thetaD) + self.M2*g*sin(theta2)*cos(thetaD) + M2*L2*omega2**2 * sin(thetaD) - (M1 + M2)*g*sin(theta1))
        / (M1 + M2) * L1 - M2*L1*cos(thetaD)**2, omega2, ]
        return f
