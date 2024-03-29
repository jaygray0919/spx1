
# display name and photo of each Nobel Prize winner as the item.

from BaseCollection import BaseCollection
from html import *

class Collection(BaseCollection):
    PAGE_TITLE = 'Nobel Prize'
    PAGE_HEADING = ''
    PAGE_SUBHEADING = ''

    def __init__(self, db):
        self.db = db

        # Always show all the facets.
        self.facetlist = db.facetlist

        # Don't show the attributes that contain URLs.
        self.attrlist = [
            attr for attr in db.attrlist
            if attr not in ['britannica_url','dbpedia_url','graph_url','sparql_url','timeline_url','wikidata_url','wikipedia_url','photo_logo']]

    def itemdisplay(self, item, request):
        metadata = self.db.metadata(item)
        if metadata['date_birth'] or metadata['date_death']:
            lifespan = [metadata['date_birth'], '-', metadata['date_death']]
        else:
            lifespan = []
        links = []
        if metadata['britannica_url']:
            links += [br, link(metadata['britannica_url'], 'Encyclopedia Britannica')]
        if metadata['dbpedia_url']:
            links += [br, link(metadata['dbpedia_url'], 'DBpedia')]
        if metadata['graph_url']:
            links += [br, link(metadata['graph_url'], 'Graph')]
        if metadata['sparql_url']:
            links += [br, link(metadata['sparql_url'], 'SPARQL')]
        if metadata['timeline_url']:
            links += [br, link(metadata['timeline_url'], 'Timeline')]
        if metadata['wikidata_url']:
            links += [br, link(metadata['wikidata_url'], 'Wikidata')]
        if metadata['wikipedia_url']:
            links += [br, link(metadata['wikipedia_url'], 'Wikipedia')]
        return [img(metadata['photo_logo']), br,
                metadata['name_usual'], br, lifespan, links]

    def itemlisting(self, item, index, link=None, query=None, **args):
        metadata = self.db.metadata(item)
        listing = [img(metadata['photo_logo']), br,
                   abbrev(metadata['name_usual'], 20), br,
                   metadata['date_birth'], '-', metadata['date_death']]
        if link:
            listing = link(listing, query=query, index=index)
        return listing
