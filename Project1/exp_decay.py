from scipy.integrate import solve_ivp
import numpy as np

class ExponetialDecay():
    def __init__(self, a):
        self.a = a
    
    def __call__(self, t, u):
        #Returs the derivative of u(t)
        return -self.a * u

    def solve(self, u0, T, dt):
        t = (0, T)
        time = T/dt
        time = np.linspace(0, T, int(time))

        sol = solve_ivp(self.__call__, t, u0, t_eval=time)
        
        return sol.t, sol.y

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    decay_model = ExponetialDecay(1)
    t, u = decay_model.solve([0.5, 1, 1.5, 2], 10, .1)
    for i in u:
        plt.plot(t, i, "b")
    
    decay_model = ExponetialDecay(0.5)
    t, u = decay_model.solve([1, 1.5, 2, 2.5], 10, .1)
    for i in u:
        plt.plot(t, i, "r")
    
    plt.show()