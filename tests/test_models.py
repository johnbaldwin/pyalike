# -*- coding: utf-8 -*-

import unittest
import tempfile
import os
import pyalike

from pyalike import models
from pyalike import FSO_DIR, FSO_FILE, FSO_LINK

class Pyalike_models_TestCase(unittest.TestCase):
    def setUp(self):
        # TODO: change this soon to
        #self.dbpath = '../tmp/test_models.sqlite'
        self.tempfn = tempfile.mkstemp(suffix='.sqlite')
        self.dbpath = self.tempfn[1]
        print "dbpath= %s" % self.dbpath
        self.db = pyalike.DB(self.dbpath, debug=True)

    def tearDown(self):
        # delete the temp path
        os.remove(self.dbpath)


    # test methods to test CRUD actions on the models

    def test_fso(self):
        path = '/a/path/to/my/file.ext'
        signature= 'abcdzefg'
        fso_type = FSO_FILE
        fso = models.FSO(path, signature, fso_type )
        print "fso=", fso
        self.db.session.add(fso)
        self.db.session.commit()



