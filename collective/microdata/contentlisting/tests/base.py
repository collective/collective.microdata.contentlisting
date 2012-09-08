# -*- coding: utf8 -*-

from Products.Five.browser import BrowserView

class NewsItemTestingMicrodataFolderListingAdapter(BrowserView):
    
    def __call__(self, item, microdata, *args, **kwargs):
        return \
"""<dt itemscope="itemscope" itemtype="http://schema.org/Book">
<span itemprop="name">Let\'s display the "%s" book</span>
</dt>
""" % microdata.name


class NewsItemTestingMicrodataFolderSummaryViewAdapter(BrowserView):
    
    def __call__(self, item, microdata, *args, **kwargs):
        return \
"""<div class="tileItem visualIEFloatFix" itemscope="itemscope" itemtype="http://schema.org/Book">
    <h2 class="tileHeadline">
        <a href="http://nohost/plone/folder/news" class="summary url" itemprop="url">
            <span itemprop="name">Let\'s summarize the "%s" book</span>
        </a>
    </h2>
</div>
""" % microdata.name

