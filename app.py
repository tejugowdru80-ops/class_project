disease_data = {
    "diabetes": {
        "description": "A condition where blood sugar levels are high.",
        "symptoms": "Increased thirst, frequent urination, fatigue",
        "treatment": "Insulin therapy, diet control"
    },
    "malaria": {
        "description": "A mosquito-borne infectious disease.",
        "symptoms": "Fever, chills, sweating",
        "treatment": "Antimalarial drugs"
    },
    "covid": {
        "description": "A viral disease caused by coronavirus.",
        "symptoms": "Fever, cough, breathing difficulty",
        "treatment": "Supportive care, oxygen therapy"
    }
}

from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("project.html")

@app.route("/search", methods=["POST"])
def search():
    disease_name = request.form["disease"].lower()

    if disease_name in disease_data:
        result = disease_data[disease_name]
        return render_template("result_dis.html", disease=disease_name, info=result)
    else:
        return render_template('result_dis.html', disease=disease_name, info=None)

if __name__ == '__main__':
    app.run(debug=True)