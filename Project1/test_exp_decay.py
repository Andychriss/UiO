import exp_decay
import pytest


def test_ExpontentialDecay():
    ODE = exp_decay.ExponetialDecay(0.4)
    ODEder = ODE(1, 3.2)
    tol = 10e-7
    assert abs(ODEder - (-1.28)) < tol
