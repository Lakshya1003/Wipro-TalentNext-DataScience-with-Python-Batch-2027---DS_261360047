# Command Line Arguments - Sample Questions

**Q1: Which module is required to access cmd line arguments?**

To access command line arguments in Python, you need to bring in the system module. You can do this by using the `import` keyword right at the top of your script. Once you have it, you can easily grab whatever arguments were passed by looking at `sys.argv`.

```python
import sys

the_arguments_given = sys.argv
print(the_arguments_given)
```
