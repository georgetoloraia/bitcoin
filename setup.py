from setuptools import setup, find_packages # type: ignore

setup(
    name="bitcoin",
    version="0.1.0",
    description="A Python-based blockchain implementation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="George Toloraia",
    author_email="georgetoloraia@gmail.com",
    url="https://github.com/georgetoloraia/bitcoin",
    packages=find_packages(exclude=["tests", "docs"]),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    python_requires=">=3.7",
    install_requires=[
        "cryptography>=3.4.7",
        "protobuf>=3.20.0",
        "flask>=2.0.0",
        "requests>=2.25.1",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=22.0",
            "flake8>=3.9",
        ],
    },
    entry_points={
        "console_scripts": [
            "run_node=network.p2p:start_node",  # Example entry point for running the node
        ],
    },
    project_urls={
        "Bug Tracker": "https://github.com/georgetoloraia/bitcoin/issues",
        "Source Code": "https://github.com/georgetoloraia/bitcoin",
    },
)
