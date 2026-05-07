from lib.base import ShodanBaseAction

class DnsResolveAction(ShodanBaseAction):
    def run(self, hostnames):
        try:
            if isinstance(hostnames, list):
                hostnames_str = ",".join(hostnames)
            else:
                hostnames_str = hostnames
            args = {"hostnames": hostnames_str}
            result = self.client._request('/dns/resolve', args)
            return True, result
        except Exception as e:
            return False, str(e)