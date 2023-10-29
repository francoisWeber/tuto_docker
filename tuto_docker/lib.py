from functools import lru_cache
import numpy as np


@lru_cache()
def factoriel_recusrive(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factoriel_recusrive(n - 1)


def factoriel(n: int) -> int:
    resp = 1
    for p in range(1, n + 1):
        resp *= p
    return resp


def exp_approx(x: float, cut_at: int = 10) -> float:
    elements = [x**i / factoriel_recusrive(i) for i in range(cut_at)]
    return sum(elements)


def compare_exp_to_np(x: float, cut_at: int = 10) -> float:
    exp_x_approx = exp_approx(x, cut_at)
    exp_x_np = np.exp(x)
    return np.abs(exp_x_approx - exp_x_np) / exp_x_np
