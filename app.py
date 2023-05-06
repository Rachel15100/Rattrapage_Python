from dash import Dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import random

# Liste des questions et réponses possibles
questions = {
    "Git": "Quelle commande permet de créer une nouvelle branche ?",
    "Python": "Quel est l'opérateur de comparaison qui permet de vérifier si deux valeurs sont égales ?",
    "Linux": "Quelle commande permet d'afficher le contenu d'un fichier ?"
}


reponses = {
    "Git": "git branch",
    "Python": "==",
    "Linux": "cat"
}

# Fonction pour choisir une question aléatoire
def choisir_question():
    return random.choice(questions)

# Création de l'application Dash
app = Dash(__name__)

# Layout de la page
app.layout = html.Div([
    html.H1("Questionnaire"),
    html.H2(id="question"),
    dcc.Input(id="reponse-input", type="text", value=""),
    html.Button("Vérifier la réponse", n_clicks=0, id="submit-button"),
    html.H3(id="reponse")
])

# Fonction pour choisir une question aléatoire
def choisir_question():
    categorie = random.choice(list(questions.keys()))
    question = questions[categorie]
    reponse = reponses[categorie]
    return question, reponse


# Callback pour afficher une question aléatoire
@app.callback(
    Output("question", "children"),
    Input("submit-button", "n_clicks"))

def afficher_question(n_clicks):
    question = choisir_question()
    return question[0]

# Callback pour vérifier la réponse
@app.callback(
    Output("reponse", "children"),
    [Input("submit-button", "n_clicks")],
    [State("reponse-input", "value")])


def verifier_reponse(n_clicks, reponse_utilisateur):
    reponse_attendue = choisir_question()[1]
    if reponse_utilisateur == reponse_attendue:
        return "Bonne réponse !"
    else:
        return "Mauvaise réponse, la réponse était ", reponse_attendue


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8043)
