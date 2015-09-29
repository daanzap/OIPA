from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.serializers import BaseSerializer
from iati.models import Activity
from api.activity import serializers as activitySerializers
from api.activity import filters
from api.activity.aggregation import AggregationsPaginationSerializer
from api.generics.filters import BasicFilterBackend
from api.generics.filters import SearchFilter
from rest_framework.filters import DjangoFilterBackend

from api.transaction.serializers import TransactionSerializer

import json
from rest_framework.response import Response
from django.db.models import Count, Sum
from rest_framework import mixins, status

from django.db.models import Q

from geodata.models import Country, Region
from iati.models import Organisation, Sector, ActivityStatus, PolicyMarker, CollaborationType, FlowType, AidType, FinanceType, TiedStatus

from api.activity.serializers import ActivitySerializer, ActivityStatusSerializer, \
                                     ParticipatingOrganisationSerializer, PolicyMarkerSerializer, \
                                     CollaborationTypeSerializer, FlowTypeSerializer, AidTypeSerializer, FinanceTypeSerializer, TiedStatusSerializer
from api.country.serializers import CountrySerializer
from api.region.serializers import RegionSerializer
from api.sector.serializers import SectorSerializer
from api.organisation.serializers import OrganisationSerializer

class ActivityAggregationSerializer(BaseSerializer):

    _aggregations = {
        "count": {
            "field": "count",
            "annotate_name": "count",
            "annotate": Count('id')
        },
        "budget": {
            "field": "budget",
            "annotate_name": "budget",
            "annotate": Sum('budget__value')
        },
        "total_budget": {
            "field": "total_budget",
            "annotate_name": 'total_budget',
            "annotate": Sum('total_budget')
        },
        "disbursement": {
            "field": "disbursement",
            "extra_filter": Q(transaction__transaction_type='D'),
            "annotate_name": 'disbursement',
            "annotate": Sum('transaction__value'),
        },
        "expenditure": {
            "field": "expenditure",
            "extra_filter": Q(transaction__transaction_type='E'),
            "annotate_name": "expenditure",
            "annotate": Sum('transaction__value')
        },
        "commitment": {
            "field": "commitment",
            "extra_filter": Q(transaction__transaction_type='C'),
            "annotate_name": 'commitment',
            "annotate": Sum('transaction__value')
        },
        "incoming_fund": {
            "field": "incoming_fund",
            "extra_filter": Q(transaction__transaction_type='IF'),
            "annotate_name": 'incoming_fund',
            "annotate": Sum('transaction__value')
        },
    }

    _allowed_groupings = {
        "recipient_country": {
            "field": "recipient_country",
            "queryset": Country.objects.all(),
            "serializer": CountrySerializer,
            "fields": ('url', 'code', 'name'),
            # "subquery": "SELECT * FROM geodata_country WHERE geodata_country.code = recipient_country",
        },
        "recipient_region": {
            "field": "recipient_region",
            "queryset": Region.objects.all(),
            "serializer": RegionSerializer,
            "fields": ('url', 'code', 'name'),
        },
        "sector": {
            "field": "sector",
            "queryset": Sector.objects.all(),
            "serializer": SectorSerializer,
            "fields": ('url', 'code', 'name'),
        },
        "reporting_organisation": {
            "field": "reporting_organisation",
            "queryset": Organisation.objects.all(),
            "serializer": OrganisationSerializer,
            "fields": ('url', 'code', 'name'),
        },
        "participating_organisation": {
            "field": "participating_organisation",
            "queryset": Organisation.objects.all(),
            "serializer": ParticipatingOrganisationSerializer,
            "fields": ('url', 'code', 'name'),
        },
        "activity_status": {
            "field": "activity_status",
            "queryset": ActivityStatus.objects.all(),
            "serializer": ActivityStatusSerializer,
            "fields": (), # has default fields
        },
        "policy_marker": {
            "field": "policy_marker",
            "queryset": PolicyMarker.objects.all(),
            "serializer": PolicyMarkerSerializer,
            "fields": (), # has default fields
        },
        "collaboration_type": {
            "field": "collaboration_type",
            "queryset": CollaborationType.objects.all(),
            "serializer": CollaborationTypeSerializer,
            "fields": (), # has default fields
        },
        "default_flow_type": {
            "field": "default_flow_type",
            "queryset": FlowType.objects.all(),
            "serializer": FlowTypeSerializer,
            "fields": (), # has default fields
        },
        "default_aid_type": {
            "field": "default_aid_type",
            "queryset": AidType.objects.all(),
            "serializer": AidTypeSerializer,
            "fields": (), # has default fields
        },
        "default_finance_type": {
            "field": "default_finance_type",
            "queryset": FinanceType.objects.all(),
            "serializer": FinanceTypeSerializer,
            "fields": (), # has default fields
        },
        "default_tied_status": {
            "field": "default_tied_status",
            "queryset": TiedStatus.objects.all(),
            "serializer": TiedStatusSerializer,
            "fields": (), # has default fields
        },
        "budget_per_year": {
            "field": "year",
            "extra": { 
                'year': 'EXTRACT(YEAR FROM "period_start")::integer',
            },
            "queryset": None,
            "serializer": None,
            "fields": None,
        },
        "budget_per_quarter": {
            "field": "year,quarter",
            "extra": {
                'year': 'EXTRACT(YEAR FROM "period_start")::integer',
                'quarter': 'EXTRACT(QUARTER FROM "period_start")::integer',
            },
            "queryset": None,
            "serializer": None,
            "fields": None,
        },
    }

    _allowed_orderings = [ i['field'] for i in _allowed_groupings.values()]

    def apply_order_filters(self, queryset, orderList, aggregationList):

        allowed_orderings = self._allowed_orderings + aggregationList
        allowed_orderings = allowed_orderings + ['-' + o for o in allowed_orderings]

        orderings = self._intersection(allowed_orderings, orderList)

        if (len(orderings)):
            return queryset.order_by(*orderings)
        # else: 
        #     return queryset.order_by(*self._intersection(allowed_orderings, groupList))

        return queryset

    def apply_limit_offset_filters(self, queryset, page_size, page):

        if page_size:

            if not page:
                page = 1

            page_size = int(page_size)
            page = int(page)

            offset = (page * page_size) - page_size
            offset_plus_limit = offset + page_size
            return queryset[offset:offset_plus_limit]

        return queryset

    def apply_annotations(self, queryset, groupList, aggregationList):

        first_queryset = queryset
        first_annotations = dict()

        same_query_aggregations = [ i for i in aggregationList if not self._aggregations[i].get('extra_filter') ]
        separate_aggregations = [ i for i in aggregationList if self._aggregations[i].get('extra_filter') ]

        for aggregation in same_query_aggregations:
            a = self._aggregations.get(aggregation, {})
            first_annotations[a['annotate_name']] = a['annotate']
     
        # aggregations that can be performed in the same query (hence require no extra filters)
        groupings = {group: self._allowed_groupings[group] for group in groupList}
        groupFields = []
        for grouping in groupings.values():
            groupFields.extend(grouping["field"].split(','))
        groupExtras = {"select": grouping["extra"] for grouping in groupings.values() if "extra" in grouping}

        # apply extras
        # for grouping in groupings:
        first_queryset = first_queryset.extra(**groupExtras)

        # remove nulls (
        # to do: check why values() uses left outer joins,
        # this can be a lot slower than inner joins and will prevent the null
        nullFilters = {}
        for grouping in groupings.values():
            if grouping["fields"]:
                nullFilters[grouping["field"] + '__isnull'] = False
        for aggregation in same_query_aggregations:
            nullFilters[aggregation + '__isnull'] = False

        # Apply group_by calls and annotations
        result = first_queryset.values(*groupFields).annotate(**first_annotations).filter(**nullFilters)

        # aggregations that require extra filters, and hence must be exectued separately
        for aggregation in separate_aggregations:
            # field = self._aggregations.get("")
            a = self._aggregations.get(aggregation, None)
            extra_filter = a["extra_filter"]
            field = a["field"]

            annotation = dict([(a['annotate_name'], a['annotate'])])
            next_result = queryset.filter(extra_filter).values(*groupList).annotate(**annotation)
            
            main_group_field = groupList[0]


            if len(next_result):
                # join results in results object (first_result >= new_result)
                iold = iter(result)
                inew = iter(next_result)

                n = next(inew)
                for o in iold: 

                    if (n[main_group_field] == o[main_group_field]):
                        o[field] = n[field]

                        try:
                            n = next(inew)
                        except StopIteration:
                            break

        return result

    def serialize_foreign_keys(self, valuesQuerySet, request, groupList):

        serializers = {}

        for grouping in groupList:
            field_name = self._allowed_groupings[grouping]["field"]
            serializer = self._allowed_groupings[grouping]["serializer"]
            fields = self._allowed_groupings[grouping]["fields"]
            foreignQueryset = self._allowed_groupings[grouping]["queryset"]

            if fields:
                data = serializer(foreignQueryset, 
                    context={
                        'request': request,
                    },
                    many=True,
                    fields=fields,
                    query_field="%s_fields" % (field_name),
                ).data
            else: 
                data = serializer(foreignQueryset, 
                    context={
                        'request': request,
                    },
                    many=True,
                ).data

            serializers[grouping] = { i.get('code'):i for i in data }


        results = list(valuesQuerySet)

        for i, result in enumerate(list(results)):
            for k,v in result.iteritems():
                if k in groupList:
                    if v:
                        result[k] = serializers.get(k, {}).get(str(v))
                    else:
                        del results[i]

        return results

    def to_representation(self, queryset):
        request = self.context.get('request') 
        params = request.query_params

        order_by = filter(None, params.get('order_by', "").split(','))
        page_size = params.get('page_size', None)
        page = params.get('page', None)

        group_by = self._intersection(filter(None, params.get('group_by', "").split(',')), self._allowed_groupings.keys())
        aggregations = self._intersection(filter(None,params.get('aggregations', "").split(',')), self._aggregations.keys())

        if not (len(group_by) and len(aggregations)):
            return {'error_message': 'Please provide (valid values for) both mandatory fields; group_by and aggregations'}

        # queryset = self.apply_group_filters(queryset, request, group_by)
        queryset = self.apply_order_filters(queryset, order_by, aggregations)
        queryset = self.apply_annotations(queryset, group_by, aggregations)
        result = self.apply_limit_offset_filters(queryset, page_size, page)
        result = self.serialize_foreign_keys(result, request, group_by)

        return result

    def _union(self, list1, list2):
        return list(set(list1) | set(list2))

    def _intersection(self, list1, list2):
        return list(set(list1) & set(list2))


class ActivityAggregations(GenericAPIView):
    """
    Returns aggregations based on the item grouped by, and the selected aggregation.

    ## Group by options

    API request has to include `group_by` parameter.
    This parameter controls result aggregations and
    can be one or more (comma separated values) of:

    - `recipient_country`
    - `recipient_region`
    - `sector`
    - `reporting_organisation`
    - `participating_organisation`
    - `activity_status`
    - `policy_marker`
    - `collaboration_type`
    - `default_flow_type`
    - `default_aid_type`
    - `default_finance_type`
    - `default_tied_status`
    - `budget_per_year`
    - `budget_per_quarter`

    ## Aggregation options

    API request has to include `aggregations` parameter.
    This parameter controls result aggregations and
    can be one or more (comma separated values) of:

    - `count`
    - `budget`
    - `disbursement`
    - `expenditure`
    - `commitment`
    - `incoming_fund`


    ## Request parameters

    All filters available on the Activity List, can be used on aggregations.

    """

    queryset = Activity.objects.all()

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter,)
    filter_class = filters.ActivityFilter

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        results = ActivityAggregationSerializer(
            queryset,
            context=self.get_serializer_context())

        if results.data:
            if isinstance(results.data, dict) and results.data.get('error_message'):
                return Response(results.data.get('error_message'))
            return Response(results.data)
        else:
            return Response('No results', status.HTTP_204_NO_CONTENT)


class ActivityList(ListAPIView):
    """
    Returns a list of IATI Activities stored in OIPA.

    ## Request parameters
    - `ids` (*optional*): Comma separated list of activity id's.
    - `activity_scope` (*optional*): Comma separated list of iso2 country codes.
    - `recipient_country` (*optional*): Comma separated list of iso2 country codes.
    - `recipient_region` (*optional*): Comma separated list of region codes.
    - `sector` (*optional*): Comma separated list of 5-digit sector codes.
    - `sector_category` (*optional*): Comma separated list of 3-digit sector codes.
    - `reporting_organisation` (*optional*): Comma separated list of organisation id's.
    - `participating_organisation` (*optional*): Comma separated list of organisation id's.
    - `min_total_budget` (*optional*): Minimal total budget value.
    - `max_total_budget` (*optional*): Maximal total budget value.
    - `start_date_actual_lte` (*optional*): Date in YYYY-MM-DD format, returns activities earlier or equal to the given date.
    - `start_date_actual_gte` (*optional*): Date in YYYY-MM-DD format, returns activities later or equal to the given date.
    - `activity_status` (*optional*): Comma separated list of activity statuses.
    - `hierarchy` (*optional*): Comma separated list of activity hierarchies.
    - `related_activity_id` (*optional*): Comma separated list of activity ids. Returns a list of all activities mentioning these activity id's.
    - `related_activity_type` (*optional*): Comma separated list of RelatedActivityType codes.
    - `related_activity_recipient_country` (*optional*): Comma separated list of iso2 country codes.
    - `related_activity_recipient_region` (*optional*): Comma separated list of region codes.
    - `related_activity_sector` (*optional*): Comma separated list of 5-digit sector codes.
    - `related_activity_sector_category` (*optional*): Comma separated list of 3-digit sector codes.
    - `transaction_provider_activity` (*optional*): Comma separated list of activity id's.


    ## Available aggregations

    API request may include `aggregations` parameter.
    This parameter controls result aggregations and
    can be one or more (comma separated values) of:

    - `total_budget`: Calculate total budget of activities
        presented in filtered activities list.
    - `disbursement`: Calculate total disbursement of activities presented in
        filtered activities list.
    - `commitment`: Calculate total commitment of activities presented in
        filtered activities list.

    ## Searching

    API request may include `q` parameter. This parameter controls searching
    and contains expected value.

    Searching is performed on fields:

    - `activity_id`
    - `title`
    - `description`
    - `country`
    - `reporting_org` 
    - `region`
    - `sector`
    - `documentlink_title`
    - `participating_org`

    ## Result details

    Each item contains summarized information on the activity being shown,
    including the URI to activity details. To show more information, go to the
    activity's detail page or select any field using the `q_fields` parameter on the list. Example;
    `q_fields=activity_id,title,country,any_field`.


    """
    queryset = Activity.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter,)
    filter_class = filters.ActivityFilter
    serializer_class = activitySerializers.ActivitySerializer

    fields = ('url', 'id', 'title', 'total_budget',)
    pagination_class = AggregationsPaginationSerializer

    # def get_serializer_context(self):
    #     return {'request': self.request }

    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #     return Activity.objects.prefetch_related('current_activity')


class ActivityDetail(RetrieveAPIView):
    """
    Returns detailed information about Activity.

    ## URI Format

    ```
    /api/activities/{activity_id}
    ```

    ### URI Parameters

    - `activity_id`: Desired activity ID

    ## Extra endpoints

    Detailed information about activity sectors, participating organizations
    and recipient countries can be found in separate pages:

    - `/api/activities/{activity_id}/sectors`: Lists sectors activity presents
    - `/api/activities/{activity_id}/participating-orgs`: List of participating
        organizations in this activity
    - `/api/activities/{activity_id}/recipient-countries`:
        List of recipient countries.

    ## Request parameters

    - `fields` (*optional*): List of fields to display

    """
    queryset = Activity.objects.all()
    serializer_class = activitySerializers.ActivitySerializer


class ActivitySectors(ListAPIView):
    """
    Returns a list of IATI Activity Sectors stored in OIPA.

    ## URI Format

    ```
    /api/activities/{activity_id}/sectors
    ```

    ### URI Parameters

    - `activity_id`: Desired activity ID

    ## Result details

    Each result item contains:

    - `sector`: Sector name
    - `percentage`: The percentage of total commitments or total
        activity budget to this activity sector.
    - `vocabulary`: An IATI code for the vocabulary (see codelist) used
        for sector classifications.

    """
    serializer_class = activitySerializers.ActivitySectorSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Activity(pk=pk).activitysector_set.all()


class ActivityParticipatingOrganisations(ListAPIView):
    """
    Returns a list of IATI Activity Participating Organizations stored in OIPA.

    ## URI Format

    ```
    /api/activities/{activity_id}/participating-orgs
    ```

    ### URI Parameters

    - `activity_id`: Desired activity ID

    """
    serializer_class = activitySerializers.ParticipatingOrganisationSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Activity(pk=pk).participating_organisations.all()


class ActivityRecipientCountries(ListAPIView):
    """
    Returns a list of IATI Activity Recipient Countries stored in OIPA.

    ## URI Format

    ```
    /api/activities/{activity_id}/recipient-countries
    ```

    ### URI Parameters

    - `activity_id`: Desired activity ID

    """
    serializer_class = activitySerializers.RecipientCountrySerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Activity(pk=pk).activityrecipientcountry_set.all()


class ActivityRecipientRegions(ListAPIView):
    """
    Returns a list of IATI Activity Recipient Regions stored in OIPA.

    ## URI Format

    ```
    /api/activities/{activity_id}/recipient-regions
    ```

    ### URI Parameters

    - `activity_id`: Desired activity ID

    """
    serializer_class = activitySerializers.ActivityRecipientRegionSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Activity(pk=pk).activityrecipientregion_set.all()


class ActivityTransactions(ListAPIView):
    """
    Returns a list of IATI Activity Transactions stored in OIPA.

    ## URI Format

    ```
    /api/activities/{activity_id}/transactions
    ```

    ### URI Parameters

    - `activity_id`: Desired activity ID

    ## Request parameters:

    - `recipient_country` (*optional*): Recipient countries list.
        Comma separated list of strings.
    - `recipient_region` (*optional*): Recipient regions list.
        Comma separated list of integers.
    - `sector` (*optional*): Sectors list. Comma separated list of integers.
    - `sector_category` (*optional*): Sectors list. Comma separated list of integers.
    - `reporting_organisations` (*optional*): Organisation ID's list.
    - `participating_organisations` (*optional*): Organisation IDs list.
        Comma separated list of strings.
    - `min_total_budget` (*optional*): Minimal total budget value.
    - `max_total_budget` (*optional*): Maximal total budget value.
    - `activity_status` (*optional*):


    - `related_activity_id` (*optional*):
    - `related_activity_type` (*optional*):
    - `related_activity_recipient_country` (*optional*):
    - `related_activity_recipient_region` (*optional*):
    - `related_activity_sector` (*optional*):

    ## Searching is performed on fields:

    - `description`
    - `provider_organisation_name`
    - `receiver_organisation_name`

    """
    serializer_class = TransactionSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Activity(pk=pk).transaction_set.all()
