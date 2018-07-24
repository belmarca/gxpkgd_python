from flask import jsonify, request, current_app, Blueprint
from pony.orm import db_session, select, commit
from pony.orm.serialization import to_json

from gxpkgd_python.models import Package
from gxpkgd_python.handlers import github_handler


packagesBP = Blueprint('packages', __name__)


@packagesBP.route('/packages')
def packages():
    try:
        with db_session:
            packages = select(p for p in Package)[:]
            result = [p.to_dict() for p in packages]
            return jsonify({"data": result})
    except Exception as e:
        return jsonify({"error": str(e)})


@packagesBP.route('/package/<path:repo>', methods=['GET', 'POST'])
@db_session
def package(repo):
    if request.method == 'GET':
        try:
            package = select(p for p in Package if p.repo == repo)[:][0].to_dict()
            return jsonify({"data": package})
        except Exception as e:
            return jsonify({"error": str(e)})
    elif request.method == 'POST':
        try:
            package = github_handler(repo)
            Package(**package)
            # gotta call !%@#^!$ command for the exception to be properly thrown
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


