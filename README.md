#gxpkgd
A Python 3.x implementation of `gxpkgd`.

## Description

`gxpkg` is [gerbil](https://github.com/vyzo/gerbil) scheme's package manager.
This repository is an implementation of `gxpkgd`, the package manager's metadata
server daemon.

It currently only handles the registration of github repositories.

## Installation

Create a new virtualenv and run `pip install -e .` followed by either `./run
dev`, `./run prod` or simply `flask run`.

Dev runs on `localhost:5000` while prod runs on `0.0.0.0:4000` which is meant to
be served behind an https reverse proxy.

## Example usage

```
➜  ~ http post localhost:5000/package/https://github.com/vyzo/gerbil-simsub
HTTP/1.0 200 OK
Content-Length: 50
Content-Type: application/json
Date: Wed, 25 Jul 2018 01:07:05 GMT
Server: Werkzeug/0.14.1 Python/3.5.3

{
    "data": "Package vyzo/gerbil-simsub added."
}

➜  ~ http get localhost:5000/package/https://github.com/vyzo/gerbil-simsub 
HTTP/1.0 200 OK
Content-Length: 701
Content-Type: application/json
Date: Wed, 25 Jul 2018 01:07:12 GMT
Server: Werkzeug/0.14.1 Python/3.5.3

{
    "data": {
        "author": "vyzo",
        "description": "Package has no description.",
        "forks": [
            {
                "html_url": "https://github.com/belmarca/gerbil-simsub",
                "id": 1,
                "login": "belmarca",
                "name": "gerbil-simsub",
                "package": 1
            },
            {
                "html_url": "https://github.com/jamesray1/gerbil-simsub",
                "id": 2,
                "login": "jamesray1",
                "name": "gerbil-simsub",
                "package": 1
            }
        ],
        "id": 1,
        "last_update": "2018-07-24 21:07:04.638772",
        "license": "MIT",
        "name": "gerbil-simsub",
        "repo": "https://github.com/vyzo/gerbil-simsub",
        "runtime": "No runtime specified."
    }
}

➜  ~ http post localhost:5000/package/https://github.com/belmarca/gerbil-simsub
HTTP/1.0 200 OK
Content-Length: 54
Content-Type: application/json
Date: Wed, 25 Jul 2018 01:07:22 GMT
Server: Werkzeug/0.14.1 Python/3.5.3

{
    "data": "Package belmarca/gerbil-simsub added."
}

➜  ~ http get localhost:5000/package/https://github.com/belmarca/gerbil-simsub
HTTP/1.0 200 OK
Content-Length: 323
Content-Type: application/json
Date: Wed, 25 Jul 2018 01:07:26 GMT
Server: Werkzeug/0.14.1 Python/3.5.3

{
    "data": {
        "author": "belmarca",
        "description": "A PubSub Protocol and its Simulator",
        "forks": [],
        "id": 2,
        "last_update": "2018-07-24 21:07:20.941187",
        "license": "MIT",
        "name": "gerbil-simsub",
        "repo": "https://github.com/belmarca/gerbil-simsub",
        "runtime": "gerbil"
    }
}

➜  ~ http get localhost:5000/packages
HTTP/1.0 200 OK
Content-Length: 1096
Content-Type: application/json
Date: Wed, 25 Jul 2018 01:07:31 GMT
Server: Werkzeug/0.14.1 Python/3.5.3

{
    "data": [
        {
            "author": "vyzo",
            "description": "Package has no description.",
            "forks": [
                {
                    "html_url": "https://github.com/belmarca/gerbil-simsub",
                    "id": 1,
                    "login": "belmarca",
                    "name": "gerbil-simsub",
                    "package": 1
                },
                {
                    "html_url": "https://github.com/jamesray1/gerbil-simsub",
                    "id": 2,
                    "login": "jamesray1",
                    "name": "gerbil-simsub",
                    "package": 1
                }
            ],
            "id": 1,
            "last_update": "2018-07-24 21:07:04.638772",
            "license": "MIT",
            "name": "gerbil-simsub",
            "repo": "https://github.com/vyzo/gerbil-simsub",
            "runtime": "No runtime specified."
        },
        {
            "author": "belmarca",
            "description": "A PubSub Protocol and its Simulator",
            "forks": [],
            "id": 2,
            "last_update": "2018-07-24 21:07:20.941187",
            "license": "MIT",
            "name": "gerbil-simsub",
            "repo": "https://github.com/belmarca/gerbil-simsub",
            "runtime": "gerbil"
        }
    ]
}
```

## Todo

Tests.
