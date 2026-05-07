# Shodan StackStorm Pack

StackStorm integration pack for [Shodan](https://www.shodan.io/) — the search engine for Internet-connected devices.

## Requirements

- A Shodan API key — get one at [account.shodan.io](https://account.shodan.io/)

## Installation

```shell
st2 pack install shodan
```

## Configuration

```shell
st2 pack config shodan
```

Or create the config manually:

```yaml
# /opt/stackstorm/configs/shodan.yaml
shodan_api_key: "YOUR_API_KEY_HERE"
request_timeout: 30
```

Then reload:

```shell
st2ctl reload --register-configs
```

## Actions

| Action | Description |
|--------|-------------|
| `shodan.host_info` | Returns all Shodan data for a host — ports, banners, hostnames, geolocation, org, CVEs |
| `shodan.host_ports` | Returns open ports only for a host (faster than `host_info`) |
| `shodan.search` | Search Shodan using filter syntax |
| `shodan.dns_resolve` | Resolve one or more hostnames to IP addresses |
| `shodan.dns_reverse` | Reverse DNS lookup for one or more IP addresses |

## Usage

```shell
# Full host lookup
st2 run shodan.host_info ip=8.8.8.8

# Open ports only
st2 run shodan.host_ports ip=8.8.8.8

# Search
st2 run shodan.search query="product:redis country:VN"
st2 run shodan.search query="port:22 has:vuln" page=2

# DNS
st2 run shodan.dns_resolve hostnames='["google.com", "cloudflare.com"]'
st2 run shodan.dns_reverse ips='["8.8.8.8", "1.1.1.1"]'
```

## Shodan Query Filter Reference

| Filter | Example |
|--------|---------|
| `port:` | `port:22` |
| `country:` | `country:VN` |
| `org:` | `org:"Amazon"` |
| `product:` | `product:nginx` |
| `os:` | `os:windows` |
| `asn:` | `asn:AS13335` |
| `vuln:` | `vuln:CVE-2021-44228` |
| `has:vuln` | `has:vuln` |

Full filter reference: https://www.shodan.io/search/filters

## License

Apache 2.0