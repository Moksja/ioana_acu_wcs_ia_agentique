import plotly.express as px
import pandas as pd
import os

html_name = "analyse_ventes.html"

fig_def_width = "30%"
bar_width = "50%"

data = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')
cat_order = {
    "region":["Nord","Sud"],
    "produit":["Produit A", "Produit B", "Produit C"]
}


figure_ca_region = px.pie(data, values='prix', names='region', title="chiffres d'affaires par région", category_orders=cat_order)
figure_qte_region = px.pie(data, values='qte', names='region', title='quantité vendue par région', category_orders=cat_order)
figure_qte_pdt = px.pie(data, values="qte", names="produit", title="quantité vendue par produit", category_orders=cat_order)
fig_ca_pdt = px.pie(data, values="prix", names="produit", title="chiffres d'affaires par produit", category_orders=cat_order)
fig_ca_jour = px.histogram(data, x="date", y="prix", color="region", title="chiffres d'affaires par jour et par region",category_orders=cat_order, barmode="group")
fig_qte_jour = px.histogram(data, x="date", y="qte", color="region", title="quantité vendue par jour et par region",category_orders=cat_order, barmode="group")
fig_qte_jour = px.histogram(data, x="date", y="prix", color="region", title="chiffres d'affaires par jour et par region",category_orders=cat_order, barmode="group")

fig_to_write = [figure_qte_region,figure_ca_region,figure_qte_pdt,fig_ca_pdt,fig_ca_jour]

os.remove(html_name)
print(f"Précedent {html_name} supprimé.")

with open(html_name, 'a') as f:
    for fig in fig_to_write :
        width = fig_def_width if fig != fig_ca_jour else bar_width
        f.write(fig.to_html(full_html=False, include_plotlyjs='cdn',default_width=width))

print(f'{html_name} généré avec succès !')
print(f'Figures générées avec succès !')
