from setuptools import setup, find_packages
import os

version = '0.6.1'

setup(
    name='avrc.ari.theme',
    version=version,
    description="AIDS Research Institute XDV Theme",
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
    keywords='',
    author='BEAST Core Development Team',
    author_email='beast@ucsd.edu',
    url='http://datam0nk3y.org/',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'':'src'},
    namespace_packages=['avrc', 'avrc.ari'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.app.theming',
        ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
