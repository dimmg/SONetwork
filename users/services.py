from clients.clearbit import clearbit
from clients.hunter import hunter


class HunterService():
    @staticmethod
    def is_valid_email(email):
        subdomain = HunterService._get_subdomain_for_email(email)
        result = hunter.domain_search(subdomain)

        return result['data']['webmail'] or bool(result['data']['email'])

    @staticmethod
    def _get_subdomain_for_email(email):
        return email.split('@')[1]


class ClearBitService():
    @staticmethod
    def get_details_for_email(email):
        result = dict(clearbit.Enrichment.find(email=email, stream=True))

        return {
            'first_name': result.get('person', {}).get('name', {}).get('givenName') or '',
            'last_name': result.get('person', {}).get('name', {}).get('familyName') or '',
            'gender': result.get('person', {}).get('gender') or '',
            'bio': result.get('person', {}).get('bio') or ''
        }
