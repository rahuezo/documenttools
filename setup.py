from setuptools import setup

setup(
    name='documenttools',
    version='0.1',
    description='A set of tools for comparing documents, tagging documents for keywords, tagging documents using NER, and computing document statistics.',
    url='https://github.com/rahuezo/documenttools',
    author='Rudy Huezo',
    author_email='rahuezo@ucdavis.edu',
    license='MIT',
    packages=['documenttools', 'documenttools.files', 'documenttools.statistics', 'documenttools.taggers'],
    zip_safe=False

)
