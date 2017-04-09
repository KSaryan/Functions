"""
Skills function practice.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> num_spaces("Balloonicorn is       awesome!")
    8

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Positive', 'Odd']

    >>> sign_and_parity(-2)
    ['Negative', 'Even']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""

# Part One
def hello_world():
    """Prints 'Hello World'"""

    print "Hello World"


def say_hi(name):
    """Prints 'Hi' and inputted name"""

    print "Hi", name


def print_product(num1, num2):
    """Prints the product of two numbers"""

    print num1 * num2


def repeat_string(your_string, n):
    """Prints given string n number of times"""
    
    print your_string * int(n)


def print_sign(num):
    """Prints whether given number is higher or lower than 0"""
    
    if num == 0:
        print "Zero"
    elif num < 0:
        print "Lower than 0"
    else: 
        print "Higher than 0"


def is_divisible_by_three(num):
    """Returns True if number is divisble by 3, otherwise False"""
    
    return num % 3 == 0


def num_spaces(sentence):
    """Returns number of spaces in given string"""
    
    num_spaces = 0
    for char in sentence:
        if char == " ":
            num_spaces += 1
    return num_spaces


def total_meal_price(price, tip = .15):
    """Calculates and returns price of meal based on given price and tip

    If no tip given, default is 15%
    """

    return price + price * tip


def sign_and_parity(num):
    """Returnds list containing sign and parity of given num"""

    num_info = ["Positive", "Odd"]
    if num < 0:
        num_info [0] = "Negative"
    if num % 2 == 0:
        num_info[1] = "Even"
    return num_info


# Calling function, assigning to variables, and printing
# Question 9, part 2
s_and_p = sign_and_parity(-5)
sign = s_and_p[0]
parity = s_and_p[1]
print sign
print parity


# Part Two
def full_title(name, job = "Engineer"):
    """Returns name and job as one string

    If no job given, Engineer is default"""

    return "{} {}".format(job, name)


def write_letter(recipient_name, recepient_title, sender_name):
    """Composes letter from sender to recipient"""

    recipient_full_title = full_title(recipient_name, recepient_title)
    print "Dear {}, I think you are amazing! Sincerely, {}".format(recipient_full_title, sender_name)


###############################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.


# 3. Write a function called 'print_product' that takes two integers and
#    multiplies them together. Print the result.


# 4. Write a function called 'repeat_string' that takes a string and an integer
#    and prints the string that many times


# 5. Write a function called 'print_sign' that takes an integer and prints
#    "Higher than 0" if higher than zero and "Lower than 0" if lower than zero.
#    If the integer is zero, print "Zero".


# 6. Write a function called 'is_divisible_by_three' that takes an integer and
#    returns a boolean (True or False), depending on whether the number is
#    evenly divisible by 3.


# 7. Write a function called 'num_spaces' that takes a sentence as one string
#    and returns the number of spaces.


# 8. Write a function called 'total_meal_price' that can be passed a meal price
#    and a tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip percentage should
#    be optional; if not given, it should default to 15%.


# 9. Write a function called 'sign_and_parity' that takes an integer as an
#    argument and returns two pieces of information as strings --- "Positive"
#    or "Negative" and "Even" or "Odd". The two strings should be returned in
#    a list.
#
#    Then, write code that shows the calling of this function on a number and
#    unpack what is returned into two variables --- sign and parity (whether
#    it's even or odd). Print sign and parity.


###############################################################################

# PART TWO

# 1. Write a function that takes a name and a job title as parameters, making
#    it so the job title defaults to "Engineer" if a job title is not passed
#    in. Return the person's title and name in one string.

# 2. Given a recipient name & job title and a sender name, print the following
#    letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.


###############################################################################

# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
