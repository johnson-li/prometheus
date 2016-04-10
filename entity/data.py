from google.appengine.ext import ndb

__author__ = 'Johnson'


class JsonData(ndb.Model):
    json = ndb.StringProperty()


class ApiRequestData(ndb.Model):
    hostName = ndb.StringProperty()
    targetUrl = ndb.StringProperty()
    traceRoute = ndb.StringProperty()
    transferTimes = ndb.IntegerProperty(repeated=True)
