from engine import engine

character = {
    'name': ['place-holder'],
    'health':   [1,2,3,4,5],
    'strength': [1,2,3,4,5],
    'endurance': [1,2,3,4,5],
    'dexterity': [1,2,3,4,5],
    'fav-color': ['red','blue'],
}

def generate():
    character_init('character1', 'male')
    character_init('character2', 'female')

def character_init(name, gender):
    engine.create(name)
    character_output=engine.generate(character, gender)
    engine.update(character_output, name)
