import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

def plot_suicidios_brasil_masc():
    df = pd.read_csv('BrazilSuicidiosIdadeMasc.csv', header=0, index_col=0, parse_dates=True, low_memory=False)
    df.plot()

    plt.title('Suicídios do Sexo Masculino no Brasil (1985-2015)')
    plt.ylabel('Taxa de Suicídios')
    plt.show()

def plot_suicidios_america_do_sul():
    df = pd.read_csv('SouthAmericaSuicidios2003.csv')

    fig = go.Figure(data=go.Choropleth(
        locations=df['country'],
        z=df['year-2003'].astype(int),
        locationmode='country names',
        colorscale=['orange', 'blue', 'red'],
        colorbar_title="Índice Suicídios",
    ))
    fig.update_layout(title_text='Suicídios na América do Sul (2003)', geo_scope='south america')

    fig.write_html("suicidios_america_sul.html")  # Salva como HTML
    print("Gráfico salvo em suicidios_america_sul.html - Abra no navegador")

def plot_suicidios_brasil_treemap():
    df = pd.read_csv('Brazil2010MascFemi.csv')

    fig = px.treemap(df, path=['sexo', 'idade'], values='quantidade')
    fig.update_layout(title_text='Suicídios no Brasil por Sexo e Idade (2010)')

    fig.write_html("suicidios_brasil_treemap.html")  # Salva como HTML
    print("Gráfico salvo em suicidios_brasil_treemap.html - Abra no navegador")

if __name__ == "__main__":
    plot_suicidios_brasil_masc()
    plot_suicidios_america_do_sul()
    plot_suicidios_brasil_treemap()
