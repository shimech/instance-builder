from setuptools import setup
import os


root_dir = os.path.abspath(os.path.dirname(__file__))


def __get_requirements(filename: str) -> list[str]:
    return [name.rstrip() for name in open(os.path.join(root_dir, filename)).readlines()]


setup(
    packages=["instance-builder"],
    install_requires=__get_requirements("requirement.txt"),
    keywords=[
        "Instance Builder",
        "Builder",
        "Lombok"
    ],
)
