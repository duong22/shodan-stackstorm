from lib.base import ShodanBaseAction

MATCH_FIELDS = (
    "ip_str", "port", "transport", "hostnames", "domains",
    "org", "isp", "product", "version", "os", "cpe", "cpe23",
    "asn", "vulns", "tags", "timestamp", "location",
)

class SearchAction(ShodanBaseAction):
    def run(self, query, facets=None, page=1, minify=True):
        try:
            kwargs = {"page": page, "minify": minify}
            if facets:
                kwargs["facets"] = facets

            result = self.client.search(query, **kwargs)
            matches = [self._trim(m) for m in result.get("matches", [])]

            return True, {
                "total": result.get("total", 0),
                "page": page,
                "count": len(matches),
                "matches": matches,
                "facets": result.get("facets", {}),
            }
        except Exception as e:
            return False, str(e)

    def _trim(self, match):
        trimmed = {k: match[k] for k in MATCH_FIELDS if k in match}

        loc = trimmed.pop("location", {}) or {}
        trimmed["country_code"] = loc.get("country_code", "")
        trimmed["country_name"] = loc.get("country_name", "")
        trimmed["city"] = loc.get("city", "")

        vulns = trimmed.get("vulns")
        if isinstance(vulns, dict):
            trimmed["vulns"] = {
                cve: data.get("summary", "") for cve, data in vulns.items()
            }

        return trimmed