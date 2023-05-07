from dash import Dash, dcc, html, Output, Input, State, callback
import random


# Définissez la question et la réponse correcte
question = "Quelle commande permet de créer une nouvelle branche ?"
correct_answer = "git branch"

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Quiz"),
    html.P(question),
    dcc.Input(id='user-input', type='text', value='', placeholder='Entrez votre réponse ici...'),
    html.Button('Vérifier la réponse', id='submit-button', n_clicks=0),
    html.Div(id='output')
])


# Créez une fonction de rappel pour vérifier la réponse
@app.callback(
    Output('output', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('user-input', 'value')]
)

def check_answer(n_clicks, user_answer):
    if n_clicks > 0:
        if user_answer.lower() == correct_answer.lower():
            return html.P("Bonne réponse !")
        else:
            return html.P(f"Mauvaise réponse. La réponse était {correct_answer}")
    else:
        return ""

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=8001)
