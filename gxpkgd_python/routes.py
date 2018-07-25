from flask import jsonify, request, current_app, Blueprint
from pony.orm import db_session, select, commit
from pony.orm.serialization import to_json

from gxpkgd_python.models import Package, Fork
from gxpkgd_python.handlers import github_handler


packagesBP = Blueprint('packages', __name__)


@packagesBP.route('/packages')
def packages():
    try:
        with db_session:
            packages = [i.to_dict() for i in select(p for p in Package)[:]]
            for p in packages:
                forks = [i.to_dict() for i in select(f for f in Fork if f.package.repo == p['repo'])[:]]
                p['forks'] = forks
            return jsonify({"data": packages})
    except Exception as e:
        return jsonify({"error": str(e)})


@packagesBP.route('/package/<path:repo>', methods=['GET', 'POST'])
@db_session
def package(repo):
    if request.method == 'GET':
        try:
            package = select(p for p in Package if p.repo == repo)[:][0].to_dict()
            forks = [i.to_dict() for i in select(f for f in Fork if f.package.repo == repo)[:]]
            package['forks'] = forks
            return jsonify({"data": package})
        except Exception as e:
            return jsonify({"error": str(e)})
    elif request.method == 'POST':
        try:
            package, forks = github_handler(repo)
            p = Package(**package)
            for f in forks:
                Fork(login=f['login'], name=f['name'], html_url=f['html_url'], package=p)
            commit()
            msg = 'Package {}/{} added.'.format(package['author'], package['name'])
            return jsonify({"data": msg})
        except Exception as e:
            return jsonify({"error": str(e)})


@packagesBP.route('/search/<string:query>')
def search(query):
    try:
        results = search_package(query)
        return jsonify({"data": results})
    except Exception as e:
        return jsonify({"error": str(e)})


