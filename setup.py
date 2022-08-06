import os

from setuptools import find_packages, setup


this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md")) as f:
    long_description = f.read()

setup(
    name="attributes-doc",
    version="0.3.0",
    url="https://github.com/tkukushkin/attributes-doc",
    author="Timofey Kukushkin",
    author_email="tima@kukushkin.me",
    description="PEP 224 implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        'typing; python_version<"3"',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    project_urls={
        "Source": "https://github.com/tkukushkin/attributes-doc",
    },
)
