from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple symptom-disease mapping (you can replace with ML later)
disease_data = {
    "fever,cough": "Flu",
    "headache,nausea": "Migraine",
    "chest pain,shortness of breath": "Heart Issue"
}

# Mock doctors database
doctors = {
    "Flu": ["Dr. Ravi - General Physician", "Dr. Meena - Internal Medicine"],
    "Migraine": ["Dr. Kumar - Neurologist"],
    "Heart Issue": ["Dr. Arjun - Cardiologist"]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    symptoms = request.json.get("symptoms").lower()
    
    disease = "Unknown"
    for key in disease_data:
        if key in symptoms:
            disease = disease_data[key]
            break

    doctor_list = doctors.get(disease, ["No doctors found"])

    return jsonify({
        "disease": disease,
        "doctors": doctor_list
    })

if __name__ == "__main__":
    app.run(debug=True)