from setuptools import setup, find_packages

setup(
    name="lune_devtoolkit_xyz",                  # Make sure this is unique on TestPyPI
    version="0.1.1",                              # Bump this version if it fails again
    author="Your Name",
    author_email="you@example.com",
    description="Lune: Advanced dev toolkit for stealth and deception modules",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/lune",  # Optional, use a real repo if you have it
    packages=find_packages(),                    # Includes all modules and subfolders with __init__.py
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Optional warning about this, but still works
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
