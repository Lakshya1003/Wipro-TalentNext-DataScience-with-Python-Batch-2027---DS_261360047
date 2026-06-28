# Exception Handling - Sample Questions

**Q1: What will be the output for print(5-'A')?**

If you try to run that, Python will immediately crash and throw a `TypeError`. You can't mathematically subtract a text string from a number!

**Q2: Which block is always executed irrespective of the exception?**

That would be the `finally` block. No matter if your code works perfectly or completely crashes into an error, the `finally` block is guaranteed to run at the very end.

```python
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Failed!")
finally:
    print("This runs no matter what.")
```

**Q3: Which block is executed when there is no exception?**

The `else` block! If your `try` block succeeds without triggering any errors, the code inside the `else` block gets to run right after it.

**Q4: Which is the base class for all the exception classes?**

The absolute root class for all of them is `BaseException`. Every single error and exception in Python eventually inherits from this base class!

**Q5: Do we need any module to implement exception handling?**

Nope! You don't need to import anything at all. Keywords like `try`, `except`, `else`, and `finally` are built directly into standard Python so you can use them anywhere.
