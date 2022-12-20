import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="flask-json-db",
    author="Prince Roshan",
    version='0.0.1',
    author_email="princekrroshan01@gmail.com",
    url="https://github.com/Agent-Hellboy/flask-json-db",
    description=("A flask extension to log a python object in json file"),
    long_description=read("README.rst"),
    license="MIT",
    package_dir={'': 'src'},
    packages=['flask_json_db'],
    keywords=[
        "flask-extension","log-variable"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)