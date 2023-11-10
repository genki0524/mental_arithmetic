from calapp import app
from flask import render_template,request
import sys
sys.path.append('../')
from make_question import Question

question = Question()

@app.route("/")
def index():
    return render_template("calapp/start.html")

@app.route("/question/easy",methods=["GET"])
def question_easy():
    question.make_question(1)
    question_correct = question.getCorrect()
    return render_template("calapp/question.html",question_nums = question.nums,question_correct=question_correct)

@app.route("/question/normal",methods=["GET"])
def question_normal():
    question.make_question(2)
    question_correct = question.getCorrect()
    return render_template("calapp/question.html",question_nums = question.nums,question_correct=question_correct)

@app.route("/question/hard",methods=["GET"])
def question_hard():
    question.make_question(3)
    question_correct = question.getCorrect()
    return render_template("calapp/question.html",question_nums = question.nums,question_correct=question_correct)

@app.route("/result",methods=["GET","POST"])
def result():
    correct = question.getCorrect()
    if request.method == "GET":
        input_answer = ""
        return render_template("calapp/result.html",correct=correct,input_answer=input_answer)

    if request.method == "POST":
        input_answer = request.form.get("input-answer")
        return render_template("calapp/result.html",correct=correct,input_answer=input_answer)