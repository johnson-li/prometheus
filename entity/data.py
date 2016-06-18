from google.appengine.ext import ndb

__author__ = 'Johnson'


class JsonData(ndb.Model):
    json = ndb.StringProperty()


class ApiRequestData(ndb.Model):
    """
    https/http2 request/response data sizes are all within tcp layer
    """
    hostName = ndb.StringProperty()
    targetUrl = ndb.StringProperty()
    traceRoute = ndb.StringProperty(indexed=False)
    httpsTransferTime = ndb.IntegerProperty(repeated=True, indexed=False)
    http2TransferTime = ndb.IntegerProperty(repeated=True, indexed=False)
    timeStamp = ndb.IntegerProperty()
    requestTimes = ndb.IntegerProperty()
    httpsRequestSize = ndb.IntegerProperty()
    httpsResponseSize = ndb.IntegerProperty()
    http2RequestSize = ndb.IntegerProperty()
    http2ResponseSize = ndb.IntegerProperty()


class TrafficSizeData(ndb.Model):
    """
    TrafficSizeData records data size in physical layer
    """
    hostName = ndb.StringProperty()
    targetUrl = ndb.StringProperty()
    timeStamp = ndb.IntegerProperty()
    requestTimes = ndb.IntegerProperty()
    httpsRequestSize = ndb.IntegerProperty()
    httpsResponseSize = ndb.IntegerProperty()
    http2RequestSize = ndb.IntegerProperty()
    http2ResponseSize = ndb.IntegerProperty()


class Http2SupportData(ndb.Model):
    """
    Log whether a host supports http2 or not
    """
    host = ndb.StringProperty()
    source = ndb.StringProperty()
    timeStamp = ndb.IntegerProperty()
    support = ndb.BooleanProperty()
    errors = ndb.StringProperty(repeated=True, indexed=False)
