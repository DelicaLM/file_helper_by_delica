from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='file_helper_by_delica',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description="A Python package that simplifies file IO with automatic error handling.",
    author="Delica Leboe-McGowan",
    author_email="stormindustries22@outlook.com",
    packages=['file_helper_by_delica'],
    install_requires=[

    ],
    long_description=long_description,
    long_description_type='text/markdown'
)
