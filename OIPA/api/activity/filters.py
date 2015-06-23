from api.generics.filters import BasicFilter
from api.generics.filters import FilterField
from iati.models import Activity


class ActivityFilter(BasicFilter):
    activity_scope = FilterField(lookup_type='in', field='scope')
    recipient_countries = FilterField(
        lookup_type='in',
        field='recipient_country'
    )
    recipient_regions = FilterField(lookup_type='in', field='recipient_region')
    sectors = FilterField(lookup_type='in', field='sector')
    participating_organisations = FilterField(
        lookup_type='in',
        field='participating_organisation'
    )
    reporting_organisations = FilterField(
        lookup_type='in',
        field='reporting_organisation'
    )
    policy_marker = FilterField(
        lookup_type='in',
        field = 'policy_marker'
    )

    min_total_budget = FilterField(lookup_type='gte', field='total_budget')
    max_total_budget = FilterField(lookup_type='lte', field='total_budget')

    class Meta:
        model = Activity
        fields = [
            'activity_scope',
            'reporting_organisations',
            'recipient_countries',
            'recipient_regions',
            'sectors',
            'participating_organisations',
            'min_total_budget',
            'max_total_budget'
        ]
