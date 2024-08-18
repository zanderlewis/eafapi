import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="idrc",
    version="0.0.1",
    author="Zander Lewis",
    author_email="zander@zanderlewis.dev",
    description="Auto APIs for lazy people.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zanderlewis/idrc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)