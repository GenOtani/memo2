from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# メモを保存するリスト（本当はDBを使うべきだけど最初はこれでOK）
memos = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        memo = request.form.get("memo")
        if memo:
            memos.append(memo)
        return redirect("/")
    return render_template("index.html", memos=memos)

if __name__ == "__main__":
    app.run(debug=True)
