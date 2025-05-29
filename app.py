# Desenvolvido por: Daniel Martins e Hugo Bertoldo - 1º Sem
from shiny import App, ui, render, reactive
import pandas as pd
import matplotlib.pyplot as plt

dados = [
    {"Ano": 2000, "Posição": 28, "Vitórias": 4, "Empates": 4, "Derrotas": 16, "Gols Marcados": 26, "Artilheiro": "Luizão (26)", "Títulos": "Mundial de Clubes"},
    {"Ano": 2001, "Posição": 18, "Vitórias": 9, "Empates": 7, "Derrotas": 11, "Gols Marcados": 46, "Artilheiro": "Dados não disponíveis", "Títulos": ""},
    {"Ano": 2002, "Posição": 2, "Vitórias": 15, "Empates": 7, "Derrotas": 9, "Gols Marcados": 50, "Artilheiro": "Deivid (17)", "Títulos": "Copa do Brasil"},
    {"Ano": 2003, "Posição": 15, "Vitórias": 15, "Empates": 12, "Derrotas": 19, "Gols Marcados": 61, "Artilheiro": "Liédson (16)", "Títulos": ""},
    {"Ano": 2004, "Posição": 5, "Vitórias": 20, "Empates": 14, "Derrotas": 12, "Gols Marcados": 53, "Artilheiro": "Jô (8)", "Títulos": ""},
    {"Ano": 2005, "Posição": 1, "Vitórias": 24, "Empates": 9, "Derrotas": 9, "Gols Marcados": 87, "Artilheiro": "Carlos Tevez (31)", "Títulos": "Brasileirão"},
    {"Ano": 2006, "Posição": 9, "Vitórias": 15, "Empates": 8, "Derrotas": 15, "Gols Marcados": 41, "Artilheiro": "Carlos Tevez (15)", "Títulos": ""},
    {"Ano": 2007, "Posição": 17, "Vitórias": 10, "Empates": 14, "Derrotas": 14, "Gols Marcados": 40, "Artilheiro": "Finazzi (13)", "Títulos": ""},
    {"Ano": 2008, "Posição": 1, "Vitórias": 25, "Empates": 10, "Derrotas": 3, "Gols Marcados": 79, "Artilheiro": "Dentinho (24)", "Títulos": "Série B"},
    {"Ano": 2009, "Posição": 10, "Vitórias": 14, "Empates": 10, "Derrotas": 14, "Gols Marcados": 50, "Artilheiro": "Ronaldo (23)", "Títulos": "Paulista, Copa do Brasil"},
    {"Ano": 2010, "Posição": 3, "Vitórias": 19, "Empates": 11, "Derrotas": 8, "Gols Marcados": 65, "Artilheiro": "Bruno César (14)", "Títulos": ""},
    {"Ano": 2011, "Posição": 1, "Vitórias": 21, "Empates": 8, "Derrotas": 9, "Gols Marcados": 53, "Artilheiro": "Liédson (23)", "Títulos": "Brasileirão"},
    {"Ano": 2012, "Posição": 6, "Vitórias": 15, "Empates": 12, "Derrotas": 11, "Gols Marcados": 51, "Artilheiro": "Paulinho (26)", "Títulos": "Libertadores, Mundial de Clubes, Paulista, Recopa Sul-Americana"},
    {"Ano": 2013, "Posição": 10, "Vitórias": 11, "Empates": 17, "Derrotas": 10, "Gols Marcados": 27, "Artilheiro": "Paolo Guerrero (18)", "Títulos": "Paulista, Recopa Sul-Americana"},
    {"Ano": 2014, "Posição": 4, "Vitórias": 19, "Empates": 12, "Derrotas": 7, "Gols Marcados": 49, "Artilheiro": "Paolo Guerrero (16)", "Títulos": ""},
    {"Ano": 2015, "Posição": 1, "Vitórias": 24, "Empates": 9, "Derrotas": 5, "Gols Marcados": 71, "Artilheiro": "Jádson / Vágner Love (16)", "Títulos": "Brasileirão"},
    {"Ano": 2016, "Posição": 7, "Vitórias": 15, "Empates": 10, "Derrotas": 13, "Gols Marcados": 48, "Artilheiro": "Ángel Romero (13)", "Títulos": ""},
    {"Ano": 2017, "Posição": 1, "Vitórias": 21, "Empates": 9, "Derrotas": 8, "Gols Marcados": 50, "Artilheiro": "Jô (25)", "Títulos": "Brasileirão, Paulista"},
    {"Ano": 2018, "Posição": 13, "Vitórias": 11, "Empates": 11, "Derrotas": 16, "Gols Marcados": 34, "Artilheiro": "Jádson (15)", "Títulos": "Paulista"},
    {"Ano": 2019, "Posição": 8, "Vitórias": 14, "Empates": 14, "Derrotas": 10, "Gols Marcados": 42, "Artilheiro": "Gustavo (14)", "Títulos": "Paulista"},
    {"Ano": 2020, "Posição": 12, "Vitórias": 13, "Empates": 12, "Derrotas": 13, "Gols Marcados": 45, "Artilheiro": "Jô (8)", "Títulos": ""},
    {"Ano": 2021, "Posição": 5, "Vitórias": 15, "Empates": 12, "Derrotas": 11, "Gols Marcados": 40, "Artilheiro": "Jô (10)", "Títulos": ""},
    {"Ano": 2022, "Posição": 4, "Vitórias": 18, "Empates": 11, "Derrotas": 9, "Gols Marcados": 44, "Artilheiro": "Róger Guedes (15)", "Títulos": ""},
    {"Ano": 2023, "Posição": 13, "Vitórias": 12, "Empates": 14, "Derrotas": 12, "Gols Marcados": 47, "Artilheiro": "Róger Guedes (21)", "Títulos": ""},
    {"Ano": 2024, "Posição": 7, "Vitórias": 15, "Empates": 11, "Derrotas": 12, "Gols Marcados": 54, "Artilheiro": "Yuri Alberto (31)", "Títulos": ""},
]

df = pd.DataFrame(dados)
anos = list(df['Ano'])

app_ui = ui.page_fluid(
    ui.tags.style(
    """
    body {
        background: #181818 !important;
        color: #fafafa !important;
    }
    .card, .table, .form-select, .form-control, .shiny-table, .shiny-table th, .shiny-table td {
        background: #232323 !important;
        color: #fafafa !important;
        border-color: #2d2d2d !important;
    }
    .form-select, select, input, .input-group-text {
        background: #181818 !important;
        color: #fafafa !important;
        border-color: #444 !important;
    }
    .form-select:focus, input:focus {
        background: #232323 !important;
        color: #fff !important;
        border-color: #444 !important;
    }
    label, .form-label {
        color: #fafafa !important;
    }
    """
    ),
    ui.layout_columns(
        ui.card(
            ui.h3("Bem-vindo ao Painel de Desempenho do Corinthians!"),
            ui.p("Aqui você acompanha a trajetória do Corinthians no Campeonato Brasileiro e nas principais competições, temporada por temporada, a partir do ano 2000."),
            ui.p("Explore resultados, artilheiros, estatísticas e conquistas do Timão, de forma rápida e visual."),
            ui.p("Escolha o ano desejado no menu acima e veja como foi a campanha do Corinthians naquele ano!"),
        ),
        ui.img(
            src="https://preview.redd.it/2gcfeob6zyu81.png?width=640&crop=smart&auto=webp&s=7b73731d8e607c59b9e66b9dad14dfa1526b1c05",
            style="width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"
        ),
    ),
    ui.input_select("ano", "Selecione o ano da temporada:", [str(a) for a in anos], selected=str(anos[-1])),
    ui.output_table("tabela"),
    ui.output_plot("grafico"),
    ui.output_text("titulos"),
    ui.output_text("total_gols"),
)


def calcular_total_gols(dados):
    total = 0
    for d in dados:
        total += d["Gols Marcados"]
    return total

def server(input, output, session):
    @reactive.Calc
    def dados_ano():
        ano = int(input.ano())
        return df[df["Ano"] == ano]

    @output
    @render.table
    def tabela():
        return dados_ano().drop(columns=["Títulos"])

    @output
    @render.plot
    def grafico():
        row = dados_ano().iloc[0]
        labels = ["Vitórias", "Empates", "Derrotas"]
        valores = [row["Vitórias"], row["Empates"], row["Derrotas"]]
        # Define o fundo escuro do gráfico e do canvas
        fig, ax = plt.subplots(facecolor="#232323")
        ax.bar(labels, valores, color="#1976d2")  # azul corinthiano!
        ax.set_title("Vitórias, Empates e Derrotas", color="#fafafa")
        ax.set_facecolor("#232323")
        ax.tick_params(colors="#fafafa")
        # Bordas dos gráficos
        ax.spines['bottom'].set_color('#fafafa')
        ax.spines['left'].set_color('#fafafa')
        ax.spines['right'].set_color('#232323')
        ax.spines['top'].set_color('#232323')
        ax.yaxis.label.set_color('#fafafa')
        ax.xaxis.label.set_color('#fafafa')
        # Cor dos números dos eixos
        ax.yaxis.set_tick_params(labelcolor='#fafafa')
        ax.xaxis.set_tick_params(labelcolor='#fafafa')
        return fig


    @output
    @render.text
    def titulos():
        row = dados_ano().iloc[0]
        if row["Títulos"]:
            return f"Títulos na temporada: {row['Títulos']}"
        return ""

    @output
    @render.text
    def total_gols():
        total = calcular_total_gols(dados)
        return f"Total de gols marcados pelo Corinthians desde 2000: {total}"

app = App(app_ui, server)
