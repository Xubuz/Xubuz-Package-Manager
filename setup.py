from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Xubuz Package Manager"
LONG_DESCRIPTION = "A package manager for Xubuz Linux."

setup(
    name="XubuzPM",
    version=VERSION,
    author="Ayush K M",
    author_email="kmayushkm@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "Package Manager", "xubuz"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
