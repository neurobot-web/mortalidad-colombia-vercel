from flask import Flask
import dash
from dash import html, dcc
import pandas as pd

# Create a simple test app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Test App - Mortalidad Colombia'),
    html.P('Si ves esto, la aplicación funciona!'),
    html.Div(id='test-output', children='Cargando datos...')
])

@app.callback(
    dash.Output('test-output', 'children'),
    dash.Input('test-output', 'id')
)
def test_callback(_):
    try:
        # Test data loading
        df = pd.read_excel('Anexos/Anexo1.NoFetal2019_CE_15-03-23.xlsx')
        return f'Datos cargados exitosamente: {len(df)} registros'
    except Exception as e:
        return f'Error cargando datos: {str(e)}'

# Vercel serverless function handler
def handler(request):
    return app.server