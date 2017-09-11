import logging

from requests.exceptions import HTTPError

from clients.clearbit import clearbit
from clients.hunter import hunter

logging.getLogger().setLevel(logging.INFO)


class HunterService:
    @staticmethod
    def is_valid_email(email):
        """
        Checks whether an email is supposed to be deliverable.
        :param email: email to be checked
        :return: True if email is deliverable, False - otherwise
        """
        subdomain = HunterService._get_domain_for_email(email)
        try:
            result = hunter.domain_search(subdomain)
        except HTTPError as e:
            logging.info('Skipping hunter.io services. REASON: %s', str(e))

            return True

        return result['webmail'] or bool(result['emails'])

    @staticmethod
    def _get_domain_for_email(email):
        """
        Extracts the domain from the given email.
        :param email: email, domain to be extracted from
        :return: email domain
        """
        return email.split('@')[1]


class ClearBitService:
    @staticmethod
    def get_details_for_email(email):
        """
        Returns meta information about a given email according
        to the clearbit.com databases.
        """
        try:
            result = dict(clearbit.Enrichment.find(email=email, stream=True))
        except HTTPError as e:
            logging.info('Skipping clearbit.com services. REASON %s', str(e))

            return {}

        return {
            'first_name': result.get('person', {}).get('name', {}).get('givenName') or '',
            'last_name': result.get('person', {}).get('name', {}).get('familyName') or '',
            'gender': result.get('person', {}).get('gender') or '',
            'bio': result.get('person', {}).get('bio') or ''
        }
