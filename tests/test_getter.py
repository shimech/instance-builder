from instance_builder import getter


@getter
class User:
    __id: int = 0
    __name: str = "Shuntaro Shimizu"
    __age: int = 99
    __email: str = "ut.s.shimizu@gmail.com"


def test_getter() -> None:
    user = User()
    assert user.get_id() == 0
    assert user.get_name() == "Shuntaro Shimizu"
    assert user.get_age() == 99
    assert user.get_email() == "ut.s.shimizu@gmail.com"
