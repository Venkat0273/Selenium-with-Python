"""Let's write some basic stuff in Python 3.x"""
# When ever you are writing functions in Python, make function name in lower case itself else python raises PEP8 Error though it is not functional error but complying with PEP8 standard is recommended
def python_basics_bool():
  """Let's write some stuff regarding boolean data types.
  Operations that we can perform on Booleans are AND, OR and NOT. These are logical operators.
  We can also check whether bool is sub class of int.
  Let's have a practical implementation of the above discussed
  """
  # Let's declare 2 variables
  a, b = True, False
  # Let's perform AND operation on the aforeassigned variables. Logical AND returns True if both the operands are True else it returns False. In our case, a is True but b is False hence it returns False
  print(f"Are they equal?: {a AND b}")
  # Let's perform OR operation. OR operator returns True if any one of the operand is True.
  print(f"Are they equal?: {a OR b}")
  # Let's perform NOT operation. NOT returns negative of boolean values. If input is True, it returns False.
  print(f"Is it True?: {NOT b}")
  print(f"Is bool sub class of int?: {issubclass(bool, int)}")
  print(f"Is True instance of bool?: {isinstance(True, bool)}")
  print(f"Is False instance of bool?: {isinstance(False, bool)}")
  print("We are done with Boolean operations, change this file to add few more if you know")


def python_basics_int():
  """Below are common methods that you can apply on integers.
  """
  # Let's define 2 variables
  num1, num2 = 6, 9
  print(f"Sum of given is: {num1 + num2}")
  

python_basics_bool()
