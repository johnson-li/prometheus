from google.appengine.ext import ndb

__author__ = 'Johnson'


class JsonData(ndb.Model):
    json = ndb.StringProperty()
