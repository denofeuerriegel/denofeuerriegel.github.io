import requests

def get_random_meal():
    # Die kostenlose API von TheMealDB für ein zufälliges Gericht
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        meal = data['meals'][0] # Das erste (und einzige) Gericht aus der Antwort nehmen
        
        name = meal['strMeal']
        category = meal['strCategory']
        area = meal['strArea']
        link = meal['strSource'] or meal['strYoutube'] or "Kein Link verfügbar"
        
        print(f"🍽️  Gericht: {name} ({area}, {category})")
        print(f"🔗 Rezept/Video: {link}")
    else:
        print("Ups, da hat die API nicht geantwortet.")

# Dein Mini-Planer
print("Willkommen zu deinem random Speiseplan!\n")

for i in range(1, 4):
    print(f"--- Tag {i} ---")
    get_random_meal()
    print("") # Leerzeile für die Optik
    