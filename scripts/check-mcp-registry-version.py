"""Check immutable registry metadata before publishing from cofounder-plugin."""

import json
import os
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import urlopen


def main() -> None:
    server = json.loads(Path("server.json").read_text())
    name = quote(server["name"], safe="")
    version = quote(server["version"], safe="")
    url = f"https://registry.modelcontextprotocol.io/v0.1/servers/{name}/versions/{version}"
    try:
        with urlopen(url, timeout=30) as response:
            published = json.load(response)["server"]
    except HTTPError as error:
        if error.code != 404:
            raise
        publish = True
    else:
        published.pop("_meta", None)
        if published != server:
            raise SystemExit(
                "This version already has different metadata; bump the plugin version."
            )
        print("Identical version already published.")
        publish = False
    with open(os.environ["GITHUB_OUTPUT"], "a") as output:
        output.write(f"publish={str(publish).lower()}\n")


if __name__ == "__main__":
    main()
