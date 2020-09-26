from matplotlib.animation import FuncAnimation
import numpy as np
from numpy import sin, cos, pi
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

from matplotlib import animation
        
G = 9.81

class DoublePendulum():
    def __init__(self, M1=1, L1=1, M2=1, L2=1):
        self.M1 = M1
        self.L1 = L1
        self.M2 = M2
        self.L2 = L2

    def delta(self, theta1, theta2):
        return theta2 - theta1

    def __call__(self, t, y):
        #return derivative of y
        theta1, omega1, theta2, omega2 = y
        f = [omega1, 
             (self.M2 * self.L1 * omega1**2 * sin(self.delta(theta1, theta2)) * cos(self.delta(theta1, theta2))
              + self.M2 * G * sin(theta2)*cos(self.delta(theta1, theta2))
              + self.M2*self.L2*omega2**2 * sin(self.delta(theta1, theta2))
              - (self.M1 + self.M2)*G*sin(theta1)) / ((self.M1 + self.M2) * self.L1 - self.M2*self.L1*cos(self.delta(theta1, theta2))**2),
        omega2, 
             (-self.M2 * self.L2 * omega2**2 * np.sin(self.delta(theta1, theta2)) * np.cos(self.delta(theta1, theta2))
              + (self.M1 + self.M2) * G * np.sin(theta1) *
                 np.cos(self.delta(theta1, theta2))
              - (self.M1 + self.M2) * self.L1 * omega1**2 *
                 np.sin(self.delta(theta1, theta2))
                 - (self.M1 + self.M2) * G * np.sin(theta2)) / ((self.M1 + self.M2) * self.L2 - self.M2 * self.L1 * np.cos(self.delta(theta1, theta2))**2)]
        return f
    
    def solve(self, y0, T, dt, angles="rad"):
        self.angles = angles
        if angles == 'deg':
            y0 = y0*(pi/180)

        self.dt = dt

        t = (0, T)
        time = T/dt
        time = np.linspace(0, T, int(time))
        sol = solve_ivp(self.__call__, t, y0, t_eval=time, method = "Radau")

        self.solution_t = np.array(sol.t)
        self.solution_theta1 = np.array(sol.y[0])
        self.solution_omega1 = np.array(sol.y[1])
        self.solution_theta2 = np.array(sol.y[2])
        self.solution_omega2 = np.array(sol.y[3])
        

        self.x1 = self.L1 * sin(self.theta1)
        self.y1 = -self.L1 * cos(self.theta1)
        self.x2 = self.x1 + self.L2 * sin(self.theta2)
        self.y2 = self.y1 -self.L2 * cos(self.theta2)
        




    @property
    def x_1(self):
        return self.x1

    @property
    def y_1(self):
        return self.y1
    
    @property
    def x_2(self):
        return self.x2

    @property
    def y_2(self):
        return self.y2

    @property
    def t(self):
        return self.solution_t

    @property
    def theta1(self):
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
        return np.gradient(self.x_1, self.t)
    
    @property
    def vx2(self):
        return np.gradient(self.x_2, self.t)

    @property
    def vy1(self):
        return np.gradient(self.y_1, self.t)

    @property
    def vy2(self):
        return np.gradient(self.y_2, self.t)

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
        

    def _next_frame(self, i):
        self.pendulums.set_data((0, self.x_1[i], self.x_2[i]), (0, self.y_1[i], self.y_2[i]))
        return self.pendulums,

    def show_animation(self):
        plt.show()
    
    def save_animation(self):
        self.animation.save("example_simulation.mp4", fps = 60)
    
    
    def create_animation(self):
        # Create empty figure
        fig = plt.figure()

        # Configure figure
        plt.axis('equal')
        plt.axis('off')
        plt.axis((-3, 3, -3, 3))

        # Make an "empty" plot object to be updated throughout the animation
        self.pendulums, = plt.plot([], [], 'o-', lw=2)

        # Call FuncAnimation
        self.animation = animation.FuncAnimation(fig,
                                                 self._next_frame,
                                                 frames=range(len(self.x1)),
                                                 repeat=None,
                                                 interval=1000*self.dt,
                                                 blit=True)


if __name__ == "__main__":
    ODE = DoublePendulum(1, 1, 1, 1)
    ODE.solve([pi/2, pi/2, 0,  0], 10, 0.01)
    plt.plot(ODE.t, ODE.kinetic, color = "red", label = "Kinetic")
    plt.plot(ODE.t, ODE.potential, color = "blue", label = "Potential")
    plt.plot(ODE.t, ODE.potential + ODE.kinetic, color = "black")
    ODE.create_animation()
    ODE.show_animation()
    """print(ODE.x1)
    print(ODE.x2)
    print(ODE.vx2)
    

    plt.plot(ODE.t, ODE.y_1, color = "black", label = "Y1")
    plt.plot(ODE.t, ODE.y_2, color = "yellow", label = "Y2")
    plt.plot(ODE.t, ODE.y_1 + ODE.y_2, color = "purple", label = "y1 +Y2")

    plt.plot(ODE.t, ODE.vx1, color = "green", label = "x1")
    plt.plot(ODE.t, ODE.vx2, color = "grey", label = "x2")

    for i in range(len(ODE.t)):
        plt.axis('equal')
        plt.axis('off')
        plt.axis((-3, 3, -3, 3))
        plt.plot([ODE.x1[i], 0], [ODE.y1[i], 0])
        plt.plot([ODE.x2[i], ODE.x1[i]], [ODE.y2[i], ODE.y1[i]])
        plt.scatter(ODE.x1[i], ODE.y1[i])
        plt.scatter(ODE.x2[i], ODE.y2[i])
        plt.show()
    plt.legend()
    plt.show()
"""


