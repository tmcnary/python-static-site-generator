import typer
from ssg.site import Site

def __main__(self, source="content", dest="dist"):
    config = {"source":source, "dest":dest}
#     Site(config).glob().build()