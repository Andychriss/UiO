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
        theta1, omega1, theta2, omega2 = y
        thetaD = theta2 - theta1
<<<<<<< HEAD
<<<<<<< HEAD
        f = [omega1, self.M2 * self.L1 * omega1**2 * sin(thetaD) * cos(thetaD) 
        + self.M2 * G * sin(theta2)*cos(thetaD) 
        + self.M2*self.L2*omega2**2 * sin(thetaD) 
        - (self.M1 + self.M2)*G*sin(theta1) / ((self.M1 + self.M2) * self.L1 - self.M2*self.L1*cos(thetaD)**2), omega2,

        (-self.M2 * self.L2 * omega2**2 * np.sin(thetaD) * np.cos(thetaD) \
        + (self.M1 + self.M2) * G * np.sin(theta1) * np.cos(thetaD) \
        - (self.M1 + self.M2) * self.L1 * omega1**2 * np.sin(thetaD) \
        - (self.M1 + self.M2) * G * np.sin(theta2)) / ((self.M1 + self.M2) * self.L2 - self.M2 * self.L1 * np.cos(thetaD)**2]
=======
        f = [omega1, (self.M2 * self.L1 * omega1**2 * sin(thetaD) * cos(thetaD) + self.M2 * G * sin(theta2)*cos(thetaD) + self.M2*self.L2*omega2**2 * sin(thetaD) - (self.M1 + self.M2)*G*sin(theta1)) / ((self.M1 + self.M2) * self.L1 - self.M2*self.L1*cos(thetaD)**2), omega2, (-self.M2 * self.L2 * omega2**2 * np.sin(thetaD) * np.cos(thetaD) + (self.M1 + self.M2) * G * np.sin(theta1) * np.cos(thetaD) - (self.M1 + self.M2) * self.L1 * omega1**2 * np.sin(thetaD) - (self.M1 + self.M2) * G * np.sin(theta2)) / ((self.M1 + self.M2) * self.L2 - self.M2 * self.L1 * np.cos(thetaD)**2)]
=======
        f = [omega1, 
        (self.M2 * self.L1 * omega1**2 * sin(thetaD) * cos(thetaD) 
        + self.M2 * G * sin(theta2)*cos(thetaD) 
        + self.M2*self.L2*omega2**2 * sin(thetaD) 
        - (self.M1 + self.M2)*G*sin(theta1)) / ((self.M1 + self.M2) * self.L1 - self.M2*self.L1*cos(thetaD)**2), 
        omega2, 
        (-self.M2 * self.L2 * omega2**2 * np.sin(thetaD) * np.cos(thetaD) 
        + (self.M1 + self.M2) * G * np.sin(theta1) * np.cos(thetaD) 
        - (self.M1 + self.M2) * self.L1 * omega1**2 * np.sin(thetaD) 
        - (self.M1 + self.M2) * G * np.sin(theta2)) / ((self.M1 + self.M2) * self.L2 - self.M2 * self.L1 * np.cos(thetaD)**2)]
<<<<<<< HEAD
>>>>>>> 7bc2bd9a9316704c9400191ed5a78874e1131ee5
        print(len(f))
>>>>>>> e36fcbdec3a7161c9d5554df7c53a02ee0284727
=======
>>>>>>> 1a215612b80a0989ac7fc684449b477971d85b77
        return f
    
    def solve(self, y0, T, dt, angles="rad"):
        self.angles = angles
        if angles == 'deg':
            y0 = y0*(pi/180)

        t = (0, T)
        time = T/dt
        time = np.linspace(0, T, int(time))
        sol = solve_ivp(self.__call__, t, y0, t_eval=time)

        self.solution_t = sol.t
        self.solution_theta1 = sol.y[0]
        self.solution_omega1 = sol.y[1]
        self.solution_theta2 = sol.y[2]
        self.solution_omega2 = sol.y[3]

        self.x1 = self.L1 * sin(self.solution_theta1)
        self.y1 = -self.L1 * cos(self.solution_theta1)
        self.x2 = self.x1 + self.L2 * sin(self.solution_theta2)
        self.y2 = self.y1 -self.L2 * cos(self.solution_theta2)

    @property
    def x_1(self):
        return self.x1

    @property
    def y_1(self):
        return self.y1
    
    @property
    def x_2(self):
        return self.x1

    @property
    def y_2(self):
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

    @property
    def vx1(self):
        return np.gradient(self.x_1)
    
    @property
    def vx2(self):
        return np.gradient(self.x_2)

    @property
    def vy1(self):
        return np.gradient(self.y_1)

    @property
    def vy2(self):
        return np.gradient(self.y_2)

    @property
    def potential(self):
        p_1 = self.M1 * G * (self.y_1 + self.L1)
        p_2 = self.M2 * G * (self.y_2 + self.L1 + self.L2)
        return p_1 + p_2
    
    @property
    def kinetic(self):
        k_1 = 0.5 * self.M1 * (self.vx1**2 + self.vy1**2)
        k_2 = 0.5 * self.M2 * (self.vx2**2 + self.vy2**2)
        return k_1 + k_2

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    ODE = DoublePendulum(1, 1, 1, 1)
<<<<<<< HEAD
<<<<<<< HEAD
    ODE.solve(np.array([pi/2, 0, 0, 0]), 10, 0.1)
=======
    ODE.solve([0, 0, 0, 0], 10, 0.1)
>>>>>>> e36fcbdec3a7161c9d5554df7c53a02ee0284727
=======
    ODE.solve([pi/6, pi/6, 0, 0], 10, 0.1)
>>>>>>> 1a215612b80a0989ac7fc684449b477971d85b77
    plt.plot(ODE.t, ODE.kinetic, color = "red", label = "Kinetic")
    plt.plot(ODE.t, ODE.potential, color = "blue", label = "Potential")

    plt.legend()
    plt.show()