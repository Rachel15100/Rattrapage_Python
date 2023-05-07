from dash import Dash, dcc, html, Output, Input, State, callback
import plotly.express as px
import random



app = Dash(__name__)
server=app.server


question = ["Quelle commande permet de créer une nouvelle branche ?", "Quel est l'opérateur de comparaison qui permet de vérifier si deux valeurs sont égales ?"]
correct_answer = ["git branch", "=="]

indexQuestion=random.randint(0, len(question)-1)
choixQuestion=question[indexQuestion]

app.layout = html.Div([
    html.H1("Quiz"),
    html.P("Question : " + choixQuestion),
    dcc.Input(id='user-input', type='text', value='', placeholder='Entrez votre réponse ici...'),
    html.Button('Vérifier la réponse', id='submit-button', n_clicks=0),
    html.Div(id='output')
])


@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='submit-button', component_property='n_clicks')],
    [State(component_id='user-input', component_property='value')]
)

def check_answer(n_clicks, user_answer):
    if n_clicks > 0:
        if user_answer.lower() == correct_answer[indexQuestion].lower():
            return html.P("Bonne réponse !")
        else:
            return html.P(f"Mauvaise réponse. La réponse était {correct_answer}")
    else:
        return ""

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=8001)
