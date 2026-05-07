from lib.base import ShodanBaseAction

class HostPortsAction(ShodanBaseAction):
    def run(self, ip):
        try:
            result = self.client.host(ip, minify=True)
            ports = result.get("ports", [])
            return True, {"ip": ip, "ports": sorted(ports)}
        except Exception as e:
            return False, str(e)