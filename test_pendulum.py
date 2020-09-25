
import pendulum
import pytest
import numpy as np
from numpy import pi


@pytest.mark.parametrize(
    "y", [(-109/60, 0.15)]
)
def test_pendulum(y):
    ODE = pendulum.Pendulum(2.7, 1)
    ODEder = ODE(0, [0.15, pi/6])
    tol = 10e-7
    assert abs(ODEder[0] - y[0]) < tol
    assert abs(ODEder[1] - y[1]) < tol


def test_solve():
    ODE = pendulum.Pendulum(1, 1)
    ODE.solve([0, 0], 10, 0.1)
    assert np.all(ODE.theta) == 0 and np.all(ODE.omega) == 0 and np.array_equal(ODE.t, np.linspace(0, 10, 100))

def test_solveError():
    ODE = pendulum.Pendulum(1, 1)
    with pytest.raises(AttributeError):
        assert ODE.theta and ODE.omega and ODE.t

@pytest.mark.parametrize(
    "y", [(-109/60, 0.15)]
)
def test_cartesian(y):
    ODE = pendulum.Pendulum(1, 1)
    ODE.solve([0.15, pi/6], 10, 0.1)
    tol = 10e-7
    r = np.square(ODE.x1) + np.square(ODE.y1)

    assert abs(np.all(r) - ODE.L**2) < tol


