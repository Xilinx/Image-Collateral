from setuptools import setup, find_packages

setup(
    name="amd-docs-theme",
    version="0.2.3",
    packages=find_packages(),
    package_data={
        'amd_docs_theme': [
            "theme.conf",
            "templates/*.html",
            "static/css/*.css",
            "static/css/fonts/*.woff",
            "static/css/fonts/*.woff2",
            "static/css/fonts/*.eot",
            "static/css/fonts/*.ttf",
            "static/css/fonts/*.svg",
            "static/img/*.ico",
            "static/img/*.png",
            "static/img/*.svg",
            "static/js/*.js",
            "locale/*.pot",
            "locale/*/LC_MESSAGES/*.mo",
            "locale/*/LC_MESSAGES/*.po",
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