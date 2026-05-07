"""Return all available Shodan data for a given IP address."""

from lib.base import ShodanBaseAction


class HostInfoAction(ShodanBaseAction):
    def run(self, ip, history=False, minify=False):
        try:
            result = self.client.host(ip, history=history, minify=minify)
            return True, result
        except Exception as e:
            return False, str(e)
