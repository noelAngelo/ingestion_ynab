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
        "resource_defaults": {"primary_key": "id", "write_disposition": "merge"},
        "resources": [
            {
                "name": "transactions",
                "endpoint": {
                    "path": "/transactions",
                    "method": "GET",
                    "params": {
                        "sort": "createdAt",
                        "direction": "desc",
                        "since": {
                            "type": "incremental",
                            "cursor_path": "attributes.createdAt",
                            "initial_value": "2017-01-01T00:00:00Z",
                        },
                    },
                    "data_selector": "data",  # selects the list of records
                },
            }
        ],
    }

    yield from rest_api_resources(config)
