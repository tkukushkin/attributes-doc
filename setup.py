import os

from setuptools import find_packages, setup


this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='attributes-doc',
    version='0.1.0',
    url='https://github.com/tkukushkin/attributes-doc',
    author='Timofey Kukushkin',
    author_email='tima@kukushkin.me',
    description='PEP 224 implementation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    py_modules=['attributes_doc'],
    package_dir={'': 'src'},
    install_requires=[
        'typing;python_version<"3"',
    ],
    extras_require={
        'test': [
            'coverage',
            'mypy;python_version>="3"',
            'pycodestyle',
            'pylint;python_version>="3"',
            'pytest<5',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        'Source': 'https://github.com/tkukushkin/attributes-doc',
    },
)
