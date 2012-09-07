Introduction
============

This package is a Plone add-on for sites where `collective.microdata.core`__ is installed. See the
product's page for more information about `microdata`__ and `schema.org implementation`__.

__ http://pypi.python.org/pypi/collective.microdata.core
__ http://en.wikipedia.org/wiki/Microdata_%28HTML%29
__ http://www.schema.org/

You could like to install this product when you need to get a set of microdata informations from your
folder contents pages.

However this product only provide basic views implementation for the `Thing`__ vocabulary. A 3rd party
product could extend it for additional vocabularies.

__ http://www.schema.org/Thing

An implementation example could be taken from looking at `collective.microdata.event`__

__ http://pypi.python.org/pypi/collective.microdata.event

Limitation and know issues
==========================

This package is a bit experimental and it overrides a couple of Plone views:

* "Standard view" (``folder_listing``)
* "Summary view" (``folder_summary_view``)

Also:

 * (right now) those views can't be used anymore for full objects (only brains).
 * this is not working on Plone site root (original views will be loaded).

How to extend
=============

Instead of directly displaying how a single content looks like, the provided view of this product will look
before for 3rd party implementations.

The customized view you are using on your folder will read from the current catalog brain the
``microdata_itemtype`` metadata, then a view with a special name is searched.

The name must be something like "``VOCABULARY_URL VIEW_ID_item``".

For example, if the current content is providing the Person vocabulary (http://www.schema.org/Person)
and you are listing it in the Plone "Standard view" (folder_listing), the view used for displaying the
single entry will be named "``http://www.schema.org/Person folder_listing_item``".

If this view is not found, the brain will be displayed with default views, provided with the product, that
will display the content in the standard Plone way.
