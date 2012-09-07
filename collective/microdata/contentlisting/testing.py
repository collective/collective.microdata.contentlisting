# -*- coding: utf-8 -*-

import zope.component
from zope.configuration import xmlconfig

from Products.ZCatalog.interfaces import ICatalogBrain

from plone.testing import z2

from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from collective.microdata.core.testing import MicrodataCore
from collective.microdata.core.tests.base import NewsItemTestingMicrodataAdapter
from collective.microdata.core.tests.base import NewsItemTestingMicrodataBrainAdapter
from collective.microdata.core.interfaces import IMicrodataVocabulary

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

