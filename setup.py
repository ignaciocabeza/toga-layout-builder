
#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="toga-layout-builder", 
    version="0.0.1",
    author="Ignacio Cabeza",
    author_email="ignaciocabeza@gmail.com",
    description="Toga Layout",
    long_description="long_description",
    long_description_content_type="text/markdown",
    url="https://github.com/ignaciocabeza/toga-layout-builder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)