"""Numerical primitives used by the immutable cumulative verifier.

The Gaussian checks are intentionally independent of the released neural
sampler. They regression-test the already-judged theoretical evidence; they do
not stand in for the paper's full synthetic or molecular experiments.
"""

from __future__ import annotations

import math
from collections.abc import Callable, Sequence

import numpy as np
from scipy.integrate import quad
from scipy.special import expit

Schedule = Callable[[np.ndarray | float], np.ndarray | float]


def alpha_linear(t: np.ndarray | float) -> np.ndarray | float:
    return 1.0 - np.asarray(t)


def alpha_quadratic(t: np.ndarray | float) -> np.ndarray | float:
    return 1.0 - np.asarray(t) ** 2


def alpha_cosine(t: np.ndarray | float) -> np.ndarray | float:
    return np.cos(0.5 * math.pi * np.asarray(t))


def alpha_ddpm(t: np.ndarray | float) -> np.ndarray | float:
    t_arr = np.asarray(t)
    return np.sqrt(np.exp(-0.5 * (0.1 * t_arr + 0.5 * (20.0 - 0.1) * t_arr**2)))


def alpha_sigmoid(t: np.ndarray | float) -> np.ndarray | float:
    """Official ACE sigmoid schedule, translated from torch to NumPy."""
    t_arr = np.asarray(t)
    softplus = np.logaddexp(0.0, ((1.0 - t_arr) - 0.5) * 12.0)
    exponent = (20.0 / 12.0) * softplus + 0.001 * (1.0 - t_arr)
    return np.sqrt(1.0 - np.exp(-exponent))


OFFICIAL_SCHEDULES: dict[str, Schedule] = {
    "linear": alpha_linear,
    "polynomial": alpha_quadratic,
    "sigmoid": alpha_sigmoid,
    "ddpm": alpha_ddpm,
    "cosine": alpha_cosine,
}


def criterion(
    t: np.ndarray | float,
    gammas: Sequence[Callable[[np.ndarray | float], np.ndarray | float]],
    schedules: Sequence[Schedule],
    *,
    epsilon: float = 0.0,
) -> np.ndarray:
    t_arr = np.asarray(t, dtype=float)
    total = np.zeros_like(t_arr, dtype=float)
    for gamma, schedule in zip(gammas, schedules, strict=True):
        alpha = np.asarray(schedule(t_arr), dtype=float)
        total += np.asarray(gamma(t_arr), dtype=float) / (alpha**2 + epsilon)
    return total


def gaussian_log_integral_numeric(precision: float, limit: float) -> float:
    """Log integral of exp(-precision*x^2/2) on [-limit, limit].

    Positive precision is integrated with an independent adaptive quadrature.
    Non-positive precision uses a stable log-trapezoid calculation, which also
    exposes divergence as the truncation limit grows.
    """
    if precision > 0.0:
        value, _ = quad(
            lambda x: math.exp(-0.5 * precision * x * x),
            -limit,
            limit,
            epsabs=1e-12,
            epsrel=1e-12,
            limit=300,
        )
        return math.log(value)

    points = max(20_001, int(1_000 * limit) + 1)
    xs = np.linspace(-limit, limit, points, dtype=float)
    logs = -0.5 * precision * xs**2
    peak = float(np.max(logs))
    scaled = np.exp(logs - peak)
    integral = float(np.trapezoid(scaled, xs))
    return peak + math.log(integral)


def analytic_gaussian_log_integral(precision: float) -> float:
    if precision <= 0.0:
        raise ValueError("The Gaussian integral is finite only for positive precision")
    return 0.5 * math.log(2.0 * math.pi / precision)


def ace_bump(
    gammas: Sequence[Callable[[np.ndarray | float], np.ndarray | float]],
    corrected_index: int,
    bump: float,
) -> list[Callable[[np.ndarray | float], np.ndarray | float]]:
    corrected = list(gammas)
    original = gammas[corrected_index]

    def bumped(t: np.ndarray | float) -> np.ndarray | float:
        t_arr = np.asarray(t)
        return original(t_arr) + bump * t_arr * (1.0 - t_arr)

    corrected[corrected_index] = bumped
    return corrected


def sigmoid_unit(t: np.ndarray | float, slope: float = 10.0) -> np.ndarray:
    """A bounded auxiliary schedule used only by the historical regression."""
    t_arr = np.asarray(t)
    raw = expit(slope * (0.5 - t_arr))
    lo = expit(-0.5 * slope)
    hi = expit(0.5 * slope)
    return 0.25 + 0.75 * (raw - lo) / (hi - lo)
