from setuptools import setup
from codecs import open
import os
import re

package_name = "instance_builder"

root_dir = os.path.abspath(os.path.dirname(__file__))


def __get_requirements(filename: str) -> list[str]:
    return [name.rstrip() for name in open(os.path.join(root_dir, filename)).readlines()]


with open(os.path.join(root_dir, package_name, "__init__.py")) as f:
    init_text = f.read()
    r"__version__\s*=\s*[\'\"](.+?)[\'\"]", init_text).group(1)
        version=re.search(
    author = re.search(
        r"__author__\s*=\s*[\'\"](.+?)[\'\"]", init_text).group(1)
    author_email = re.search(
        r"__author_email__\s*=\s*[\'\"](.+?)[\'\"]", init_text).group(1)
    url = re.search(r"__url__\s*=\s*[\'\"](.+?)[\'\"]", init_text).group(1)
    license = re.search(
        r"__license__\s*=\s*[\'\"](.+?)[\'\"]", init_text).group(1)

assert version
assert author
assert author_email
assert url
assert license

with open("README.md", mode="r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name=package_name,
    version=version,
    author=author,
    author_email=author_email,
    description="Instance builder library for Python inspired by Lombok",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    packages=[package_name],
    install_requires=__get_requirements("requirement.txt"),
    license=license,
    keywords=[
        "Instance Builder",
        "Builder",
        "Lombok"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
