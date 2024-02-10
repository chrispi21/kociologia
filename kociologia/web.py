from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from domain.opisywacz_kotow import opisywacz_kotow
from domain.wygeneruj_obraz_kota import wygeneruj_obraz_kota
from domain.wykrywacz_ras_kotow import wykrywacz_ras_kotow

NO_CAT_IMAGE = "https://thumb.ac-illust.com/a4/a41a97601767b3e83dda8cb700d37101_t.jpeg"
INIT_CAT = "kociologia/ui/assets/black_cat.jpg"

rasa_kota = st.text_input('Podaj nazwę rasy kota')

if rasa_kota:
    if wykrywacz_ras_kotow(rasa_kota):
        st.write(opisywacz_kotow(rasa_kota))
        st.image(wygeneruj_obraz_kota(rasa_kota))
    else:
        st.image(NO_CAT_IMAGE)
else:
    st.image(INIT_CAT)
