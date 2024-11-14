#raise a typeerror if x is not an integer?

x = "hello"

if not  type(x) is int:
    raise typeerror("only integers are allowed")
