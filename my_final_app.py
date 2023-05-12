from dash import Dash, dcc, html, Output, Input, State, callback
import random
import unidecode


app = Dash(__name__)
server=app.server

dico=dict()
dico={"[Git] Quelle commande permet de créer une nouvelle branche ?":"git branch",
      "[Python] Quel est l'opérateur de comparaison qui permet de vérifier si deux valeurs sont égales ?":"==",
      "[Linux] Quelle commande linux permet de lister le contenu d'un répertoire ?": "ls", 
      "[Linux] Quelle commande permet de changer de répertoire ?": "cd",
      "[Linux] Quelle commande permet de supprimer un répertoire et son contenu ?":"rm -rv", 
      "[Linux] Quelle commande permet de rechercher une chaine de caractère dans un fichier ?":"grep",
      "[Git] Quelle commande permet de changer de branche ?":"git checkout",
      "[Git] Quelle commande permet de créer une copie locale d'une repository git ?":"git clone",
      "[Linux] Quelle commande linux permet de planifier l'exécution de commandes ou de scripts à intervals réguliers  ?":"cron",
      "[Python] Quel package python permet la création d'un tableau de bord ?":"dash",
      "[Linux] Quelle commande permet d'afficher le contenu d'un fichier ?":"cat",
      "[Linux] Quel outils permet de transférer des données en ligne vers un terminal ?":"curl",
      '[Linux] cat fichier.txt | grep -oP "linux\s\w+" : renvoie le mot linux seul. Vrai ou Faux ?':"Faux",
      "Qu'est ce que Linux ? (2 mots)":"Système d'exploitation",
      "[Linux] Quelle est l'extention pour un script shell ? (attention au '.')":".sh",
      "[Linux] La commande : */5 * * * * /chemin/vers/le/script.sh, exécute le script.sh toutes les 5 minutes. Vrai ou Faux ?":"Vrai",
      "[Linux] Quelle est la commande pour créer un nouveau repository en linux ?":"mkdir",
      "[Linux] Quel est le symbole d'un chevron en linux ?":">",
      "[Linux] Quelle est la commande pour saisir du texte dans un fichier texte linux ? (4 lettres)":("echo", "vim"),
      "[Linux] Quelle est la commande pour changer les permissions d'un fichier ?":"chmod",
      "[Linux] Quelle sont les lettres permettant à un utilisateur de lire, écrire et exécuter un fichier ?":"rwx",
      "[LInux] Quelle commande permet d'exécuter une commande en tant que super utilisateur ?":"sudo"}


def serve_layout():
    choixQuestion=random.choice(list(dico.keys()))

    layout = html.Div([
        html.H1("Rattrapage Git, Python, Linux"),
        html.H3("Question : " + choixQuestion, id="question"),
        dcc.Input(id='user-input', type='text', value='', placeholder='Entrez votre réponse ici...'),
        html.Button('Evaluate answer', id='submit-button', n_clicks=0),
        html.Div(id='output'),
        html.H5("Veuillez cliquer sur random question pour changer de question"),
        html.A(html.Button('Random question', id='refresh-button'), href='http://13.39.83.94:8017')
    ])
    
    return layout

app.layout=serve_layout
app.title = "Formulaire RG"

@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='submit-button', component_property='n_clicks')],
    [State(component_id='user-input', component_property='value'),
     State(component_id='question', component_property='children')]
)

def verification_Dico(n_clicks, reponse_utilisateur, question_text):
    if n_clicks>0:
        reponse=dico[question_text.replace("Question : ", "")]
        if reponse_utilisateur.lower()==reponse.lower():
            return html.P("Bonne réponse ! ✅", style={'color':'green'})
        if unidecode.unidecode(reponse_utilisateur.lower()).__contains__(unidecode.unidecode(reponse.lower())):
            return html.P("Bonne réponse ! ✅", style={'color':'green'})
        else:
            return html.P(f"Mauvaise réponse ❌ La réponse était {reponse}", style={'color':'red'})
    else:
        return ""

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0",  port=8017)
