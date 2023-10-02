from flask import Flask, render_template, request, redirect, url_for
from random import randint
 
app = Flask(__name__)

character_list = []

class Character:
  def __init__(self, name):
    self.name = name
    self.level = 0
    self.exp = 0
    self.character_class = "Nenhuma"
    self.set_base_stats()
    self.add_to_character_list()

  def add_to_character_list(self):
    character_list.append((self.name, self.character_class))
    self.index = character_list.index((self.name, self.character_class));
    character_list[(self.index)] = ((self.index, self.name, self.character_class, self.strength, self.intelligence, self.dexterity))
    print(self.index)

  def set_base_stats(self):
    self.strength = 10
    self.intelligence = 10
    self.dexterity = 10

  def get_exp(self):
    self.exp += randint(1,100)
    if self.exp >= 100:
      self.level_up()     
    
  def level_up(self):
    self.level += 1
    self.strength += randint(1,2)
    self.intelligence += randint(1,2)
    self.dexterity += randint(1,2)
    print (f"Level Up! Current level: {self.level}")
    
  def debug(self):
    while self.level < 5:
      self.get_exp()
    print(self.strength)
    print(self.intelligence)
    print(self.dexterity)
    print("Done testing.")
    print(f"Level: {self.level}, name: {self.name}, index: {self.index}")    

class Wizard(Character):
  def __init__(self, name):
    super().__init__(name)
  
  def set_base_stats(self):
    self.character_class = "Mago"
    self.strength = 8 + randint(0,2)
    self.intelligence = 12 + randint(0, 4)
    self.dexterity = 10 + randint(0,2)

class Warrior(Character):
  def __init__(self, name):
    super().__init__(name)
  
  def set_base_stats(self):
    self.character_class = "Guerreiro"
    self.strength = 12 + randint(0, 4)
    self.intelligence = 8 + randint(0,2)
    self.dexterity = 10 + randint(0,2)

class Rogue(Character):
  def __init__(self, name):
    super().__init__(name)
  
  def set_base_stats(self):
    self.character_class = "Ladino"
    self.strength = 8 + randint(0,2)
    self.intelligence = 10 + randint(0,2)
    self.dexterity = 12 + randint(0, 4)

@app.route("/", methods=['POST', 'GET'])
def hello():
  number_of_characters = len(character_list)    
  if request.method == 'POST':
    characterName = request.form['characterName']
    characterClass = request.form['characterClass']
    if characterClass == "warrior":
      character = Warrior(characterName)
    elif characterClass == "wizard":
      character = Wizard(characterName)
    elif characterClass == "rogue":
      character = Rogue(characterName)
    else:
      character = Character(characterName, characterClass)
    if characterName != "":
      number_of_characters = len(character_list)
      return render_template('newcharacter.html', characterName=characterName, characterClass=characterClass, strength=character.strength, dexterity=character.dexterity, intelligence=character.intelligence)
  return render_template('index.html', character_list=character_list, number_of_characters=number_of_characters)


if __name__ == "__main__":
    app.run(debug=True)
