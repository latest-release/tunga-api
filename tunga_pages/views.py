from django.contrib.sitemaps import Sitemap
from dry_rest_permissions.generics import DRYPermissions, DRYObjectPermissions
from rest_framework import viewsets

from tunga_pages.models import SkillPage
from tunga_pages.serializers import SkillPageSerializer


class SkillPageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Skill Page Resource
    """
    queryset = SkillPage.objects.all()
    serializer_class = SkillPageSerializer
    permission_classes = [DRYObjectPermissions]
    lookup_url_kwarg = 'keyword'
    lookup_field = 'keyword'
    lookup_value_regex = '[^/]+'
    search_fields = ('keyword', 'skill__name')


class SkillPagesSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return SkillPage.objects.filter()

    def lastmod(self, obj):
        return obj.created_at
