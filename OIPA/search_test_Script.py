from haystack.query import SearchQuerySet
from iati.models import Activity


print 'before search'
test_lang = SearchQuerySet().filter(lang='en');
activity_ids = []
for activty_id in test_lang:
    activity_ids.append(activty_id.pk)

print 'added ids'

activities = Activity.objects.filter(pk__in=list(activity_ids))
print 'search complete'
print 'done!!!'