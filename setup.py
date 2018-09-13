
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='documentsegmenter',
    version='0.0.1',

    description='Booking python library for machine translation',
    long_description=long_description,

    author='Fedor Kovalev',
    author_email='kovalevfm@gmail.com',
    license='MIT',

    keywords='nlp segmentation',
    packages=find_packages(exclude=['contrib', 'docs']),
    install_requires=['regex', 'six', 'spacy', 'nltk'],
    python_requires='>=2.6, <4.0',
)
