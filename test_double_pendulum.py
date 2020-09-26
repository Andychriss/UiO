import numpy as np
from numpy import sin, cos, pi
import pytest
import double_pendulum

G = 9.81
M1 = 1
M2 = 1
L1 = 1
L2 = 1
omega1 = 0.15
omega2 = 0.15


def delta(theta1, theta2):
    return theta2 - theta1


def domega1_dt(M1, M2, L1, L2, theta1, theta2, omega1, omega2):
    return (M2 * L1 * omega1**2 * sin(delta(theta1, theta2)) * cos(delta(theta1, theta2))
            + M2 * G * sin(theta2)*cos(delta(theta1, theta2))
            + M2*L2*omega2**2 * sin(delta(theta1, theta2))
            - (M1 + M2)*G*sin(theta1)) / ((M1 + M2) * L1 - M2*L1*cos(delta(theta1, theta2))**2)


def domega2_dt(M1, M2, L1, L2, theta1, theta2, omega1, omega2):
    return (-M2 * L2 * omega2**2 * np.sin(delta(theta1, theta2)) * np.cos(delta(theta1, theta2))
    + (M1 + M2) * G * np.sin(theta1) * np.cos(delta(theta1, theta2))
        - (M1 + M2) * L1 * omega1**2 * np.sin(delta(theta1, theta2))
        - (M1 + M2) * G * np.sin(theta2)) / ((M1 + M2) * L2 - M2 * L1 * np.cos(delta(theta1, theta2))**2)


@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (0, 0, 0),
        (0, 0.5235987755982988, 0.5235987755982988),
        (0.5235987755982988, 0, -0.5235987755982988),
        (0.5235987755982988, 0.5235987755982988, 0.0),
    ],
)
def test_delta(theta1, theta2, expected):
    assert abs(delta(theta1, theta2) - expected) < 1e-10


@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (0, 0, 0.0),
        (0, 0.5235987755982988, 3.4150779130841977),
        (0.5235987755982988, 0, -7.864794228634059),
        (0.5235987755982988, 0.5235987755982988, -4.904999999999999),
    ],
)
def test_domega1_dt(theta1, theta2, expected):
    assert (
        abs(domega1_dt(M1, M2, L1, L2, theta1, theta2, omega1, omega2) - expected)
        < 1e-10
    )


@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (0, 0, 0.0),
        (0, 0.5235987755982988, -7.8737942286340585),
        (0.5235987755982988, 0, 6.822361597534335),
        (0.5235987755982988, 0.5235987755982988, 0.0),
    ],
)
def test_domega2_dt(theta1, theta2, expected):
    assert (
        abs(domega2_dt(M1, M2, L1, L2, theta1, theta2, omega1, omega2) - expected)
        < 1e-10
    )


def test_solve():
    ODE = double_pendulum.DoublePendulum(1, 1, 1, 1)
    ODE.solve([0, 0, 0, 0], 10, 0.1)
    assert np.all(ODE.theta1) == 0 and np.all(ODE.theta2) == 0 and np.all(
        ODE.omega1) == 0 and np.all(ODE.omega2) == 0 and np.array_equal(ODE.t, np.linspace(0, 10, 100))


def test_solveError():
    ODE = double_pendulum.DoublePendulum(1, 1, 1, 1)
    with pytest.raises(AttributeError):
        assert ODE.theta1 and ODE.theta2 and ODE.omega1 and ODE.omega2 and ODE.t



def test_cartesian():
    ODE = double_pendulum.DoublePendulum(1, 1, 1, 1)
    ODE.solve([0.15, pi/6, 0, 0], 10, 0.1)
    tol = 10e-7
    r = np.square(ODE.x1) + np.square(ODE.y1)

    assert abs(np.all(r) - ODE.L1**2) < tol



def test_cartesian1():
    ODE = double_pendulum.DoublePendulum(1, 1, 1, 1)
    ODE.solve([0.15, pi/6, 0, 0], 10, 0.1)
    tol = 10e-7
    r = np.square(ODE.x2) + np.square(ODE.y2)

    assert abs(np.all(r) - ODE.L2**2) < tol
