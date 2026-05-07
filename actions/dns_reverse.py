from lib.base import ShodanBaseAction

class DnsReverseAction(ShodanBaseAction):
    def run(self, ips):
        try:
            if isinstance(ips, list):
                ips_str = ",".join(ips)
            else:
                ips_str = ips
            args = {"ips": ips_str}
            result = self.client._request('/dns/reverse', args)

            return True, result
        except Exception as e:
            return False, str(e)