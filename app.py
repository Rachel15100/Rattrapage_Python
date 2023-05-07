from dash import Dash, dcc, html, Output, Input, State, callback
import random

app = Dash(__name__)
server=app.server

question = ["Quelle commande permet de créer une nouvelle branche ?", 
            "Quel est l'opérateur de comparaison qui permet de vérifier si deux valeurs sont égales ?", 
            "Quelle commande linux permet de lister le contenu d'un répertoire ?", 
            "Quelle commande permet de changer de répertoire ?", 
            "Quelle commande permet de supprimer un répertoire et son contenu ?",
            "Quelle commande permet de rechercher une chaine de caractère dans un fichier ?", 
            "Quelle commande permet de changer de branche ?", 
            "Quelle commande permet de créer une copie locale d'une reponsitory git ?", 
            "Quelle commande linux permet de planifier l'exécution de commandes ou de scripts à intervalles réguliers  ?", 
            "Quelle package python permet la création d'un tableau de bord ?", 
            "Quelle commande permet d'afficher le contenu d'un fichier ?", 
            "Quel outils permet de transférer des données en ligne vers un terminal ?", 
            'cat fichier.txt | grep -oP "linux\s\w+" : renvoie le mot linux seul. Vrai ou Faux ?', 
            "Qu'est ce que Linux ? (2 mots)", 
            "Quelle est l'extention pour un script shell ? (attention au '.')", 
            "La commande : */5 * * * * /chemin/vers/le/script.sh, exécute le script.sh toutes les 5 minutes. Vrai ou Faux ?", 
            "Quelle est la commande pour créer un nouveau repository en linux ?", 
            "Quel est le symbole d'un chevron en linux ?", 
            "Quelle est la commande pour saisir du texte dans un fichier texte linux ? (4 lettres)", 
            "Quelle est la commande pour changer les permissions d'un fichier ?", 
            "Quelle sont les lettres permettant à un utilisateur de lire, écrire et exécuter un fichier ?", 
            "Quelle commande permet d'exécuter une command en tant que super utilisateur ?"]

correct_answer = ["git branch", "==", "ls", "cd", "rm -rv",
                  "grep", "git checkout", "git clone", "cron", "dash",
                  "cat", "curl", "Faux", "Système d'exploitation", ".sh", 
                  "Vrai", "mkdir", ">", "echo", "chmod", 
                  "rwx", "sudo"]

def serve_layout():
    indexQuestion=random.randint(0, len(question)-1)
    choixQuestion=question[indexQuestion]


    layout = html.Div([
        html.H1("Rattrapage Git, Python, Linux"),
        html.H2("Question : " + choixQuestion, id="question"),
        dcc.Input(id='user-input', type='text', value='', placeholder='Entrez votre réponse ici...'),
        html.Button('Vérifier la réponse', id='submit-button', n_clicks=0),
        html.Div(id='output')
    ])
    return layout

app.layout=serve_layout
app.title = "Quiz RG"


@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='submit-button', component_property='n_clicks')],
    [State(component_id='user-input', component_property='value'),
     State(component_id='question', component_property='children')]
)

def check_answer(n_clicks, user_answer, question_text):
    if n_clicks > 0:
        indexQuestion = question.index(question_text[len("Question : "):])
        if user_answer.lower() == correct_answer[indexQuestion].lower():
            return html.P("Bonne réponse !")
        else:
            return html.P(f"Mauvaise réponse. La réponse était {correct_answer[indexQuestion]}")
    else:
        return ""

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8066)
