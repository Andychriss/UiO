import numpy as np
from numpy import sin, cos, pi
from scipy.integrate import solve_ivp


g = 9.81

class Pendulum():
    def __init__(self, L = 1, M = 1):
        self.L = L
        self.M = M
        

    def __call__(self, t, y):
        #return derivative of y
        omega, theta = y
        f = [-(g/self.L)*sin(theta), omega]
        return f

    
    def solve(self, y0, T, dt, angles = "rad"):
        self.angles = angles
        if angles == 'deg':
            y0 = y0*(pi/180)

        t = (0, T)
        time = T/dt
        time = np.linspace(0, T, int(time))
        sol = solve_ivp(self.__call__, t, y0, t_eval=time, method="Radau")

        self.solution_t = np.array(sol.t)
        self.solution_theta = np.array(sol.y[1])
        self.solution_omega = np.array(sol.y[0])

        self.x1 = self.L * sin(self.theta)
        self.y1 = -self.L * cos(self.theta)

    @property
    def x(self):
        return self.x1

    @property
    def y(self):
        return self.y1

    @property
    def t(self):
        return self.solution_t
    
    @property
    def theta(self):
        return self.solution_theta
    
    @property
    def omega(self):
        return self.solution_omega

    @property
    def potential(self):
        return self.M * g * (self.y + self.L)

    @property
    def vx(self):
        return np.gradient(self.x, self.t)
    
    @property
    def vy(self):
        return np.gradient(self.y, self.t)
    
    @property
    def kinetic(self):
        return 0.5 * self.M * (self.vx**2 + self.vy**2)
    
class DampenedPendulum(Pendulum):
    def __init__(self,L = 1, M = 1, B = 0):
        self.L = L
        self.M = M
        self.B = B

    def __call__(self, t, y):
        #return derivative of y
        omega, theta = y
        f = [-(g/self.L)*sin(theta) - (self.B/self.M) * omega, omega]
        return f
        
if __name__ == "__main__":
    import matplotlib.pyplot as plt

    ODE = DampenedPendulum(1, 1)
    ODE.solve([pi/2, 1], 10, 0.01)
    t = ODE.t
    x = ODE.x
    y = ODE.y
    plt.plot(t, x, color = "red", label = "x")
    plt.plot(t, y, color = "blue", label = "y")

    kinetic = ODE.kinetic
    potential = ODE.potential
    total = kinetic + potential

    plt.plot(t, kinetic, color = "yellow", label = "kinetic")
    plt.plot(t, potential, color = "green", label = "potential")

    plt.plot(t, total, color = "black", label = "Total Energy")
    plt.legend()
    plt.show()