import streamlit as st
from streamlit_calendar import calendar
from scraper_engine import scrape_real_movies_and_sessions as get_movies_by_date
from poster_api import get_movie_poster
import json
from datetime import datetime

st.set_page_config(page_title="CinePlanner AI", page_icon="🎬", layout="wide")
st.markdown("<style>.stApp { background: #0d0d1a; color: white; }</style>", unsafe_allow_html=True)

# Session State başlatma
if 'my_events' not in st.session_state:
    st.session_state.my_events = []
if 'movies' not in st.session_state:
    st.session_state.movies = []

with st.sidebar:
    st.title("🎬 CinePlanner")
    # Bugünün tarihini varsayılan yap
    d = st.date_input("Tarih Seç:", value=datetime.today())
    
    if st.button("🔍 Gerçek Seansları Tara"):
        with st.spinner("Canlı veriler taranıyor..."):
            # Tarihi GG Ay YYYY formatına çevir (Örn: 08 Nisan 2026)
            date_str = d.strftime("%d %B %Y")
            res = get_movies_by_date("İstanbul", date_str)
            try:
                data = json.loads(res)
                st.session_state.movies = data.get("movies", [])
                st.success(f"{len(st.session_state.movies)} film bulundu!")
            except:
                st.error("Veri işlenirken bir hata oluştu.")

col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("🍿 Vizyondakiler")
    if not st.session_state.movies:
        st.info("Henüz film taranmadı veya sonuç bulunamadı.")
        
    for m in st.session_state.movies:
        with st.expander(f"🎬 {m['film_adi']}"):
            p_col, i_col = st.columns([1, 2])
            
            # Afiş çekme
            clean_name = m.get('temiz_film_adi', m['film_adi'])
            poster = get_movie_poster(clean_name)
            p_col.image(poster, use_container_width=True)
            
            with i_col:
                for s in m.get('salonlar', []):
                    st.markdown(f"📍 **{s['sinema_adi']}**")
                    seanslar = s.get('seanslar', [])
                    
                    # Seans butonlarını yan yana diz
                    btn_cols = st.columns(len(seanslar) if seanslar else 1)
                    for idx, sn in enumerate(seanslar):
                        # Buton anahtarını benzersiz yap
                        btn_key = f"btn_{m['film_adi']}_{s['sinema_adi']}_{sn}_{idx}"
                        if btn_cols[idx % len(btn_cols)].button(sn, key=btn_key):
                            # Takvime eklenecek yeni olay
                            new_event = {
                                "title": f"{m['film_adi']} ({s['sinema_adi']})",
                                "start": f"{d.strftime('%Y-%m-%d')}T{sn}:00",
                                "end": f"{d.strftime('%Y-%m-%d')}T{datetime.strptime(sn, '%H:%M').replace(hour=(datetime.strptime(sn, '%H:%M').hour + 2)).strftime('%H:%M')}:00",
                                "url": s.get('bilet_linki', 'https://www.biletinial.com'),
                                "backgroundColor": "#e50914",
                                "borderColor": "#ffffff"
                            }
                            # Listeye ekle ve sayfayı yenile
                            st.session_state.my_events.append(new_event)
                            st.toast(f"✅ {m['film_adi']} takvime eklendi!")
                            st.rerun()

with col2:
    st.subheader("📅 Film Takvimim")
    
    # Takvim ayarları
    calendar_options = {
        "initialView": "dayGridMonth",
        "headerToolbar": {
            "left": "prev,next today",
            "center": "title",
            "right": "dayGridMonth,timeGridWeek"
        },
        "selectable": True,
    }
    
    # Takvimi çiz (key parametresi dinamik güncellemeyi sağlar)
    calendar(
        events=st.session_state.my_events,
        options=calendar_options,
        key="cinema_calendar"
    )
    
    if st.button("🗑️ Tüm Planı Temizle"):
        st.session_state.my_events = []
        st.rerun()