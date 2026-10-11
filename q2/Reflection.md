# Reflection: Encapsulation

## Activity 2 question
**How does using `@property` make your code easier to read compared to using traditional `get_` and `set_` methods?**

With `@property`, I can read and change a value the same way I use a normal variable. I write `rectangle.width` and `rectangle.width = 5` instead of `rectangle.get_width()` and `rectangle.set_width(5)`. There are no parentheses and no `get_`/`set_` prefixes, so the lines are shorter and read more like plain English. The attribute is still private (`__width`), and the setter still checks that the value is greater than 0, so the code is cleaner without losing protection. Whoever uses my class only needs to know the name `width`, not which method to call for reading or writing.

## Activity 3: What I learned from BankAccount
- **Private attributes** (`__account_number`, `__balance`) cannot be accessed directly from outside the class, so other code cannot change them by accident.
- **Setters** let me validate data. `set_balance()` ignores a negative value and prints a warning, so the balance never becomes invalid (it stayed 1000.00 when I tried -100).
- **`@property` getters** let me read the account number and balance safely, like regular attributes.
- Formatting the balance with `:.2f` makes the output look like real money (1000.00).

## How encapsulation protects data and improves code organization
Encapsulation bundles data and the methods that work on it into one class, and hides the data behind access modifiers (`__` private, `_` protected, no underscore public). Because all changes go through methods, the class controls what values are allowed, which protects the data from mistakes. It also keeps the code organized, because everything about an object is in one place and the internal details can change without breaking the code that uses the class.
