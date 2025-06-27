import requests
from datetime import datetime


GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 32
TOKEN= "#REDACTED"
bearer_headers = {
    "Authorization":f"Bearer{TOKEN}"
}



APP_ID = "#REDACTED"
API_KEY ="#REDACTED"




exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


sheet_endpoint = "https://api.sheety.co/910106f49778b65d4349fd25fb45e1ee/copy1OfMyWorkouts/workouts"


exercise_text = input("Tell me which exercises you did: ").strip()


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(exercise_endpoint, json=parameters, headers=headers)

if response.status_code != 200:
    print("❌ Nutritionix API call failed.")
    print(response.text)
    exit()

result = response.json()

if "exercises" not in result:
    print("❌ No exercises found.")
    exit()


now = datetime.now()
today_date = now.strftime("%d/%m/%Y")
now_time = now.strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
  
   
    sheet_response = requests.post(
        sheet_endpoint,
        #headers=bearer_headers,
        json=sheet_inputs,
        auth=(
            "#REDACTED",        
            "#REDACTED"    
     )
    )

    if sheet_response.status_code == 200:
        print(f"✅ Workout logged:\n{sheet_response.text}")
    else:
        print(f"❌ Failed to log workout:\n{sheet_response.text}")
#Ran 3 miles and biked for 20 minutes
#Ran 5k and cycle for 20 minutes
