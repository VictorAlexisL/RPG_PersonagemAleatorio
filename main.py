from flask import Flask, render_template, request, redirect, url_for
from random import randint
app = Flask(__name__)

character_list = []

class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.level = 0
        self.exp = 0
        self.character_class = character_class
        if character_class == 'warrior':
          self.classe = "Guerreiro"
        elif character_class == 'thief':
            self.classe = "Ladino"
        else:
            self.classe = "Mago"
        self.strength = 10
        self.intelligence = 10
        self.dexterity = 10
        self.generate_stats()
        character_list.append((self.name, self.classe, self.strength, self.intelligence, self.dexterity))

    def get_exp(self):
        self.exp += randint(1,100)
        if self.exp >= 100:
            self.level_up()        
        return self.exp
    
    def generate_stats(self):
        if self.character_class == "warrior":
            self.strength += randint(2,5)
            self.intelligence += randint(0,1)
            self.dexterity += randint(0,3)
        elif self.character_class == "wizard":
            self.strength += randint(0,1)
            self.intelligence += randint(2,5)
            self.dexterity += randint(0,3)
        else:
            self.strength += randint(0,1)
            self.intelligence += randint(0,3)
            self.dexterity += randint(2,5)          
        print(f"{self.name}, Class: {self.character_class}, Strength: {self.strength}; Intelligence: {self.intelligence}; Dexterity: {self.dexterity}")
        return f"{self.name}, Class: {self.character_class}, Strength: {self.strength}; Intelligence: {self.intelligence}; Dexterity: {self.dexterity}"

    def level_up(self):
        print("Level Up!")
        self.level += 1
        self.generate_stats()
        print(f"Current level: {self.level}")
        return self.level
    
    def debug(self):
        while self.level < 5:
            Character.get_exp(self)
        print("Done testing.")
        return True

@app.route("/", methods=['POST', 'GET'])
def hello():
  number_of_characters = len(character_list)    
  if request.method == 'POST':
    characterName = request.form['characterName']
    characterClass = request.form['characterClass']
    character = Character(characterName, characterClass)
    if characterName != "":
      number_of_characters = len(character_list)
      return render_template('newcharacter.html', characterName=characterName, characterClass=characterClass, strength=character.strength, dexterity=character.dexterity, intelligence=character.intelligence)
  return render_template('index.html', character_list=character_list, number_of_characters=number_of_characters)


if __name__ == "__main__":
    app.run(debug=True)
