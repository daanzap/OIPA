from haystack.query import SearchQuerySet
from iati.models import Activity
import time
import gc




print 'before search'
start = time.clock() 
test_lang = SearchQuerySet().filter(lang='en').values_list('pk',flat=True)
elapsed = time.clock()
elapsed = elapsed - start
print "Time spent in search elastic is: ", elapsed
activity_ids = []
start = time.clock()
i = 0
gc.disable()
#print test_lang
print type(test_lang)
for activty_id in test_lang[0:3000000]:
	#print type(activty_id)
	#print activty_id
   	activity_ids.append(activty_id)
   	i = i+1

gc.enable()
elapsed = time.clock()
elapsed = elapsed - start
print "Time spent in adding "+str(i)+" ids is: ", elapsed    

print 'added ids'
start = time.clock() 
activities = Activity.objects.filter(pk__in=activity_ids).all()
elapsed = time.clock()
elapsed = elapsed - start
print "Time spent in gettting objects is: ", elapsed
print 'search complete'
print 'done!!!'
print len(activities)