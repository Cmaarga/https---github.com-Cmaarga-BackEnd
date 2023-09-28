from flask import Blueprint
from ..controllers.canales_controller import CanalesController

bp_canales = Blueprint("canales", __name__)

bp_canales.route("/", methods=["GET"])(CanalesController.get)
bp_canales.route("/", methods=["POST"])(CanalesController.create)
