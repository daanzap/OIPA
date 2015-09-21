from haystack.query import SearchQuerySet
from iati.models import Activity
import time




print 'before search'
test_lang = SearchQuerySet().filter(lang='en');
activity_ids = []
for activty_id in test_lang:
    activity_ids.append(activty_id.pk)

print 'added ids'
start = time.clock() 
activities = Activity.objects.filter(pk__in=list(activity_ids))
elapsed = time.clock()
elapsed = elapsed - start
print "Time spent in (function name) is: ", elapsed
print 'search complete'
print 'done!!!'