from setuptools import setup, find_packages
import os

version = '0.1'

tests_require = ['plone.app.testing']

setup(name='collective.microdata.contentlisting',
      version=version,
      description="Folders and collections listing support for microdata in Plone",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        ],
      keywords='plone microdata schema.org html5 listing folder',
      author='keul',
      author_email='luca@keul.it',
      url='https://github.com/keul/collective.microdata.contentlisting',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.microdata'],
      include_package_data=True,
      zip_safe=False,
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      install_requires=[
          'setuptools',
          'collective.microdata.core',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
