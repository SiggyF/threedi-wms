from setuptools import setup

version = '0.1dev'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CREDITS.rst').read(),
    open('CHANGES.rst').read(),
    ])

install_requires = [
    'celery',
    'Flask',
    'gislib',
    'gunicorn',
    'matplotlib',
    'netCDF4',
    'Pillow',
    'requests',
    'scipy',
    'setuptools',
    'SQLAlchemy',
    ],

tests_require = [
    'nose',
    'coverage',
    ]

setup(name='threedi-wms',
      version=version,
      description="TODO",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords=[],
      author='TODO',
      author_email='TODO@nelen-schuurmans.nl',
      url='',
      license='GPL',
      packages=['threedi_wms'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points={
          'console_scripts': [
              'flask=server.app:run',
              'sandbox=sandbox.sandbox:main',
          ]},
      )
