# This is the file you'll use to submit most of Lab 0.

# Certain problems may ask you to modify other files to accomplish a certain
# task. There are also various other files that make the problem set work, and
# generally you will _not_ be expected to modify or even understand this code.
# Don't get bogged down with unnecessary work.


# Section 1: Problem set logistics ___________________________________________

# This is a multiple choice question. You answer by replacing
# the symbol 'fill-me-in' with a number, corresponding to your answer.

# You get to check multiple choice answers using the tester before you
# submit them! So there's no reason to worry about getting them wrong.
# Often, multiple-choice questions will be intended to make sure you have the
# right ideas going into the problem set. Run the tester right after you
# answer them, so that you can make sure you have the right answers.

# What version of Python do we *recommend* (not "require") for this course?
#   1. Python v2.3
#   2. Python v2.5 or Python v2.6
#   3. Python v3.0
# Fill in your answer in the next line of code ("1", "2", or "3"):

ANSWER_1 = "2"


# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch

def cube(x):
    return x * x * x

def factorial(x):
    if x < 0:
        raise Exception("factorial: input must not be negative")
    elif x == 0:
        return 1
    else:
        return x * factorial(x-1)

def count_pattern(pattern, lst):
    count = 0
    if len(pattern) > len(lst):
        return count
    elif seq_equal(pattern, lst):
        count = count + 1 + count_pattern(pattern, lst[1:])
    elif len(pattern) <= len(lst):
        count = count_pattern(pattern, lst[1:])
    else:
        return count
    return count
            
            
def seq_equal(l, s):
    res = True
    for i in range(len(l)):
        res = res and (l[i] == s[i])
    return res

# Problem 2.2: Expression depth

def depth(expr):
    if not isinstance(expr, (list,tuple)):
        return 0
    elif isinstance(expr, (list,tuple)):
        return (1 + max(map((lambda x: depth(x)), expr)))
        


# Problem 2.3: Tree indexing

def tree_ref(tree, index):
    res = tree
    for i in index:
        res = res[i]
    return res

# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.

from algebra import Sum, Product, simplify_if_possible
from algebra_utils import distribution, encode_sumprod, decode_sumprod

# Section 4: Survey _________________________________________________________

# Please answer these questions inside the double quotes.

# When did you take 6.01?
WHEN_DID_YOU_TAKE_601 = ""

# How many hours did you spend per 6.01 lab?
HOURS_PER_601_LAB = ""

# How well did you learn 6.01?
HOW_WELL_I_LEARNED_601 = ""

# How many hours did this lab take?
HOURS = ""
