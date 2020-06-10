from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="toga-layout-builder", 
    version="0.3.0",
    author="Ignacio Cabeza",
    author_email="ignaciocabeza@gmail.com",
    description="Toga Layout",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ignaciocabeza/toga-layout-builder",
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        'toga',
        'pyyaml',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)