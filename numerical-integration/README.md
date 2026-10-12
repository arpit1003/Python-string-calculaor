# Numerical Integration Explorer

A beginner-friendly mathematics project in Python. It approximates definite integrals using two numerical methods and compares the results with exact answers:

- **Trapezoidal rule:** approximate the area with trapezoids.
- **Simpson's rule:** use a quadratic approximation over pairs of intervals.

The **absolute error** is |approximate result − exact result|.

## Requirements

Python 3.9 or newer. No external dependencies.

## Run

Open a terminal in this folder:

~~~bash
python integration.py
python integration.py --function sine --a 0 --b 3.141592653589793 --n 100
python integration.py --function exp --a 0 --b 1 --n 20
~~~

Available functions: **square** (x²), **sine** (sin x), and **exp** (eˣ).
Use --a and --b for the limits and --n for the number of intervals.
To compare both methods, n must be an even integer at least 2.

Default example (integral of x² from 0 to 1, n = 10):

~~~text
Function: square | Interval: [0.0, 1.0] | n = 10
Exact integral: 0.3333333333
Trapezoidal: 0.3350000000 | absolute error = 1.667e-03
Simpson    : 0.3333333333 | absolute error = 0.000e+00
~~~

## Mathematical formulas

Let h = (b − a)/n and xᵢ = a + ih.

**Trapezoidal rule:**

I ≈ h [f(a)/2 + f(x₁) + ··· + f(xₙ₋₁) + f(b)/2]

**Composite Simpson's rule** (n even):

I ≈ h/3 [f(a) + 4f(x₁) + 2f(x₂) + ··· + 4f(xₙ₋₁) + f(b)]

The exact value is found using known antiderivatives. Simpson's rule integrates quadratic functions exactly, apart from possible floating-point rounding.

## Tests

~~~bash
python -m unittest discover -v
~~~

## Experiment

Compare n = 2, 10, and 100 for the same function. Observe how the absolute error changes for the two methods.
