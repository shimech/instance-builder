from instance_builder import builder


@builder("id", "name", "age", "email")
class User:
    def __init__(self, id: int, name: str, age: int, email: str) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.email = email


def test_builder() -> None:
    id = 0
    name = "Shuntaro Shimizu"
    age = 99
    email = "ut.s.shimizu@gmail.com"

    user = User.Builder().id(id).name(name).age(age).email(email).build()

    assert isinstance(user, User)
    assert user.id == id
    assert user.name == name
    assert user.age == age
    assert user.email == email
