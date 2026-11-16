from flask import Flask, render_template, request

app = Flask(__name__)

meal_data = {
    "2026-11-02": {
        "아침": "쌀밥, 계란국, 김치",
        "점심": "카레라이스, 돈가스, 샐러드, 깍두기",
        "저녁": "현미밥, 된장찌개, 불고기, 김치"
    },
    "2026-11-03": {
        "아침": "토스트, 우유, 과일",
        "점심": "비빔밥, 미역국, 김치",
        "저녁": "쌀밥, 닭볶음탕, 나물, 깍두기"
    }
}

@app.route("/", methods=["GET", "POST"])
def home():
    date = ""
    meals = None
    message = ""

    if request.method == "POST":
        date = request.form.get("date", "")

        if date in meal_data:
            meals = meal_data[date]
        else:
            message = "해당 날짜의 급식 정보가 없습니다."

    return render_template(
        "index.html",
        date=date,
        meals=meals,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)