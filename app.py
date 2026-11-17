
# Flask 웹사이트 기능을 사용하기 위해 필요한 모듈을 가져온다.
from flask import Flask, render_template, request

# Flask 애플리케이션을 생성한다.
app = Flask(__name__)

# 날짜별 아침, 점심, 저녁 급식 정보를 저장한다.
# 현재는 실제 급식 정보가 아닌 테스트용 데이터이다.
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

# 홈페이지 주소로 접속했을 때 실행되는 함수이다.
# GET은 페이지 접속, POST는 급식 조회 요청을 처리한다.
@app.route("/", methods=["GET", "POST"])
def home():

    # 조회할 날짜, 급식 정보, 안내 메시지를 처음에는 비워 둔다.
    date = ""
    meals = None
    message = ""

    # 사용자가 급식 조회 버튼을 눌렀는지 확인한다.
    if request.method == "POST":

        # 날짜 입력창에서 사용자가 선택한 날짜를 가져온다.
        date = request.form.get("date", "")

        # 선택한 날짜가 급식 데이터에 있는지 확인한다.
        if date in meal_data:
            # 해당 날짜의 아침, 점심, 저녁 정보를 가져온다.
            meals = meal_data[date]
        else:
            # 해당 날짜의 급식 정보가 없을 때 안내 메시지를 표시한다.
            message = "해당 날짜의 급식 정보가 없습니다."

    # HTML 화면에 날짜, 급식 정보, 안내 메시지를 전달한다.
    return render_template(
        "index.html",
        date=date,
        meals=meals,
        message=message
    )

# 이 파일을 직접 실행했을 때 웹사이트 서버를 시작한다.
if __name__ == "__main__":
    app.run(debug=True)
