from haystack.query import SearchQuerySet
from iati.models import Activity
import time




print 'before search'
start = time.clock() 
test_lang = SearchQuerySet().filter(lang='en').values_list('pk',flat=True)
elapsed = time.clock()
elapsed = elapsed - start
print "Time spent in search elastic is: ", elapsed
print test_lang
#activity_ids = list(test_lang)
print activity_ids
# start = time.clock()
# i = 0
# #print test_lang
# for activty_id in test_lang:
# 	#print activty_id
#    	activity_ids.append(activty_id['pk'])
#    	i = i+1

# elapsed = time.clock()
# elapsed = elapsed - start
# print "Time spent in adding "+str(i)+" ids is: ", elapsed    

print 'added ids'
start = time.clock() 
activities = Activity.objects.filter(pk__in=test_lang)
elapsed = time.clock()
elapsed = elapsed - start
print "Time spent in (function name) is: ", elapsed
print 'search complete'
print 'done!!!'
print len(activities)