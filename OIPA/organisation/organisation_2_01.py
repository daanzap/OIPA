from iati.genericXmlParser import XMLParser
from iati import models
from geodata.models import Country, Region
from iati.deleter import Deleter
from iati_synchroniser.exception_handler import exception_handler
from re import sub
import hashlib
import dateutil.parser
import time
import datetime
import re
from django.conf import settings

_slugify_strip_re = re.compile(r'[^\w\s-]')
_slugify_hyphenate_re = re.compile(r'[-\s]+')

class Parse(XMLParser):

	def __init__(self):
		pass

	'''atributes:
        last-updated-datetime:2013-08-28T13:40:52.98
        {http://www.w3.org/XML/1998/namespace}lang:en
        default-currency:USD

    tag:iati-organisation
    found in http://maps.aidsalliance.org/iati/organisation.xml at line 1 iati_version =2.01'''
    def iati_organisations__iati_organisation(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        {http://www.w3.org/XML/1998/namespace}lang:en
        file-id:21020
        source-url:http://maps.aidsalliance.org/iati/organisation.xml
        publisher-id:21020
        publisher-role:Reporting
        contact-email:iati@aidsalliance.org
        activity-period:All Periods
        last-updated-datetime:2013-08-28T14:16:15Z
        generated-datetime:2013-08-28T14:16:15Z
        verification-status:1
        format:xml
        license:IATI

    tag:{http://iatiregistry.org/ns/record#}registry-record
    found in http://maps.aidsalliance.org/iati/organisation.xml at line 2 iati_version =2.01'''
    def iati_organisations__iati_organisation__ir:registry_record(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        ref:21020
        type:21

    tag:reporting-org
    found in http://maps.aidsalliance.org/iati/organisation.xml at line 3 iati_version =2.01'''
    def iati_organisations__iati_organisation__reporting_org(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:

    tag:iati-identifier
    found in http://maps.aidsalliance.org/iati/organisation.xml at line 4 iati_version =2.01'''
    def iati_organisations__iati_organisation__iati_identifier(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:

    tag:name
    found in http://maps.aidsalliance.org/iati/organisation.xml at line 5 iati_version =2.01'''
    def iati_organisations__iati_organisation__name(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:

    tag:total-budget
    found in http://maps.aidsalliance.org/iati/organisation.xml at line 6 iati_version =2.01'''
    def iati_organisations__iati_organisation__total_budget(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        iso-date:2012-01-01

    tag:period-start
    found in http://maps.aidsalliance.org/iati/organisation.xml at line 7 iati_version =2.01'''
    def iati_organisations__iati_organisation__total_budget__period_start(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        iso-date:2012-12-31

    tag:period-end
    found in http://maps.aidsalliance.org/iati/organisation.xml at line 8 iati_version =2.01'''
    def iati_organisations__iati_organisation__total_budget__period_end(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        currency:USD
        value-date:2012-12-31

    tag:value
    found in http://maps.aidsalliance.org/iati/organisation.xml at line 9 iati_version =2.01'''
    def iati_organisations__iati_organisation__total_budget__value(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        url:http://www.aidsalliance.org/includes/Publication/Alliance_AR_2012_EN_WEB_Final.pdf
        format:application/pdf

    tag:document-link
    found in http://maps.aidsalliance.org/iati/organisation.xml at line 10 iati_version =2.01'''
    def iati_organisations__iati_organisation__document_link(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        {http://www.w3.org/XML/1998/namespace}lang:en

    tag:title
    found in http://maps.aidsalliance.org/iati/organisation.xml at line 11 iati_version =2.01'''
    def iati_organisations__iati_organisation__document_link__title(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        code:B01
        {http://www.w3.org/XML/1998/namespace}lang:en

    tag:category
    found in http://maps.aidsalliance.org/iati/organisation.xml at line 12 iati_version =2.01'''
    def iati_organisations__iati_organisation__document_link__category(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:

    tag:organisation-identifier
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 8 iati_version =2.01'''
    def iati_organisations__iati_organisation__organisation_identifier(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:

    tag:narrative
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 12 iati_version =2.01'''
    def iati_organisations__iati_organisation__name__narrative(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:

    tag:narrative
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 18 iati_version =2.01'''
    def iati_organisations__iati_organisation__reporting_org__narrative(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        ref:1234

    tag:budget-line
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 27 iati_version =2.01'''
    def iati_organisations__iati_organisation__total_budget__budget_line(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        currency:USD
        value-date:2014-01-01

    tag:value
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 28 iati_version =2.01'''
    def iati_organisations__iati_organisation__total_budget__budget_line__value(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:

    tag:narrative
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 29 iati_version =2.01'''
    def iati_organisations__iati_organisation__total_budget__budget_line__narrative(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:

    tag:recipient-org-budget
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 34 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_org_budget(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        ref:AA-ABC-1234567

    tag:recipient-org
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 35 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_org_budget__recipient_org(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:

    tag:narrative
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 36 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_org_budget__recipient_org__narrative(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        iso-date:2014-01-01

    tag:period-start
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 38 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_org_budget__period_start(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        iso-date:2014-12-31

    tag:period-end
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 39 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_org_budget__period_end(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        currency:USD
        value-date:2014-01-01

    tag:value
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 40 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_org_budget__value(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        ref:1234

    tag:budget-line
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 41 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_org_budget__budget_line(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        currency:USD
        value-date:2014-01-01

    tag:value
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 42 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_org_budget__budget_line__value(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:

    tag:narrative
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 43 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_org_budget__budget_line__narrative(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:

    tag:recipient-country-budget
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 48 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_country_budget(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        code:AF

    tag:recipient-country
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 49 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_country_budget__recipient_country(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        iso-date:2014-01-01

    tag:period-start
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 50 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_country_budget__period_start(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        iso-date:2014-12-31

    tag:period-end
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 51 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_country_budget__period_end(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        currency:USD
        value-date:2014-01-01

    tag:value
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 52 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_country_budget__value(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        ref:1234

    tag:budget-line
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 53 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_country_budget__budget_line(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        currency:USD
        value-date:2014-01-01

    tag:value
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 54 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_country_budget__budget_line__value(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:

    tag:narrative
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 55 iati_version =2.01'''
    def iati_organisations__iati_organisation__recipient_country_budget__budget_line__narrative(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:

    tag:narrative
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 62 iati_version =2.01'''
    def iati_organisations__iati_organisation__document_link__title__narrative(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        code:en

    tag:language
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 65 iati_version =2.01'''
    def iati_organisations__iati_organisation__document_link__language(self,element):
        model = self.get_func_parent_model()
        #store element
        return element


    '''atributes:
        code:AF

    tag:recipient-country
    found in https://raw.githubusercontent.com/IATI/IATI-Extra-Documentation/version-2.01/en/organisation-standard/organisation-standard-example-annotated.xml at line 66 iati_version =2.01'''
    def iati_organisations__iati_organisation__document_link__recipient_country(self,element):
        model = self.get_func_parent_model()
        #store element
        return element