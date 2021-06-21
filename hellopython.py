# hello world
# ref: https://docs.python-guide.org/writing/style/

# example on "Constants" "condition if-else"

# test on variable ATTR
ATTR = True


# Just check the value
if ATTR:
    print('attr is truthy!')

# or check for the opposite
if not ATTR:
    print('attr is falsey!')

# or, since None is considered false, explicitly check for it
if ATTR is None:
    print('attr is None!')
