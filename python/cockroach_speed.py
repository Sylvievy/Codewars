'''
Description:
The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

For example:

1.08 --> 30
Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.

8kyu
15 m ago
'''
import math
def cockroach_speed(s):
    r=math.floor(s*27.778)
    return r
