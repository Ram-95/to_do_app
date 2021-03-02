from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'never'

    def items(self):
        return ['register', 'login', 'logout', 'profile', 'edit_profile']

    def location(self, item):
        return reverse(item)
