# -*- coding: utf8 -*-

from zope.interface import implements

from zope.component import queryAdapter, getMultiAdapter
from zope.component.interfaces import ComponentLookupError

from Products.Five.browser import BrowserView
from plone.memoize import view

from collective.microdata.core.interfaces import IMicrodataVocabulary

from collective.microdata.contentlisting.interfaces import IItemListingView

class BaseListingView(BrowserView):

    TEMPLATE_ID = ''

    @view.memoize
    def get_microdata(self, brain):
        # look for a type-specific adapter, if any
        adapter = queryAdapter(brain, interface=IMicrodataVocabulary,
                               name=brain.microdata_itemtype)
        if not adapter:
            # fallback to basic Thing adapter
            adapter = queryAdapter(brain, interface=IMicrodataVocabulary,
                                   name=u'')            
        return adapter


    def render_item(self, item):
        microdata = self.get_microdata(item)
        try:
            view = getMultiAdapter ((self.context, self.request),
                                    name='%s %s_item' % (microdata.microdata_vocabulary, self.TEMPLATE_ID))
        except ComponentLookupError:
            view = getMultiAdapter ((self.context, self.request),
                                    name='%s_item' % self.TEMPLATE_ID)
        return view(item, microdata)


class ListingView(BaseListingView):
    """View for the folder_listing template"""
    TEMPLATE_ID = 'folder_listing'


class SummaryView(BaseListingView):
    """View for the folder_summary_view template"""

    TEMPLATE_ID = 'folder_summary_view'


class BaseItemListingView(BrowserView):
    """Base class for listing a single item"""
    implements(IItemListingView)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.item = None
    
    def __call__(self, item, microdata, *args, **kwargs):
        self.item = item
        self.microdata = microdata
        return self.index()
