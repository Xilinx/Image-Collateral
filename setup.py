from setuptools import setup, find_packages

setup(
    name="amd-docs-theme",
    version="0.1.9",
    packages=find_packages(),
    package_data={
        'amd_docs_theme': [
            '_static/*', 
            '_templates/*', 
            '_themes/xilinx/*',
        ]
    },
    include_package_data=True,
    install_requires=[
        'sphinx>=5.1.1',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)