**AI-notes, CS50P Week 1 (Conditionals)** 

---

# CS50P - Week 1: Conditionals

## Comparison Operators

```python
==
!=
<
<=
>
>=
```

These compare two values and return either `True` or `False`.

Example:

```python
x = 5

if x > 3:
    print("Yes")
```

---

## if

Runs code only if the condition is true.

```python
if x == 10:
    print("Ten")
```

---

## if / else

Choose between two possibilities.

```python
if x > 0:
    print("Positive")
else:
    print("Not positive")
```

---

## if / elif / else

Used when there are multiple conditions.

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("Keep trying")
```

Python checks from top to bottom and stops at the first true condition.

---

## and

Both conditions must be true.

```python
if age >= 18 and age < 65:
    print("Adult")
```

---

## or

At least one condition must be true.

```python
if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

---

## Nested Conditionals

An `if` inside another `if`.

```python
if x > 0:
    if x < 10:
        print("Single digit")
```

---

## match / case

Another way to compare one value against different cases.

```python
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case _:
        print("Unknown")
```

`_` works like the default case.

---

## Good Habits

* Use meaningful variable names.
* Keep indentation consistent (4 spaces).
* Use `elif` instead of many separate `if` statements when checking the same thing.
* Order conditions carefully because Python stops after the first true one.

---

## Things to Remember

* `=` assigns a value.
* `==` compares two values.
* `if` checks one condition.
* `elif` checks another condition if the previous one was false.
* `else` runs if none of the above conditions were true.
* `and` means **both**.
* `or` means **at least one**.

---

