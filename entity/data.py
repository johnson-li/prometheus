from google.appengine.ext import ndb

__author__ = 'Johnson'


class JsonData(ndb.Model):
    json = ndb.StringProperty()


class ApiRequestData(ndb.Model):
    hostName = ndb.StringProperty()
    targetUrl = ndb.StringProperty()
    traceRoute = ndb.StringProperty(indexed=False)
    httpsTransferTime = ndb.IntegerProperty(repeated=True, indexed=False)
    http2TransferTime = ndb.IntegerProperty(repeated=True, indexed=False)
    timeStamp = ndb.IntegerProperty()
