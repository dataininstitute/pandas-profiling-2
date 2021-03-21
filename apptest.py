import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


st.title("Analyser votre Dataset avec Pandas-profiling")
st.subheader("Insérer votre Dataset au format csv, Pandas-profiling s'occupe de l'analyser !")

with st.beta_expander("Voir plus"):
    st.write("Pour chaque colonne, les statistiques suivantes sont présentées dans un rapport HTML interactif :  \n"  
    "- **Inférence de type**: détecte les types de colonnes dans un dataframe. \n"
    "- **Essentiels**: type, valeurs uniques, valeurs manquantes \n"
    "- Statistiques quantiles telles que valeur minimale, Q1, médiane, Q3, maximum, intervalle, intervalle interquartile \n"
    "- Statistiques descriptives comme la moyenne, le mode, l'écart type, la somme, l'écart absolu médian, le coefficient de variation, l'aplatissement, l'asymétrie \n"
    "- Valeurs les plus fréquentes \n"
    "- Histogramme \n"
    "- Corrélations mettant en évidence des variables hautement corrélées, matrices de Spearman, Pearson et Kendall \n"
    "- Matrice des valeurs manquantes, nombre, carte thermique et dendrogramme des valeurs manquantes \n"
    "- L'analyse de texte apprend les catégories (majuscules, espace), les scripts (latin, cyrillique) et les blocs (ASCII) de données textuelles. \n"
    "- L'analyse des fichiers et des images extrait la taille des fichiers, les dates de création et les dimensions et recherche les images tronquées ou celles contenant des informations EXIF. \n"
    "\n"
    "\n")

#file_upload = st.file_uploader("Uploader votre csv à analyser", type=["csv"])
#file_upload = st.file_uploader("Uploader votre json à analyser", type=["json"])


# Sidebar choose the type of file
st.sidebar.title("Pandas-profilng")

@st.cache
def load_data():
    df = pd.DataFrame(
		 np.random.rand(100, 5),
		 columns=['a', 'b', 'c', 'd', 'e'])
    
    return df

from PIL import Image
image = Image.open('panda.jpg')
st.sidebar.image(image)

# choix du type de fichier csv a importer
add_selectbox = st.sidebar.selectbox(
"Quel type de fichier voulez-vous analyser ?",
("Sample","CSV", "JSON","Excel"))

# choix du file uploader en fonction du type de fichier

if add_selectbox == "Sample":
     file_upload = load_data()
     
elif add_selectbox == "CSV":
     file_upload = st.sidebar.file_uploader("Uploader votre CSV à analyser", type=["csv"])
     sep_csv = st.sidebar.selectbox("Quel est le séparateur ?",(",",";","|"))

elif add_selectbox == "JSON":
     file_upload = st.sidebar.file_uploader("Uploader votre JSON  à analyser", type=["json"])
     sep_csv = None
     
elif add_selectbox == "Excel":
     file_upload = st.sidebar.file_uploader("Uploader votre JSON  à analyser", type=["xlsx"])
     sep_csv = None


# choix du pd.read en fonction du chix du file uploader

if file_upload is not None and add_selectbox == "CSV":
     df = pd.read_csv(file_upload,sep=sep_csv)

elif file_upload is not None and add_selectbox == "JSON":
     df = pd.read_json(file_upload)
     
elif file_upload is not None and add_selectbox == "Excel":
     df = pd.read_excel(file_upload)     

else:
	 df=load_data()
     
   
    


pr = ProfileReport(df, explorative=True)


st.write(df)
st_profile_report(pr)
