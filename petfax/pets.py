from flask import ( Blueprint, render_template, request)
import json

bp = Blueprint(
    "pets",
    __name__,
    url_prefix="/pets"
)

# facts_bp = Blueprint(
#     "facts",
#     __name__,
#     url_prefix="/pets"
# )

@bp.route("/")
def pets():
    pets = json.load(open("pets.json"))
    print(pets)
    return render_template(
        'index.html',
        title="This is PetFax",
        pets=pets
    )

@bp.route("/adopt", methods=["POST"])
def adopt():
    print(request.form)
    return "I have adopted a pet!"

@bp.route("/show/<int:pet_id>")
def show_post(pet_id):
    pets = json.load(open("pets.json"))
    print(pets)
    for pet in pets:
        if pet['pet_id'] == pet_id:
            return render_template('pet.html', pet=pet)
    return "Pet Id not found"

@bp.route("/factform")
def fact_form():
    return render_template("facts.html")

