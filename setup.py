from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='fhir_curl',
    version='0.1',
    description='A CLI for querying multiple FHIR servers.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='walsbr',
    author_email='walsbr@ohsu.edu',
    url='https://github.com/bmeg/fhir_curl',
    packages=['fhir_curl'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'fhir_curl=fhir_curl.cli:cli',
        ],
    },
)
