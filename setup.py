"""Setup remotepixel-tiler"""

from setuptools import setup, find_packages

with open("lambda_tiler/__init__.py") as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue

# Runtime requirements.
inst_reqs = ["rio-tiler~=1.2", "lambda-proxy~=4.1.4", "rio-color"]

extra_reqs = {
    "test": ["mock", "pytest", "pytest-cov"],
    "dev": ["mock", "pytest", "pytest-cov", "pre-commit"],
}

setup(
    name="lambda-tiler",
    version=version,
    description=u"""""",
    long_description=u"",
    python_requires=">=3",
    classifiers=["Programming Language :: Python :: 3.6"],
    keywords="",
    author=u"Vincent Sarago",
    author_email="contact@remotepixel.ca",
    url="https://github.com/vincentsarago/lambda_tiler",
    license="BSD",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=inst_reqs,
    extras_require=extra_reqs,
    entry_points={"console_scripts": ["lambda-tiler = lambda_tiler.scripts.cli:run"]},
)
