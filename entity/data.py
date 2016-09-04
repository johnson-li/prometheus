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
    httpsRequestSizeTcp = ndb.IntegerProperty()
    httpsResponseSizeTcp = ndb.IntegerProperty()
    http2RequestSizeTcp = ndb.IntegerProperty()
    http2ResponseSizeTcp = ndb.IntegerProperty()


class Http2SupportData(ndb.Model):
    """
    Log whether a host supports http2 or not
    """
    host = ndb.StringProperty()
    source = ndb.StringProperty()
    timeStamp = ndb.IntegerProperty()
    support = ndb.BooleanProperty()
    errors = ndb.StringProperty(repeated=True, indexed=False)


class FullWebData(ndb.Model):
    """
    Format of traces:
        [{'url': url, 'time_elapsed': time_elapsed}, ...]
    """
    hostName = ndb.StringProperty()
    targetUrl = ndb.StringProperty()
    timeStamp = ndb.IntegerProperty()
    httpsTraces = ndb.JsonProperty(indexed=False)
    http2Traces = ndb.JsonProperty(indexed=False)
    httpsRequestSize = ndb.IntegerProperty(indexed=False)
    httpsResponseSize = ndb.IntegerProperty(indexed=False)
    http2RequestSize = ndb.IntegerProperty(indexed=False)
    http2ResponseSize = ndb.IntegerProperty(indexed=False)
    httpsRequestSizeTcp = ndb.IntegerProperty(indexed=False)
    httpsResponseSizeTcp = ndb.IntegerProperty(indexed=False)
    http2RequestSizeTcp = ndb.IntegerProperty(indexed=False)
    http2ResponseSizeTcp = ndb.IntegerProperty(indexed=False)
    httpsTransferTime = ndb.IntegerProperty(indexed=False)
    http2TransferTime = ndb.IntegerProperty(indexed=False)


class MultiConnData(ndb.Model):
    """
    Format of traces:
        [{'url': url, 'time_elapsed': time_elapsed}, ...]
    Format of channel size:
        {channel: traffic_size, ...}
    """
    hostName = ndb.StringProperty()
    targetUrl = ndb.StringProperty()
    timeStamp = ndb.IntegerProperty()
    httpsTraces = ndb.JsonProperty(indexed=False)
    http2Traces = ndb.JsonProperty(indexed=False)
    httpsChannelRequestSize = ndb.JsonProperty(indexed=False)
    httpsChannelResponseSize = ndb.JsonProperty(indexed=False)
    httpsRequestSize = ndb.IntegerProperty(indexed=False)
    httpsResponseSize = ndb.IntegerProperty(indexed=False)
    http2RequestSize = ndb.IntegerProperty(indexed=False)
    http2ResponseSize = ndb.IntegerProperty(indexed=False)
    httpsRequestSizeTcp = ndb.IntegerProperty(indexed=False)
    httpsResponseSizeTcp = ndb.IntegerProperty(indexed=False)
    http2RequestSizeTcp = ndb.IntegerProperty(indexed=False)
    http2ResponseSizeTcp = ndb.IntegerProperty(indexed=False)
    httpsTransferTime = ndb.IntegerProperty(indexed=False)
    http2TransferTime = ndb.IntegerProperty(indexed=False)
    httpsRequestSizeTcpTcpdump = ndb.IntegerProperty(indexed=False)
    httpsResponseSizeTcpTcpdump = ndb.IntegerProperty(indexed=False)
    http2RequestSizeTcpTcpdump = ndb.IntegerProperty(indexed=False)
    http2ResponseSizeTcpTcpdump = ndb.IntegerProperty(indexed=False)
    httpsTcpdumpPacketsDrop = ndb.IntegerProperty()
    http2TcpdumpPacketsDrop = ndb.IntegerProperty()
