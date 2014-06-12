DEFAULT_USERNAME = "changeme"
DEFAULT_PASSWORD = "changeme"
DEFAULT_HOST = "dvn-demo.iq.harvard.edu"
DEFAULT_CERT = "dvn_client/resources/dvn-4.hmdc.harvard.edu"

EXAMPLE_DICT = {
    "title" : "ExampleTitle",
    "id" : "ExampleID",
    "author" : ["ExampleAuthor1", "ExampleAuthor2"],
    "producer" : "ExampleProducer",
    "date" : "1992-10-04",
    "description" : "ExampleDescription",
    "abstract" : "ExampleAbstract",
    "type" : "ExampleType",
    "source" : "ExampleSource",
    "restriction" : "ExampleRestriction",
    "relation" : "ExampleRelation",
    "keyword" : "ExampleKeyword",
    "coverage" : "ExampleCoverage",
    "publication" : "ExamplePublication",
}

EXAMPLE_FILE = "dvn_client/resources/atom-example.xml"


try:
    from local import *
except ImportError:
    pass