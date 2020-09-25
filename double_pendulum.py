

class DoublePendulum()
    def __init__(self, M1=1, L1=1, M2=1, L2=1):
    self.M1 = M1
    self.L1 = L1
    self.M2 = M2
    self.L2 = L2

    def __call__(self, t, y):
        #return derivative of y
        theta1, omega1, theta2, omega2, = y
        f = [omega1, -(g/self.L)*sin(theta1), omega2, -(g/self.L)*sin(theta2)]
        return f
