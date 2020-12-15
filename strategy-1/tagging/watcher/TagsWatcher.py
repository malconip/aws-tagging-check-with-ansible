from cfnlint.rules import CloudFormationLintRule
from cfnlint.rules import RuleMatch


class TagsRequired(CloudFormationLintRule):
    id = 'E9000'
    shortdesc = 'Tags are properly set'
    description = 'Check all Tag rules for WebServerInstaces'

    def match(self, cfn):
        matches = []
        approved_contacts = ['malcon', 'albuquerque']
        valid_services = ['cart', 'search']
        web_servers = [x for x in cfn.search_deep_keys('WebServerInstance') if x[0] == 'Resources']
        
        for web_server in web_servers:
            tags = web_server[-1]['Properties']['Tags']

            if not tags:
                message = "All resources must have at least one tag"
                matches.append(RuleMatch(web_server, message.format()))

            if not next((x for x in tags if x.get('Key') == 'env'), None):
                message = "All resources must have an 'env' tag"
                matches.append(RuleMatch(web_server, message.format()))

            for tag in tags:
                if tag.get('Key') == 'contact' and tag.get('Value') not in approved_contacts:
                    message = "The contact must be an approved contact"
                    matches.append(RuleMatch(web_server, message.format()))

                if tag.get('Key') == 'service' and tag.get('Value') not in valid_services:
                    message = "The service must be a valid service"
                    matches.append(RuleMatch(web_server, message.format()))

        return matches