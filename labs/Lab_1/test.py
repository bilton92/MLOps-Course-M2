import requests
import json

# Define the endpoint URL
url = 'http://localhost:5001/predict'

names = [
    "mean radius","mean texture","mean perimeter","mean area","mean smoothness","mean compactness",
    "mean concavity","mean concave points","mean symmetry","mean fractal dimension",
    "radius error","texture error","perimeter error","area error","smoothness error",
    "compactness error","concavity error","concave points error","symmetry error","fractal dimension error",
    "worst radius","worst texture","worst perimeter","worst area","worst smoothness","worst compactness",
    "worst concavity","worst concave points","worst symmetry","worst fractal dimension"
]

vals = [17.99,10.38,122.8,1001.0,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,
        1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,
        0.006193,25.38,17.33,184.6,2019.0,0.1622,0.6656,0.7119,0.2654,0.4601,
        0.1189]

# CrÃ©ation du dictionnaire avec toutes les features
payload = dict(zip(names, vals))

# Ajout de la nouvelle feature
payload["Combined_radius_texture"] = payload["mean radius"] * payload["mean texture"]

# Envoi au serveur
response = requests.post(url, headers={"Content-Type":"application/json"}, data=json.dumps(payload))

print("Status:", response.status_code)
print("Response:", response.text)