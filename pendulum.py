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
        sol = solve_ivp(self.__call__, t, y0, t_eval=time)
        self.solution_t = np.array(sol.t)
        self.solution_theta = np.array(sol.y[0])
        self.solution_omega = np.array(sol.y[1])

        self.x = self.L * sin(self.theta)
        self.y = -self.L * cos(self.theta)

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
    
if __name__ == "__main__":
    import matplotlib.pyplot as plt

    ODE = Pendulum(2.7, 1)
    ODE.solve([1, 1], 10, 0.1)
    print("T")
    print(ODE.t)
    print("Theta")
    print(ODE.theta)
    print("Omega")
    print(ODE.omega)
    plt.plot(ODE.t, ODE.theta, color = "Green")
    plt.plot(ODE.t, ODE.omega, color = "Red")
    #plt.show()
    print("X")
    print(ODE.x)
    print("Potential")
    print(ODE.potential)
    print(ODE.y)
    print(ODE.vx)
    print(ODE.vy)
    plt.plot(ODE.t, ODE.kinetic)
    plt.show()
    