import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="frt",
    version="0.0.1",
    author="Jean-Paul van Brakel",
    author_email="jeanpaulvbrakel@gmail.com",
    description="A package for financial research using WRDS data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vanBrakel/FRT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)