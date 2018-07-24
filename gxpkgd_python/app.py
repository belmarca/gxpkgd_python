def register_extensions(app):
    from gxpkgd_python.extensions import db, pw

    pw.init_app(app)

    db.bind('sqlite', 'db/' + app.config['PACKAGES_DB'], create_db=True)
    db.generate_mapping(create_tables=True)


def register_blueprints(app):
    from gxpkgd_python.routes import packagesBP
    app.register_blueprint(packagesBP)
