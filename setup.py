import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(
    name="aiidalab-qe-eos-demo",
    version="0.0.1",
    description="A aiidalab-qe plugin to calculate the equation of state of a crystal.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/aiidalab/aiidalab-qe-eos-demo",
    author="AiiDalab team",
    author_email="aiidalab@materialscloud.org",
    classifiers=[],
    packages=find_packages(),
    entry_points={
        "aiidalab_qe.properties": [
            "eos = aiidalab_qe_eos:eos",
        ],
    },
    install_requires=[

    ],
    package_data={},
    python_requires=">=3.6",
)
