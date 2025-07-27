import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources


@dlt.source
def upbank(upbank_token: str = dlt.secrets.value):
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://api.up.com.au/api/v1",
            "auth": {
                "type": "bearer",
                "token": upbank_token,
            },
            "paginator": {
                "type": "json_link",
                "next_url_path": "links.next",
            },
        },
        "resources": [
            "transactions",
        ],
    }
    yield from rest_api_resources(config)
