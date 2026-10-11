# Reflection: Encapsulation

## Activity 2 question
**How does using `@property` make your code easier to read compared to using traditional `get_` and `set_` methods?**

With `@property`, I can read and change a value the same way I use a normal variable. I write `rectangle.width` and `rectangle.width = 5` instead of `rectangle.get_width()` and `rectangle.set_width(5)`. There are no parentheses and no `get_`/`set_` prefixes, so the lines are shorter and read more like plain English. The attribute is still private (`__width`), and the setter still checks that the value is greater than 0, so the code is cleaner without losing protection. Whoever uses my class only needs to know the name `width`, not which method to call for reading or writing.
