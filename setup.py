import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="plvra",
    version="1.0.0",
    description="TUI Wordle clone in portuguese",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/eshiraishi/plvra-tui",
    author="Enzo Shiraishi",
    author_email="enzo.shiraishi@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        'Operating System :: OS Independent'
    ],
    packages=["plvra"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "plvra = plvra.plvra:main"
        ]
    }
)