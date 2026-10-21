# Week 12 Coding Exercise: Exception Handling

Write a program that asks the user for a number and handles invalid input safely.

```python
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")
```
