# IO Operations - Sample Questions Answers

### 1. How to open a file in create mode?
To open a file specifically in create mode, you use the `open()` function with the mode `"x"`. This creates a brand new file and will raise an error if a file with that name already exists. You can also use `"w"` which creates the file if it does not exist.

```python
my_file = open("new_document.txt", "x")
my_file.write("Hello World")
my_file.close()
```

### 2. Which function reads one line at a time?
The `readline()` function is used to read exactly one line at a time from an opened file. Each time you call it, it moves to the next line.

```python
my_file = open("existing_document.txt", "r")
first_line = my_file.readline()
print(first_line)
my_file.close()
```

### 3. Which module is required to delete files or folders?
You must import the `os` module to delete files or folders. You use `os.remove()` to delete a file, and `os.rmdir()` to delete a folder.

```python
import os

os.remove("unwanted_file.txt")
```
