"""Own scalar recurrence diagnostics, not metronic field or mass predictions.

Assume x[0],x[1]>0 and x[n+2]=x[n+1]+x[n]. Index n here is our
sequence index, NOT the book's physical N4 or its small divisor z.
All calculations are exact rational arithmetic. No files are written.
"""

from fractions import Fraction as F


def exact(value):
    if type(value) not in (int, F):
        raise TypeError("Use exact int or Fraction")
    return F(value)


def index(n, minimum=0):
    if type(n) is not int or n < minimum:
        raise ValueError(f"Require integer index >= {minimum}")
    return n


def fibonacci(n):
    index(n)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def sequence_pair(x0, x1, n):
    """Return (x[n], x[n+1]) for strictly positive exact starts."""
    a, b = map(exact, (x0, x1))
    index(n)
    if a <= 0 or b <= 0:
        raise ValueError("Strictly positive starts required")
    for _ in range(n):
        a, b = b, a+b
    return a, b


def ratio_window(n):
    """Closed outer hull for x[n+1]/x[n], n>=2, ALL positive starts.

    Endpoints and phi are not generally attained by finite rational starts.
    The hull is independent of starts, not a physical approximation budget.
    """
    index(n, 2)
    fm, fn, fp = fibonacci(n-1), fibonacci(n), fibonacci(n+1)
    endpoints = F(fp, fn), F(fn, fm)
    return min(endpoints), max(endpoints)


def golden_polynomial(x):
    x = exact(x)
    return x*x-x-1


def selector_residual(xn, previous, previous2):
    """Ordinary backward Delta: (Delta^2-3Delta+I)x, not a tensor solver."""
    xn, previous, previous2 = map(exact, (xn, previous, previous2))
    return -xn+previous+previous2


def divisor_candidates():
    """Only the stated divisibility/order premises, no heuristic equality."""
    return tuple(z for z in range(2, 15) if 15 % z == 0)


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Run exact checks (default)")
    parser.parse_args()
    lo, hi = ratio_window(22)
    # All endpoints strictly inside this ROUNDING CELL, not just error < 1e-8.
    cell_lo, cell_hi = F("1.618033985"), F("1.618033995")
    if not cell_lo < lo < hi < cell_hi:
        raise ArithmeticError("Rational rounding enclosure failed")
    if not golden_polynomial(lo) < 0 < golden_polynomial(hi):
        raise ArithmeticError("Positive golden root not enclosed")
    if divisor_candidates() != (3, 5):
        raise ArithmeticError("Divisor conditions changed")
    print(f"For all positive starts: {lo} < x[23]/x[22] < {hi}")
    print("Both bounds and the positive golden root round to 1.61803399 (8 decimals)")
    print("Divisor/order premises leave z=3 and z=5; no extra equality assumed")
    print("No physical index, field-error budget, alternative A profile, or mass certified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
