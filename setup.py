from setuptools import setup, find_packages
import os

version = '0.4'

setup(name='avrc.ari.theme',
    version=version,
    description="AIDS Research Institute XDV Theme",
    long_description=open("README.txt").read() + "\n" +
                     open(os.path.join("docs", "HISTORY.txt")).read(),
    # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
      "Framework :: Plone",
      "Programming Language :: Python",
      ],
    keywords='',
    author='',
    author_email='',
    url='http://svn.plone.org/svn/collective/',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'':'src'},
    namespace_packages=['avrc', 'avrc.ari'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.app.theming',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
