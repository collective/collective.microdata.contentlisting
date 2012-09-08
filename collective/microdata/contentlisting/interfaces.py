# -*- coding: utf8 -*-

from zope.interface import Interface

class IMicrodataListingLayer(Interface):
    """Marker interface for the collective.microdata.contentlisting layer"""

class IItemListingView(Interface):
    """A view able to display a an item with microdatat informations"""
    
    def __call__(item, microdata, *args, **kwargs):
        """Render an item and it's microdata informations"""