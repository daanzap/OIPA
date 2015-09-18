from haystack.query import SearchQuerySet
from iati.models import Activity


test_lang = SearchQuerySet().filter(lang='en');
activity_ids = []
for activty_id in test_lang:
    activity_ids.append(activty_id.pk)

activities = Activity.objects.filter(pk__in=activity_ids)
for activity in activities:
    print activity.id

print 'done!!!'