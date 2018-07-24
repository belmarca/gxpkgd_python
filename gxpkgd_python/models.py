from pony.orm import db_session, PrimaryKey, Required

from gxpkgd_python.extensions import db, pw


@db_session
def search_package(query):
    results = Package.search(query, add_wildcards=True, include_entity=True, use_dict=True)['results']
    return [r['entity'] for r in results]


@pw.register_model('author', 'name', 'description')
class Package(db.Entity):
    _table_ = 'Package'
    id = PrimaryKey(int, auto=True)
    author = Required(str)
    name = Required(str)
    description = Required(str)
    runtime = Required(str)
    license = Required(str)
    last_update = Required(str)
    repo = Required(str, unique=True)
