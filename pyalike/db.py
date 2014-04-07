# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from pyalike import models

class DB(object):

    Base = declarative_base()

    def __init__(self, dbpath, *args, **kwargs):
        self.dbstr = 'sqlite:///'+dbpath
        self.debug = kwargs.get('debug', False)

        if self.debug:
            print 'DB_Engine path = %s' % self.dbstr

        self.engine = create_engine(self.dbstr, echo=self.debug)

        models.Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

