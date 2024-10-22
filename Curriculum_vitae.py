import streamlit as st

st.set_page_config(
    page_title='Curriculum vitae',
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar navigation
st.sidebar.page_link('Curriculum_vitae.py', label='Curriculum vitae')
st.sidebar.page_link('./pages/Portfolio.py', label='Portfolio')

with st.sidebar:
    st.header("More about me", divider=True)
    st.image("./photo CV.png",caption ="Aurélien BRONCARD", use_column_width=True)
    st.link_button("My LinkedIn profil",url='https://www.linkedin.com/in/aurelien-broncard-data-ia/',type="primary",use_container_width=True)

    st.markdown("""
    <div style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
        <h2>Coordonnées :</h2>
        <p>Téléphone : 06 15 02 07 01<br>
        E-mail : aurelien.broncard@efrei.net<br>
        Adresse : rue d’Amsterdam, 75008 PARIS</p>
    </div>
    """,unsafe_allow_html=True)
    st.markdown(" ")

    st.markdown("""
    <div style="background-color: white; padding: 10px; border-radius: 15px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
        <h2>Activités personnelles :</h2>
        <ul>
            <li>Sport : Tennis bon niveau, Natation</li>
            <li>Activités associatives & culturelles : président de l’association étudiante de visite de musées</li>
            <li>Séjour linguistique : École Américaine à New York (2 semaines)</li>
            <li>Formation de la Protection Civile</li>
            <li>Ouverture sur le monde : voyages en Europe, Amérique du Nord et Asie du Sud-Est</li>
            <li>Permis Bateau côtier (16 ans)</li>
        <ul>
    </div>
    """,unsafe_allow_html=True)

with st.container():
    st.header('**Curriculum vitae**', divider=True)
tab1, tab2, tab3, tab4 = st.tabs(["Formation", "Projets Académiques", "Expérience professionnelle", "Compétences"])
tab1.markdown("""
<div class="section">
        <h2>FORMATION</h2>
    </div>
    <div class="content">
        <h3>Étudiant en 4ème année | Cursus ingénieur | Filière Data & IA | EFREI Paris</h3>
        <ul>
            <li>École d’ingénieurs généraliste en informatique et technologies numériques, Biologie & Numérique</li>
            <li>3 années de licence en bio-informatique, à la croisée des chemins entre informatique, biologie, mathématiques et physique</li>
            <li>Actuellement en master 1 en Data & Intelligence Artificielle</li>
        </ul>
        <h3>Semestre d’échange à l’Université de Californie Irvine - États-Unis (2023)</h3>
        <ul>
            <li>Participation à un semestre d’échange enrichissant, favorisant l’immersion culturelle</li>
            <li>Capacité d’adaptation et de communication inter-culturelle démontrée tout en s’engageant dans des cours rigoureux et des projets collaboratifs</li>
        </ul>
        <h3>Lycée Racine - Paris VIIIème (2021)</h3>
    </div>

""",unsafe_allow_html=True)

tab2.markdown("""
<div class="section">
        <h2>PROJETS ACADÉMIQUES</h2>
    </div>
    <div class="content">
        <h3>EXPLAIN (EXplainable Patent Learning for Artificial INtelligence) - EFREI Paris</h3>
        <p>Réponse à un appel d’offre client de l’entreprise LIPSTIP par l’entraînement de modèles IA de classification de textes sur un corpus avec explication de la classification sur une application utilisateur</p>
        <h3>Projet Atelier Data Science - EFREI Paris</h3>
        <p>Développement de visualisations et d’une analyse sur les transactions des valeurs foncières de 2023 en France</p>
    </div>
""",unsafe_allow_html=True)

tab3.markdown("""
<div class="section">
        <h2>EXPÉRIENCE PROFESSIONNELLE</h2>
    </div>
    <div class="content">
        <h3>Stage Commercial</h3>
        <p>Vélo Électrique France | Paris XIXème | Janvier 2023</p>
        <p>Stage de vente de vélos électriques de toutes marques et de tous modèles</p>
        <h3>Stage d’Exécution</h3>
        <p>AXA Banque | Val-de-Fontenay | Juin 2022</p>
        <p>Stage découverte du monde de l'entreprise dans le pôle communication avec le réseau d'agent AXA Banque</p>
        <h3>Stage d’Observation</h3>
        <p>Atelier 4+ | Paris XXème | Janvier 2018</p>
        <p>Stage technique en 3ème dans un cabinet d'Architecture et d'Ingénierie</p>
    </div>
""",unsafe_allow_html=True)
tab4.markdown("""
 <div class="section">
        <h2>COMPÉTENCES</h2>
    </div>
    <div class="content">
        <h3>Compétences en IT :</h3>
        <ul class="skills-list">
            <li><strong>HTML / CSS / JavaScript / Java :</strong> Bon niveau</li>
            <li><strong>Python / C / UML / SQL (MariaDB, MySQL) :</strong> Confirmé</li>
            <li><strong>Excel, PowerPoint, Word :</strong> Bon niveau</li>
            <li><strong>Cisco CyberSecurity Essentials Certificate</strong></li>
        </ul>
        <h3>Langues :</h3>
        <ul class="skills-list">
            <li>Français Langue maternelle | Projet Voltaire : 767 - Vérification : W4RMXXA</li>
            <li>Anglais - Niveau Européen C1 (Étudiant British Council - Paris, de la 6ème à la Terminale, TOEIC : 990/990)</li>
            <li>Espagnol - Niveau Débutant</li>
        </ul>
    </div>
""",unsafe_allow_html=True)