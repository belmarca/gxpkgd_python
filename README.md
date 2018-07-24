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
(gxs) ➜  http post localhost:5000/package/https://github.com/belmarca/gerbil-simsub
HTTP/1.0 200 OK
Content-Length: 45
Content-Type: application/json
Date: Mon, 23 Jul 2018 22:03:53 GMT
Server: Werkzeug/0.14.1 Python/3.5.3

{
    "data": "Package belmarca/gerbil-simsub added."
}

(gxs) ➜  http post localhost:5000/package/https://github.com/vyzo/gerbil-simsub
HTTP/1.0 200 OK
Content-Length: 45
Content-Type: application/json
Date: Mon, 23 Jul 2018 22:04:03 GMT
Server: Werkzeug/0.14.1 Python/3.5.3

{
    "data": "Package vyzo/gerbil-simsub added."
}

(gxs) ➜  http get localhost:5000/package/https://github.com/belmarca/gerbil-simsub 
HTTP/1.0 200 OK
Content-Length: 305
Content-Type: application/json
Date: Mon, 23 Jul 2018 22:04:10 GMT
Server: Werkzeug/0.14.1 Python/3.5.3

{
    "data": {
        "author": "belmarca", 
        "description": "A PubSub Protocol and its Simulator", 
        "id": 1, 
        "last_update": "2018-07-23 18:03:53.148801", 
        "license": "MIT", 
        "name": "gerbil-simsub", 
        "repo": "https://github.com/belmarca/gerbil-simsub", 
        "runtime": "gerbil"
    }
}

(gxs) ➜  http get localhost:5000/package/https://github.com/vyzo/gerbil-simsub
HTTP/1.0 200 OK
Content-Length: 304
Content-Type: application/json
Date: Mon, 23 Jul 2018 22:04:16 GMT
Server: Werkzeug/0.14.1 Python/3.5.3

{
    "data": {
        "author": "vyzo", 
        "description": "Package has no description.", 
        "id": 2, 
        "last_update": "2018-07-23 18:04:03.010399", 
        "license": "MIT", 
        "name": "gerbil-simsub", 
        "repo": "https://github.com/vyzo/gerbil-simsub", 
        "runtime": "No runtime specified."
    }
}

(gxs) ➜  http get localhost:5000/packages                               
HTTP/1.0 200 OK
Content-Length: 647
Content-Type: application/json
Date: Mon, 23 Jul 2018 22:04:21 GMT
Server: Werkzeug/0.14.1 Python/3.5.3

{
    "data": [
        {
            "author": "belmarca", 
            "description": "A PubSub Protocol and its Simulator", 
            "id": 1, 
            "last_update": "2018-07-23 18:03:53.148801", 
            "license": "MIT", 
            "name": "gerbil-simsub", 
            "repo": "https://github.com/belmarca/gerbil-simsub", 
            "runtime": "gerbil"
        }, 
        {
            "author": "vyzo", 
            "description": "Package has no description.", 
            "id": 2, 
            "last_update": "2018-07-23 18:04:03.010399", 
            "license": "MIT", 
            "name": "gerbil-simsub", 
            "repo": "https://github.com/vyzo/gerbil-simsub", 
            "runtime": "No runtime specified."
        }
    ]
}
```

## Todo

Tests.
