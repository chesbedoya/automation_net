from flask import Blueprint

mod_netsuite = Blueprint('mod_netsuite_selenium', __name__, url_prefix='/automationnet')


@mod_netsuite.route('/fandino')
def bebesukis():
    return 'Hola somos las bebesukis'