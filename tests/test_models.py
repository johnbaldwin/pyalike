# -*- coding: utf-8 -*-

import unittest

import pyalike

from pyalike import models
from pyalike import FSO_DIR, FSO_FILE, FSO_LINK

class Pyalike_models_TestCase(unittest.TestCase):
    def setUp(self):
        # TODO: change this soon to
        self.dbpath = '../tmp/test_models.sqlite'
        self.db = pyalike.DB()

    def tearDown(self):
        # delete the temp path
        pass

    # test methods to test CRUD actions on the models

    def test_fso(self):
        path = '/a/path/to/my/file.ext'
        signature= 'abcdzefg'
        fso_type = FSO_FILE
        fso = models.FSO(path, signature, fso_type )
        self.db.session.add(fso)
        self.db.session.commit()



