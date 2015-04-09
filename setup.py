import sys
import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
    readme = readme.replace('.. code-block:: none', '.. code-block::')
except:
    readme = ''

#template_dirs = [
#    "src/i18next/templates/i18next", # Core templates
#]
#static_dirs = [
#    "src/i18next/static", # Core static
#]
#locale_dirs = [
#    "src/i18next/locale/nl",
#    "src/i18next/locale/ru",
#    "src/i18next/locale/de",
#]
#
#templates = []
#static_files = []
#locale_files = []
#
#for template_dir in template_dirs:
#    templates += [os.path.join(template_dir, f) for f in os.listdir(template_dir)]
#
#for static_dir in static_dirs:
#    static_files += [os.path.join(static_dir, f) for f in os.listdir(static_dir)]
#
#for locale_dir in locale_dirs:
#    locale_files += [os.path.join(locale_dir, f) for f in os.listdir(locale_dir)]

version = '0.1.1'

install_requires = [
    'six>=1.4.1',
    'django-nine>=0.1.1',
]

tests_require = [
    'simple_timer>=0.2',
    'selenium',
    'beautifulsoup4',
]

try:
    PY2 = sys.version_info[0] == 2
    LTE_PY26 = PY2 and (7 > sys.version_info[1])
    PY3 = sys.version_info[0] == 3
    #if PY3:
    #    install_requires.append('simplejson>=3.0.0') # When using Python 3
    #else:
    #    install_requires.append('simplejson>=2.1.0') # When using Python 2.*
    #
    #if LTE_PY26:
    #    install_requires.append('ordereddict==1.1')
except:
    pass

setup(
    name = 'django-i18next',
    version = version,
    description = ("Additions to Django's i18n module."),
    long_description = "{0}".format(readme),
    classifiers = [
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or "
        "later (LGPLv2+)",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    keywords = "django, i18n, internationalisation",
    author = 'Artur Barseghyan',
    author_email = 'artur.barseghyan@gmail.com',
    url = 'https://github.com/barseghyanartur/django-i18next/',
    package_dir = {'': 'src'},
    packages = find_packages(where='./src'),
    license = 'GPL 2.0/LGPL 2.1',
    install_requires = install_requires,
    tests_require = tests_require,
    #package_data = {
    #    'i18next': templates + static_files + locale_files
    #},
    include_package_data = True,
)
