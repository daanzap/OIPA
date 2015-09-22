from haystack.query import SearchQuerySet
from iati.models import Activity
import time
import gc




print 'before search'
start = time.clock() 
test_lang = SearchQuerySet().filter(text='GB').values_list('pk',flat=True).stats_results()
elapsed = time.clock()
elapsed = elapsed - start
print "Time spent in search elastic is: ", elapsed



start = time.clock()
gc.disable()
activity_ids = []
activity_ids.extend(test_lang)
gc.enable()
elapsed = time.clock()
elapsed = elapsed - start
print "Time spent in converting ids new way  is: ", elapsed    

start = time.clock()
gc.disable()
activity_ids = list(test_lang[:3000000])
gc.enable()
elapsed = time.clock()
elapsed = elapsed - start
print "Time spent in converting ids is: ", elapsed    

print 'added ids'
start = time.clock() 
activities = Activity.objects.filter(pk__in=activity_ids).all()
elapsed = time.clock()
elapsed = elapsed - start
print "Time spent in gettting objects is: ", elapsed
print 'search complete'
print 'done!!!'
print len(activities)