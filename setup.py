# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2016 by the GFDRR / World Bank
#
# This file is part of ThinkHazard.
#
# ThinkHazard is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# ThinkHazard is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# ThinkHazard.  If not, see <http://www.gnu.org/licenses/>.

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()

requires = [
    'geoalchemy2',
    'psycopg2',
    'pyramid == 1.10.4',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'simplejson',
    'SQLAlchemy',
    'shapely',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'papyrus',
    'WebTest',
    'nose',
    'pyquery',
    'markdown',
    'APScheduler',
    'paste',
    'alembic',
    'pytidylib',
    ]

setup(name='thinkhazard',
      version='2.0-dev',
      description='thinkhazard',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='thinkhazard',
      install_requires=requires,
      entry_points={
          "paste.app_factory": [
              "main = thinkhazard:main"
          ],
          "console_scripts": [
              "initialize_thinkhazard_db = thinkhazard.scripts.initializedb:main",
              "import_admindivs = thinkhazard.scripts.import:import_admindivs",
              "import_recommendations = thinkhazard.scripts.import:import_recommendations",
              "import_further_resources = thinkhazard.scripts.import_further_resources:main",
              "import_contacts = thinkhazard.scripts.import:import_contacts",
              "harvest = thinkhazard.processing.harvesting:Harvester.run",
              "download = thinkhazard.processing.downloading:Downloader.run",
              "complete = thinkhazard.processing.completing:Completer.run",
              "process = thinkhazard.processing.processing:Processor.run",
              "decision_tree = thinkhazard.processing.decisiontree:DecisionMaker.run",
              "publish = thinkhazard.scripts.publish:main",
              "importpo = thinkhazard.scripts.importpo:main",
          ],
          "lingua.extractors": [
              "database = thinkhazard.lib.lingua_extractor:DatabaseExtractor",
              "enum = thinkhazard.lib.lingua_extractor:EnumExtractor"
          ],
      }
)
