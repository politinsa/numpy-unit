import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

print(setuptools.find_packages())
setuptools.setup(
    name="numpy_unit",
    version="0.1.1",
    author="Politinsa",
    description="A package providing an unit system for numpy multidimensionnal arrays.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/politinsa/numpy-unit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["numpy>=1.17.0"]
)