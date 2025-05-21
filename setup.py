from setuptools import setup, find_packages

setup(
    name="freedb",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[],
    author="Robin Trachsel",
    author_email="trachselr@bzz.ch",
    description="A simple database management package",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TrachselRobin/freeDB",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL v3 License",
    ],
    python_requires=">=3.10",
)
