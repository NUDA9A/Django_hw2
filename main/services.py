from django.conf import settings
from django.core.cache import cache


def get_cached_categories_list(self):
    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = self.object_list
            cache.set(key, category_list)
    else:
        category_list = self.object_list
    return category_list
