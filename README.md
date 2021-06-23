# Instance-Builder - Instance builder library for Python inspired by Lombok

## Usage

```python
@builder("id", "name", "age", "email")
class User:
    def __init__(self, id: int, name: str, age: int, email: str) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.email = email

user = User.Builder().id(0).name("Shuntaro Shimizu").age(99).email("ut.s.shimizu@gmail.com").build()
```
