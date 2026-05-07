import shodan
from st2common.runners.base_action import Action


class ShodanBaseAction(Action):
    def __init__(self, config):
        super().__init__(config)
        api_key = self.config.get("shodan_api_key")
        if not api_key:
            raise ValueError(
                "shodan_api_key is not configured. "
                "Please set it via: st2 pack config shodan"
            )
        timeout = self.config.get("request_timeout", 30)
        self.client = shodan.Shodan(api_key)
        self.client.timeout = timeout