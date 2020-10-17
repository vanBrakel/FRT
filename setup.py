import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apt-py",
    version="0.0.1",
    author="Jean-Paul van Brakel",
    author_email="jeanpaulvbrakel@gmail.com",
    description="A package for research into asset pricing and backtesting of investment strategies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vanBrakel/AssetPricingToolbox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)