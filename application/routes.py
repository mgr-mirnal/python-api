from application import app, db
from flask import request,jsonify
from application.models import FriendsCharacter

def format_character(character):
    return{
        'id' : character.id,
        'name' : character.name,
        'age': character.age,
        'catch_phrase': character.catch_phrase

    }

@app.route("/")
def hello_wordl():
    return '<p> Hello World!!! </p>'

@app.route('/characters', methods=['Post'])
def create_character():
    data = request.json
    character = FriendsCharacter(data['name'], data['age'], data['catch_phrase'])
    db.session.add(character)
    db.session.commit()
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

@app.route('/characters', methods=['GET'])
def get_characters():
    charcters = FriendsCharacter.query.all()
    characters_list =[]
    for character in charcters:
        characters_list.append(format_character(character))
    return {"character": characters_list}

@app.route('/characters/<id>', methods=["GET"])
def get_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase = character.catch_phrase )

@app.route('/characters/<id>', methods=['DELETE'])
def delete_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return "character deleted"

@app.route('/characters/<id>', methods=['PATCH'])
def update_character(id):
    character = FriendsCharacter.query.filter_by(id=id)
    data = request.json
    character.update(dict(name=data['name'], age=data["age"],catch_phrase=data["catch_phrase"]))
    db.session.commit()
    updatedCharacter = character.first()
    return jsonify(id=updatedCharacter.id, name=updatedCharacter.name, age=updatedCharacter.age, catch_phrase=updatedCharacter.catch_phrase) 
