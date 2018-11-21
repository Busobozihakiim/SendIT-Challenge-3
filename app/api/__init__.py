from flask import Blueprint

apiv2 = Blueprint('apiv2', __name__)

from .v2 import user, admin