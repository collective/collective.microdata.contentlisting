# -*- coding: utf-8 -*-

import zope.component
import zope.interface

from zope.configuration import xmlconfig

import zope.publisher.interfaces.browser

from plone.testing import z2

from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from collective.microdata.core.testing import MicrodataCore

import collective.microdata.contentlisting.interfaces
import collective.microdata.contentlisting.tests.base

class MicrodataContentListing(MicrodataCore):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        MicrodataCore.setUpZope(self, app, configurationContext)
        # Load ZCML for this package
        import collective.microdata.contentlisting
        xmlconfig.file('configure.zcml',
                       collective.microdata.contentlisting,
                       context=configurationContext)
        z2.installProduct(app, 'collective.microdata.contentlisting')

        zope.component.provideAdapter(
            collective.microdata.contentlisting.tests.base.NewsItemTestingMicrodataFolderListingAdapter,
            (zope.interface.Interface,
             collective.microdata.contentlisting.interfaces.IMicrodataListingLayer),
            provides=zope.publisher.interfaces.browser.IBrowserView,
            name=u'http://schema.org/Book folder_listing_item'
        )

        zope.component.provideAdapter(
            collective.microdata.contentlisting.tests.base.NewsItemTestingMicrodataFolderSummaryViewAdapter,
            (zope.interface.Interface,
             collective.microdata.contentlisting.interfaces.IMicrodataListingLayer),
            provides=zope.publisher.interfaces.browser.IBrowserView,
            name=u'http://schema.org/Book folder_summary_view_item'
        )


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.microdata.contentlisting:default')
        setRoles(portal, TEST_USER_ID, ['Member', 'Manager'])


MICRODATA_CONTENTLISTING_FIXTURE = MicrodataContentListing()
MICRODATA_CONTENTLISTING_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(MICRODATA_CONTENTLISTING_FIXTURE, ),
                       name="MicrodataContentListing:Integration")
MICRODATA_CONTENTLISTING_FUNCTIONAL_TESTING = \
    FunctionalTesting(bases=(MICRODATA_CONTENTLISTING_FIXTURE, ),
                       name="MicrodataContentListing:Functional")

