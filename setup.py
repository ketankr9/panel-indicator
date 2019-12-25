import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="panel-indicator-test1",
    version="0.0.1.dev1",
    author="Utsav Krishnan",
    author_email="ketankr9@gmail.com",
    description="A library to display any text in ubuntu unity panel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ketankr9/panel-indicator.git",
    packages=setuptools.find_packages(),
    install_requires=[
          'PyGObject>=3.34.0',
          'pycairo'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires='>=3.6',
)

