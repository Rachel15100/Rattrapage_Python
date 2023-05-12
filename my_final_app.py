from dash import Dash, dcc, html, Output, Input, State, callback
import random
import unidecode


app = Dash(__name__)
server=app.server

dico=dict()
dico={"Quelle commande permet de créer une nouvelle branche ?":"git branch",
      "Quel est l'opérateur de comparaison qui permet de vérifier si deux valeurs sont égales ?":"==",
      "Quelle commande linux permet de lister le contenu d'un répertoire ?": "ls"}


def serve_layout():
    choixQuestion=random.choice(list(dico.keys()))

    layout = html.Div([
        html.H1("Rattrapage Git, Python, Linux"),
        html.H3("Question : " + choixQuestion, id="question"),
        dcc.Input(id='user-input', type='text', value='', placeholder='Entrez votre réponse ici...'),
        html.Button('evaluate answer', id='submit-button', n_clicks=0),
        html.Div(id='output'),
        html.H5("Veuillez actualiser la page pour une accéder à une autre question"),
        html.Br(),
        html.A(html.Button('random question', id='refresh-button'), href='http://13.39.83.94:8025')
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
            return html.P("Bonne réponse !")
        else:
            return html.P("Mauvaise réponse")
    else:
        return ""

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0",  port=8025)
