"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

import pathlib

from setuptools import find_packages, setup

# Finds package directory.
here = pathlib.Path(__file__).parent.resolve()

# Uses `README.md` as long description of package.
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="sampleproject",  # Required
    version="0.0.1",  # Required
    description="A Python package template",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional
    url="https://github.com/your-name/pytemplate",  # Optional
    author="A. Random Developer",  # Optional
    author_email="author@example.com",  # Optional
    classifiers=[  # Optional
        # For a list of valid classifiers, see https://pypi.org/classifiers/
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        # These classifiers are *not* checked by 'pip install'.
        # See instead 'python_requires' below.
    ],
    keywords="template, setuptools, development",  # Optional
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.7, <4",  # Required
    install_requires=[],  # Optional
    extras_require={  # Optional
        "dev": ["yapf"],
        "test": [],
    },
    # entry_points={  # Optional
    #     "console_scripts": [
    #         "sample=sample:main",
    #     ],
    # },
    # project_urls={  # Optional
    #     "Bug Reports": "https://github.com/pypa/sampleproject/issues",
    #     "Funding": "https://donate.pypi.org",
    #     "Say Thanks!": "http://saythanks.io/to/example",
    #     "Source": "https://github.com/pypa/sampleproject/",
    # },
)
