# Week 12: Exception Handling

Exception handling is used to manage errors in a program without crashing.

Example:
```python
try:
    x = int("abc")
except ValueError:
    print("Invalid number")
```

The `try` block contains risky code and the `except` block handles the error.
