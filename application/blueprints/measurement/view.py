from sanic import Blueprint
from sanic.response import text


bp = Blueprint("Measurement", url_prefix="/measurement")


@bp.route("/")
async def index(request):
    db = request.app.ctx.mongo_db
    document = {"weight": 78.1}
    result = await db.measurement.insert_one(document)
    return text(f"result {result.inserted_id}")
