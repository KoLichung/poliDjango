from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index','about','process_price','types','featured_case','q_and_a','contact']

    def location(self, item):
        return reverse(item)