# -*- coding: utf-8 -*-

import os
import sys
import datetime

from sqlalchemy import Column
from sqlalchemy.types import Integer, SmallInteger, String, DateTime, UnicodeText
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property

Base = declarative_base()


# TODO: Add loading info from File system

# File System Object. For persisting our file signatures
# Maybe change the name to something like FileSig, FileDigest, FileRecord (maybe not this one, to ambiguous)
class FSO(Base):

    __tablename__ = 'fsos'

    id = Column(Integer, primary_key=True)
    path = Column(String)
    signature = Column(String)
    fso_type = Column(SmallInteger)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    # updated_at = Column(DateTime, default=datetime.datetime.utcnow)


    def __init__(self, path, signature, fso_type):
        self.path = path
        self.signature = signature
        self.fso_type = fso_type

    def __repr__(self):
        return "<Pyalike.FSO('%s','%s','%s','%s')>" % ( self.id, self.path, self.signature, self.fso_type)

    # tODO: add standard to_xyz methods, namely json at this point