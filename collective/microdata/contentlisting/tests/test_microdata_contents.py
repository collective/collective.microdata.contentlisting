# -*- coding: utf-8 -*-

import unittest

from zope import interface
from zope.component import queryUtility, getAdapter

from collective.microdata.contentlisting.testing import MICRODATA_CONTENTLISTING_INTEGRATION_TESTING
from collective.microdata.core.interfaces import IMicrodataCoreLayer
from collective.microdata.core.interfaces import IMicrodataVocabulary

from collective.microdata.core.tests.base import ISchemaOrgMinimalBook

from collective.microdata.contentlisting.interfaces import IMicrodataListingLayer

class TestMicrodataFolderListing(unittest.TestCase):
    
    layer = MICRODATA_CONTENTLISTING_INTEGRATION_TESTING
    
    def markRequestWithLayer(self):
        # to be removed when p.a.testing will fix https://dev.plone.org/ticket/11673
        request = self.layer['request']
        interface.alsoProvides(request, IMicrodataCoreLayer)
        interface.alsoProvides(request, IMicrodataListingLayer)
    
    def setUp(self):
        self.markRequestWithLayer()
        portal = self.layer['portal']
        request = self.layer['request']
        portal.invokeFactory(type_name='Folder', id="folder")
        self.folder = portal.folder
        self.folder.invokeFactory(type_name='News Item',
                                  id='news',
                                  title="The Lord of the Rings",
                                  description="Boromir will die, sooner or later",
                                  text="All begin in the Shrine...",
                                  creator="J. R. R. Tolkien")
        self.folder.invokeFactory(type_name='Document',
                                  id='front-page',
                                  title="A useless document",
                                  description="This will be ignored",
                                  text="Lorem ipsum")
        self.folder.setLayout('@@folder_listing')
        request.set('ACTUAL_URL', 'http://nohost/plone/folder')
    
    def test_folder_listing_view_microdata_present(self):
        folder = self.folder
        self.assertTrue(folder().find('<dt itemscope="itemscope" itemtype="http://schema.org/Book">')>-1)
        self.assertTrue(folder().find('<dt itemscope="itemscope" itemtype="http://schema.org/Thing">')>-1)


        
