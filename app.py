import plotly.express as px
import pandas as pd
import os

html_name = "analyse_ventes.html"
fig_def_width = "30%"
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure_qte_region = px.pie(données, values='qte', names='region', title='quantité vendue par région')
figure_qte_pdt = px.pie(données, values="qte", names="produit", title="quantité vendue par produit")

os.remove(html_name)
print(f"Précedent {html_name} supprimé.")

with open(html_name, 'a') as f:
    f.write(figure_qte_region.to_html(full_html=False, include_plotlyjs='cdn',default_width=fig_def_width))
    f.write(figure_qte_pdt.to_html(full_html=False, include_plotlyjs='cdn',default_width=fig_def_width))

print(f'{html_name} généré avec succès !')
print(f'Figures générées avec succès !')
