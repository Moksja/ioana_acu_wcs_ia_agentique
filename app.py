import plotly.express as px
import pandas as pd
import os

html_name = "analyse_ventes.html"

if os.path.exists(html_name):
    os.remove(html_name)
    print(f"Précédent {html_name} supprimé.")

data = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')
cat_order = {
    "region": ["Nord", "Sud"],
    "produit": ["Produit A", "Produit B", "Produit C"]
}

figure_ca_region = px.pie(data, values='prix', names='region', title="chiffres d'affaires par région", category_orders=cat_order)
figure_qte_region = px.pie(data, values='qte', names='region', title='quantité vendue par région', category_orders=cat_order)
figure_qte_pdt = px.pie(data, values="qte", names="produit", title="quantité vendue par produit", category_orders=cat_order)
fig_ca_pdt = px.pie(data, values="prix", names="produit", title="chiffres d'affaires par produit", category_orders=cat_order)
fig_qte_jour = px.histogram(data, x="date", y="qte", color="region", title="quantité vendue par jour et par région", category_orders=cat_order, barmode="group")
fig_ca_jour = px.histogram(data, x="date", y="prix", color="region", title="chiffres d'affaires par jour et par région", category_orders=cat_order, barmode="group")

fig_to_write = [
    {"Répartition par région": [figure_qte_region, figure_ca_region]},
    {"Répartition par produit": [figure_qte_pdt, fig_ca_pdt]},
    {"Évolution journalière": [fig_qte_jour, fig_ca_jour]},
]

text_bloc = [
    "Bien que la région Sud fasse plus de ventes en termes de quantités, le chiffre d'affaires de la région Nord reste légèrement supérieure.",
    """De même concernant les produits : le produit A a une plus petite rentabilité bien que ce soit le n°1 des ventes. Au contraire, le produit C 
    a la plus grande rentabilité bien qu'il soit le moins vendu.""",
    "Les régions ont un chiffre d'affaires équivalent malgré une variation notable dans les quantités vendues. En fin de mois, les ventes chutent dans les deux zones."
]
pie_width = "30%"
bar_width = "45%"

with open(html_name, 'a') as f:
    f.write("""
    <html>
    <head>
            <style>
                body { font-family: sans-serif; }
            </style>
    </head>
    <body>
        <h1>Analyse des ventes</h1>
    """)

    for i, row in enumerate(fig_to_write):
        for k, values in row.items():
            f.write(f'<h2 class="theme-title">{k}</h2>\n')
            f.write(f'<div class="row" style="margin:16px;display:flex; justify-content:left, gap:24px;">\n<p style="width:20%;padding-top:16px;text-align:justify">{text_bloc[i]}')
            for fig in values:
                w = pie_width if k != "Évolution journalière" else bar_width
                f.write(fig.to_html(full_html=False, include_plotlyjs='cdn', default_width=w))
            f.write('</div>\n')

    f.write("</body></html>")

print(f'{html_name} généré avec succès !')
print(f'Figures générées avec succès !')