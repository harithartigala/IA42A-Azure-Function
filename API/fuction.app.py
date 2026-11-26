import json
import random

import azure.functions as func

# 関数アプリを作る（誰でも呼び出せる設定）
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

RESULTS = ["大吉", "中吉", "小吉", "吉", "凶"]


# /api/fortune にアクセスされたときに動く関数
@app.route(route="fortune", methods=["GET"])
def fortune(req: func.HttpRequest) -> func.HttpResponse:
    # URLの ?name=〇〇 の値を受け取る
    name = req.params.get("name", "").strip()

    if not name:
        body = {"error": "名前を入力してください"}
        return func.HttpResponse(
            json.dumps(body, ensure_ascii=False),
            status_code=400,
            mimetype="application/json",
        )

    # 運勢をランダムに決める
    body = {
        "name": name,
        "result": random.choice(RESULTS),
    }
    return func.HttpResponse(
        json.dumps(body, ensure_ascii=False),
        mimetype="application/json",
    )