import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="featureflow-sdk",
    version="0.2.0",
    author="Featureflow",
    author_email="featureflow@featureflow.io",
    description="Python 3 SDK for the featureflow feature management platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/featureflow/featureflow-python-sdk",
    packages=setuptools.find_packages(include=['featureflow', 'featureflow.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
    extras_require={
        'test': ['behave', 'Faker'],
    },
    python_requires='>=3.7',
)
