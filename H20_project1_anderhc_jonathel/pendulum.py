import numpy as np
from numpy import sin, cos, pi
from scipy.integrate import solve_ivp


g = 9.81

class Pendulum():
    """Simulates the movement of a single pendulum

    Keyword arguments:
    L -- Length of the rod connecting the pendulum object to origo
    M -- Mass of the pendulum object (Default 1)
    """
    def __init__(self, L=1, M=1):
        self.L = L
        self.M = M
        

    def __call__(self, t, y):
        """Returns derivative of y
        """
        omega, theta = y
        f = [-(g/self.L)*sin(theta), omega]
        return f

    
    def solve(self, y0, T, dt, angles = "rad"):
        """
        Solves the differential equation using the Radau method

        Keyword arguments:
        y0 -- The initial conditions for the 
        pendulum should be passed as a list
        T -- The time frame of the simulation, starts from 0
        dt -- The amount of time between each simulation step
        angles -- The format in which the angle is given (deafult "rad")
        """
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
        """Calculates the potential energy of the pendulum
        """
        return self.M * g * (self.y + self.L)

    @property
    def vx(self):
        """ Calculates the rate of change of the x list of values
        """
        return np.gradient(self.x, self.t)
    
    @property
    def vy(self):
        """Calculates the rate of change of the y list of values
        """
        return np.gradient(self.y, self.t)
    
    @property
    def kinetic(self):
        """Calculates the kinetic energy of the pendulum
        """
        return 0.5 * self.M * (self.vx**2 + self.vy**2)
    
class DampenedPendulum(Pendulum):
    """Simulates the movement of a single pendulum

    Keyword arguments:
    L -- Length of the rod connecting the pendulum object to origo
    M -- Mass of the pendulum object (Default 1)
    B -- The damping parameter (Default 0)
    """
    def __init__(self,L = 1, M = 1, B = 0):
        self.L = L
        self.M = M
        self.B = B

    def __call__(self, t, y):
        """Returns the derivative of y, which 
        should be the two values omega and theta
        
        """

        omega, theta = y
        f = [-(g/self.L)*sin(theta) - (self.B/self.M) * omega, omega]
        return f
        
if __name__ == "__main__":
    """Plots the x and y values of the solve 
    function with inputs set to y0 = pi/2, 1 T = 10 and dt = 0.01
    Also plots the kinetic, potential and total energy of the pendulum
    """
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

    plt.plot(t, kinetic, color="yellow", label="kinetic")
    plt.plot(t, potential, color="green", label="potential")

    plt.plot(t, total, color="black", label="Total Energy")
    plt.legend()
    plt.show()
