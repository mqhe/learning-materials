# Exercise 1

n = int(input("n = "))
t = n  # We shall work on `t`, so `n` can be used in the output

# Let us get the absolute value of `t`, to avoid problem
# This can also be done as `t = abs(t)`.
if t < 0:
    t = -t

# This variable will hold the sum.
# An extra `_` in the name is to avoid the collision with
# a built-in `sum` function.
sum_ = 0

# Take last digit out of the number and add it to the sum if it's odd.
# Repeat until there are no digits left.
while t > 0:
    last_digit = t % 10
    t = t // 10    # or can use: t //= 10
    if last_digit % 2 == 1:
        sum_ += last_digit

print("The sum of the odd digits in number", n, "is", str(sum_) + ".")

#---------------------------------------------------------------------

# Exercise 2

n = int(input("Please type a number (zero to quit): "))
current_which = 0

max_number = None
max_which = None

while n != 0:
    current_which += 1
    if max_number is None or n > max_number:
        max_number = n
        max_which = current_which
    n = int(input("Please type a number (zero to quit): "))

if current_which > 0:
    print("The maximum number is #" + str(max_which) + " and its value is " + str(max_number) + ".")
else:
    print("The maximum does not exist (there were no numbers given).")

#----------------------------------------------------------------------

# Exercise 2a
n = int(input("Please type a number (zero to quit): "))
current_which = 0

max_number = None
max_which = None

while n != 0:
    current_which += 1
    # The difference from the original solution is in the next line (>=)
    if max_number is None or n >= max_number:
        max_number = n
        max_which = current_which
    n = int(input("Please type a number (zero to quit): "))

if current_which > 0:
    print("The maximum number is #" + str(max_which) + " and its value is " + str(max_number) + ".")
else:
    print("The maximum does not exist (there were no numbers given).")

#----------------------------------------------------------------------

# Exercise 3

n = int(input("n = "))
sum_ = 0
for k in range(n):
    x = abs(int(input("Type an integer #" + str(k+1) + ": ")))
    md = 0
    while x > 0:
        digit = x % 10
        x //= 10
        if digit > md:
            md = digit
    sum_ += md

print("The required sum:", sum_)

#----------------------------------------------------------------------

# Exercise 4

n = int(input("n = "))
sum_ = 0
for k in range(n):
    x = abs(int(input("Type an integer #" + str(k+1) + ": ")))
    md = 0
    cnt = 0  # how many times has the current maximum digit appeared
    while x > 0:
        digit = x % 10
        x //= 10
        if digit > md:
            md = digit
            cnt = 1  # For a new `md`, reset the counter to 1
        elif digit == md:
            cnt += 1  # We found one more digit equal to `md`
    sum_ += cnt * md

print("The required sum:", sum_)

#----------------------------------------------------------------------

# Exercise 5

n = int(input("n = "))
# The current maximum sum of odd digits.
# We use -1 to be able to detect when there were no numbers loaded
# (every number has the sum of odd/even digits at least zero).
max_sum = -1

while n != 0:
    t = abs(n)  # we shall need `n` later

    # Get the sum of the number's odd digits:
    current_sum = 0
    while t > 0:
        digit = t % 10
        t //= 10
        if digit % 2 == 1:
            current_sum += digit

    # This is not a part of the problem, but we add it to make it easier
    # for students to follow what's going on in the program.
    print("  The sum of the odd digits of " + str(n) + ":", current_sum)

    # Check if this number's sum is the new maximum
    if current_sum > max_sum:
        max_sum = current_sum
        max_n = n

    n = int(input("n = "))

if max_sum < 0:
    print("No numbers were loaded, so there is no maximum.")
else:
    print("The number with the maximum sum of odd digits is:", max_n)

