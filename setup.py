from setuptools import setup, find_packages

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

base_packages = [
    "numpy>=1.19.2",
    "scikit-learn>=0.23.2",
    "pandas",
    "scipy",
    "PyWavelets"

]

dev_dep = [
    "flake8>=3.8.3",
    "black>=19.10b0",
    "pre-commit>=2.5.0",
    "mypy>=0.770",
    "flake8-docstrings>=1.4.0" "pytest>=6.0.0",
    "pytest-cov>=2.10.0",
]

docs_dep = [
    "mkdocs-material>=6.1.0",
    "mkdocs-git-revision-date-localized-plugin>=0.7.2",
    "mkdocs-git-authors-plugin>=0.3.2",
    "mkdocs-table-reader-plugin>=0.4.1",
    "mkdocs-enumerate-headings-plugin>=0.4.3",
    "mkdocs-awesome-pages-plugin>=2.4.0",
    "mkdocs-minify-plugin>=0.3.0",
    "mknotebooks>=0.6.2",
    "mkdocstrings>=0.13.6",
    "mkdocs-print-site-plugin>=0.8.2",
    "mkdocs-markdownextradata-plugin>=0.1.9",
]

setup(
    name="SPOEF",
    version="0.0.3",
    description="Signal PrOcEssing Features for transaction data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jan Bargeman",
    author_email="jan_bargeman@live.nl",
    license="Open Source",
    python_requires=">=3.6",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    include_package_data=True,
    install_requires=base_packages,
    extras_require={
        "base": base_packages,
        "all": base_packages + dev_dep + docs_dep
    },
    url="https://github.com/janbargeman/SPOEF",
    packages=find_packages(".", exclude=["tests", "notebooks", "docs"]),
)
