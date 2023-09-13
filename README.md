![Alt Text](https://i.ibb.co/LdxyRp5/image-2023-09-13-23-36-08.png)

# GoodError Documentation

The GoodError library provides an improved exception handling mechanism in Python. It allows you to enhance the output of exceptions, including sending them to GPT-3 for additional context.

## Installation

To install GoodError, use pip:

```bash
pip install gooderror
```


## Example

Here's an example of how to use GoodError:

```python
from gooderror import GoodError

GoodError()

x = "SADfsadf" + 5

# GoodError will enhance the exception output and will add COLORS!
# OUTPUT:
#<module>, TypeError(Can only concatenate str (not "int") to str)
#main, Line 82 -> m = "SADfsadf" + 5

```

## Class: GoodError

The GoodError class provides the following attributes and methods:

### Attributes

- `gpt_key` (str): Your GPT API key.
- `use_colors` (bool): Whether to use colors in the output.


## GPT3.5 Usage

Import the GoodError class and initialize it with your GPT API key.

```python
from gooderror import GoodError

# Initialize GoodError with your GPT API key
GoodError(gpt_key="YOUR_GPT_API_KEY")

result = 0/0

# OUTPUT:
#<module>, ZeroDivisionError(Division by zero)
#main, Line 80 -> result = 0/0

#Waiting for GPT to respond...

#The error "ZeroDivisionError" is raised when you try to divide a number by zero in Python. Division by zero is not defined in mathematics, hence this error is generated to indicate an invalid operation.
#To fix this error, you need to make sure you do not divide a number by zero. If the denominator can potentially be zero in your code, you can add a check to handle this scenario using an if condition. For example:

#try:
#    result = 0/0
#except ZeroDivisionError:
#    print("Cannot divide by zero")

#In this case, if the division operation encounters a ZeroDivisionError, it will be caught by the except block, which will then print the error message.

```