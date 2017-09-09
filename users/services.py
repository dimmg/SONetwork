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
