import numpy as np
import matplotlib.pyplot as plt
from chaos_game import ChaosGame

class Variations:    
    def __init__(self, x, y, name):
        self.x, np.array(x)
        self.y = np.array(y)
        self.name = name
        
        #Hentet fra Appendix
        self.r = np.sqrt(self.x**2+self.y**2) 
        self.theta = np.arctan2(self.x, self.y) 
        self.phi = np.arctan2(self.y, self.x) 
        
        _func = self.name
        
    @staticmethod
    def linear(self):
        return (self.x, self.y)  
    
    @staticmethod
    def handkerchief(self):
        return (self.r*(np.sin(self.theta+self.r)), np.cos(self.theta-self.r))  

    @staticmethod
    def swirl(self):
        return (self.x*np.sin(self.r**2)-self.y*np.cos(self.r**2) , self.x*np.cos(self.r**2)+self.y*np.sin(self.r**2))

    @staticmethod
    def disc(self):
        return ((self.theta/np.pi)*np.sin(np.pi*self.r) , (self.theta/np.pi)*np.cos(np.pi*self.r))

    @staticmethod
    def polar(self):
        return (self.theta/np.pi, self.r-1)
    
    @staticmethod
    def sinusoidal(self):
        return (np.sin(self.x), np.sin(self.y))
    
    
_func = getattr(Variations, "linear")




# if __name__ == '__main__':
    #Oppgave 4b
        #Testkode fra oppgaven
    # plt.figure()
    # plt.scatter(u, -v, s=0.2, marker=".")
    # ax.plot(u, -v, markersize=1, marker=".", linestyle="")
    # plt.savefig("variations_4b.png")

    # grid_values = np.linspace(-1, 1, N)
    # x, y = np.meshgrid(grid_values, grid_values)
    # x_values = x.flatten()
    # y_values = y.flatten()
    

    # transformations = ["linear", "handkerchief", "swirl", "disc", "polar", "sinusodial"]
    # variations = [Variations(x_values, y_values, version) for version in transformations]

    # fig, axs = plt.subplots(2, 2, figsize=(9, 9))
    # for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):
        
    
    #     u, v = variation.transform()
    
    #     ax.plot(u, -v, markersize=1, marker=".", linestyle="", color="black")
    #     # ax.scatter(u, -v, s=0.2, marker=".", color="black")
    #     ax.set_title(variation.name)
    #     ax.axis("off")

    # fig.savefig("figures/variations_4b.png")
    # plt.show()    
