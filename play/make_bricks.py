"""

We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each)
and big bricks (5 inches each). 
Return True if it is possible to make the goal by 
choosing from the given bricks. 
This is a little harder than it looks and can be done
without any loops

"""

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True


def make_bricks(small, big, goal):
  return (goal%5)<=small and (goal-(big*5))<=small

#WHY

"""
here goal%5<=small checks whether the remainder
(i.e. the remaining inches after the big brick is used) 
can be fulfilled by the small bricks (so if it is greater
than the small bricks then it will return false else if small
is greater than the remainder then it will return True as the
number of bricks is sufficient). (goal-(big*5))<=small here means 
to check whether the total number of inches of big bricks and
small bricks are sufficient enough to complete the goal. 
Instead of (goal-(big*5))<=small we can also use goal<=big*5+small
as it may seem more clear and well-explained
"""
