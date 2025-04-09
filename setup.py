from setuptools import setup, find_packages

setup(
    name='amd-docs-theme',
    version='0.0.1',
    url='https://github.com/Xilinx/Image-Collateral',
    author='Your Name',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'sphinx>=2.3',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)