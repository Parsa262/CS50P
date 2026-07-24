# CS50P Week 2 - Loops (AI)

## for Loop

Loop through each item in a sequence.

```python
for c in word:
    print(c)
```

Loop a certain number of times:

```python
for i in range(3):
    print("Hello")
```

---

## while Loop

Repeat while a condition is true.

```python
x = 3

while x > 0:
    print(x)
    x -= 1
```

Useful when the number of repetitions is unknown.

---

## String Methods

```python
.lower()
.upper()
.strip()
.isalpha()
.isdigit()
.isalnum()
```

Examples:

```python
text.lower()
c.isdigit()
```

---

## Dictionaries

Store values with keys.

```python
fruits = {
    "apple": 130,
    "banana": 110
}
```

Access a value:

```python
fruits["apple"]
```

Check if a key exists:

```python
if fruit in fruits:
```

---

## Useful Keywords

```python
break
continue
pass
```

- `break` → leave the loop.
- `continue` → skip to the next iteration.
- `pass` → do nothing.

---

## Good Habits

- Return `False` as soon as a rule is broken.
- Return `True` only after all checks pass.
- Use dictionaries instead of many `if`/`elif` statements.
- Use `.lower()` for case-insensitive comparisons.

---

## Workflow

```text
Code
↓
check50
↓
style50
↓
submit50
```