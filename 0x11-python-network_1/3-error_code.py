#!/usr/bin/python3
"""a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import urllib.error as error
import urllib.request as req
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    request = req.Request(url)
    try:
        with req.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
