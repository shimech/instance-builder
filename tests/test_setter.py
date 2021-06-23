from instance_builder import setter


@setter
class User:
    __id: int = 0
    __name: str = "Shuntaro Shimizu"
    __age: int = 99
    __email: str = "ut.s.shimizu@gmail.com"


def test_getter() -> None:
    user = User()
    new_attributes = {
        "id": 1,
        "name": "New Name",
        "age": 0,
        "email": "new@example.com"
    }
    user.set_id(new_attributes["id"])
    user.set_name(new_attributes["name"])
    user.set_age(new_attributes["age"])
    user.set_email(new_attributes["email"])
    assert user._User__id == new_attributes["id"]
    assert user._User__name == new_attributes["name"]
    assert user._User__age == new_attributes["age"]
    assert user._User__email == new_attributes["email"]
