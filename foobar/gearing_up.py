# MOST TO LEAST OPTIMAL 

from fractions import Fraction

def answer(pegs):
    if len(pegs) == 2:
        # it is not a linear system
        x = [Fraction(pegs[1] - pegs[0]) / 3]
    else:
        # solve linear system
        dim = len(pegs) - 1
        A = [[Fraction(0) for _ in range(dim)] for _ in range(dim)]
        b = [Fraction(0) for _ in range(dim)]
        for i in range(dim):
            n = (i + 1) % dim
            b[i] = Fraction(pegs[i + 1] - pegs[i])
            A[i][i] = Fraction(1)
            A[i][n] = Fraction(1)

        A[0][0] = Fraction(2)
        x = solve(A, b)

    # result
    for i in range(len(x)):
        if x[i] < 0 or x[i].numerator < x[i].denominator:
            return [-1, -1]

    x[0] *= 2
    return [x[0].numerator, x[0].denominator]

def solve(A, b):
    """
    Solve a linear system Ax = b, adaptive for the matrix in this problem.
    Inputs:
        A - a nxn matrix. n >= 2.
        b - a nx1 vector.
    Returns:
        x - the nx1 vector satisfying Ax = b.
    """
    dim = len(b)

    # A -> Upper triangle
    for i in range(dim - 1):
        if A[dim - 1][i] != 0:
            frac = A[dim -1][i] / A[i][i]
            b[dim - 1] -= frac * b[i]
            A[dim - 1][i] = Fraction(0)
            for j in range(i + 1, dim):
                A[dim - 1][j] -= frac * A[i][j]

    b[dim - 1] /= A[dim - 1][dim - 1]
    A[dim - 1][dim - 1] = Fraction(1)

    # backward subs
    for i in range(dim - 2, -1, -1):
        b[i] -= b[i+1]

    # deal with row 0
    b[0] /= 2

    return b

# ====================================
from fractions import Fraction  
 
def answer(pegs):
    arrLength = len(pegs)
    if ((not pegs) or arrLength == 1):
        return [-1,-1]
 
    even = True if (arrLength % 2 == 0) else False
    sum = (- pegs[0] + pegs[arrLength - 1]) if even else (- pegs[0] - pegs[arrLength -1])
 
    if (arrLength > 2):
        for index in xrange(1, arrLength-1):
            sum += 2 * (-1)**(index+1) * pegs[index]
 
    FirstGearRadius = Fraction(2 * (float(sum)/3 if even else sum)).limit_denominator()
 
 
    currentRadius = FirstGearRadius
    for index in xrange(0, arrLength-2):
        CenterDistance = pegs[index+1] - pegs[index]
        NextRadius = CenterDistance - currentRadius
        if (currentRadius < 1 or NextRadius < 1):
            return [-1,-1]
        else:
            currentRadius = NextRadius
 
    return [FirstGearRadius.numerator, FirstGearRadius.denominator]

'''
The Challenge
As Commander Lambda’s personal assistant, you’ve been assigned the task of configuring the LAMBCHOP doomsday device’s axial orientation gears.
It should be pretty simple – just add gears to create the appropriate rotation ratio.

But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it,
the pegs that will support the gears are fixed in place.

The LAMBCHOP’s engineers have given you lists identifying the placement of groups of pegs along various support beams.
You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). 
The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size,
from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm)
of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the location of each peg along the support beam,
write a function answer(pegs) which, if there is a solution,
returns a list of two positive integers a and b representing the numerator and denominator of the first gear’s radius in its simplest form in order
to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1.

Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible,
the function answer(pegs) should return the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, 
and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. 
In this case, pegs would be [4, 30, 50] and answer(pegs) should return [12, 1].

The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers,
all between 1 and 10000 inclusive.
''' 
