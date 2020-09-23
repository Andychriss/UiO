
import pendulum
import pytest
from numpy import pi


@pytest.mark.parametrize(
    "x", [(-109/60, 0.15)]
)
def test_pendulum(x):
    ODE = pendulum.Pendulum(pi/6, 2.7, 1)
    ODEder = ODE(0, [0.15, pi/6])
    tol = 10e-7
    assert abs(ODEder[0] - x[0]) < tol
    assert abs(ODEder[1] - x[1]) < tol
