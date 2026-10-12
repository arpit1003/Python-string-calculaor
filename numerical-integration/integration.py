"""Compare two simple numerical integration methods with exact results."""

import argparse
import math


FUNCTIONS = {
    "square": (lambda x: x**2, lambda x: x**3 / 3),
    "sine": (math.sin, lambda x: -math.cos(x)),
    "exp": (math.exp, math.exp),
}


def trapezoidal(f, a, b, n):
    """Approximate the integral of f from a to b using n trapezoids."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    h = (b - a) / n
    total = (f(a) + f(b)) / 2
    for i in range(1, n):
        total += f(a + i * h)
    return h * total


def simpson(f, a, b, n):
    """Approximate the integral using Simpson's rule (even n only)."""
    if n < 2 or n % 2 != 0:
        raise ValueError("Simpson's rule needs an even n of at least 2")
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * f(a + i * h)
    return h * total / 3


def main():
    parser = argparse.ArgumentParser(description="Explore numerical integration")
    parser.add_argument("--function", choices=FUNCTIONS, default="square")
    parser.add_argument("--a", type=float, default=0.0, help="lower limit")
    parser.add_argument("--b", type=float, default=1.0, help="upper limit")
    parser.add_argument("--n", type=int, default=10, help="number of intervals (even)")
    args = parser.parse_args()

    if args.n < 2 or args.n % 2:
        parser.error("--n must be an even integer of at least 2")

    f, primitive = FUNCTIONS[args.function]
    exact = primitive(args.b) - primitive(args.a)
    print(f"Function: {args.function} | Interval: [{args.a}, {args.b}] | n = {args.n}")
    print(f"Exact integral: {exact:.10f}")
    for name, method in [("Trapezoidal", trapezoidal), ("Simpson", simpson)]:
        result = method(f, args.a, args.b, args.n)
        print(f"{name:11s}: {result:.10f} | absolute error = {abs(result - exact):.3e}")


if __name__ == "__main__":
    main()
