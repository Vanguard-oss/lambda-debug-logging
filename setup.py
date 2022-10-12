from pathlib import Path

from setuptools import find_packages, setup


# read the contents of your README file

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    author="Vanguard",
    author_email="opensource@vanguard.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    description="Logging configuration to make debugging Lambdas easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    install_requires=[
        "pytz>=2021.3",
    ],
    name="lambda-debug-logging",
    packages=find_packages(),
    url=("https://github.com/vanguard/lambda-debug-logging"),
    version="0.1.0",
)