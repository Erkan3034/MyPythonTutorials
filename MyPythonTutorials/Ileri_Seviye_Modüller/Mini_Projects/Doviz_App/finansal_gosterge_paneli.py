"""
# "Finansal Gösterge Paneli"
# Bu proje, Dolar, Euro, Altın, BIST 100, GBP ve CHF gibi finansal verileri gerçek zamanlı olarak takip etmenizi sağlar.
# Kullanıcılar, döviz kurlarını arayabilir, döviz çevirici ile TRY cinsinden hesaplamalar yapabilir ve portföylerini değerlendirebilir.
# Veriler, doviz.com sitesinden çekilir ve zaman içindeki değişim grafikleri oluşturulur.
# Streamlit ile geliştirilen bu uygulama, kullanıcı dostu bir arayüz sunar ve mobil uyumludur.
# Geliştirici: ERKAN TURGUT, 2025

"""
import requests
from bs4 import BeautifulSoup
import streamlit as st
import time
import plotly.express as px
import pandas as pd
import sqlite3
from datetime import datetime

# Sayfa yapılandırması
st.set_page_config(page_title="Finansal Gösterge Paneli", page_icon="💰", layout="centered",
                   initial_sidebar_state="auto")

# Responsive CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
        padding: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 8px 16px;
        font-size: clamp(14px, 2.5vw, 16px);
        width: 100%;
        margin: 5px 0;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .metric-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin: 10px 0;
        width: 100%;
    }
    .metric-label {
        font-size: clamp(16px, 3vw, 18px);
        font-weight: bold;
        color: #333;
    }
    .metric-value {
        font-size: clamp(20px, 4vw, 24px);
        color: #4CAF50;
    }
    .change-up {
        color: #28a745;
        font-size: clamp(12px, 2vw, 14px);
    }
    .change-down {
        color: #dc3545;
        font-size: clamp(12px, 2vw, 14px);
    }
    /* Header stilleri */
    .header {
        background-color: #2c3e50;
        color: white;
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .header h1 {
        font-size: clamp(24px, 6vw, 36px);
        margin: 0;
        font-weight: 700;
    }
    .header p {
        font-size: clamp(14px, 3vw, 16px);
        margin: 5px 0 0;
    }
    /* Başlık stilleri */
    h2 {
        font-size: clamp(18px, 4vw, 24px);
        color: #34495e;
        text-align: left;
        margin: 15px 0;
        font-weight: 600;
        border-bottom: 2px solid #4CAF50;
        padding-bottom: 5px;
    }
    /* Arama çubuğu stilleri */
    .search-bar {
        margin: 20px 0;
        text-align: center;
    }
    .search-bar input {
        padding: 10px;
        font-size: clamp(14px, 2.5vw, 16px);
        border-radius: 5px;
        border: 1px solid #ccc;
        width: 100%;
        max-width: 400px;
    }
    /* Footer stilleri */
    .footer {
        background-color: #2c3e50;
        color: white;
        padding: 15px;
        text-align: center;
        border-radius: 10px;
        margin-top: 20px;
        font-size: clamp(12px, 2.5vw, 14px);
    }
    .footer a {
        color: #4CAF50;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    /* Mobil uyumluluk */
    @media (max-width: 768px) {
        .stColumn > div {
            display: block;
            width: 100%;
        }
        .metric-card {
            margin: 5px 0;
        }
        .stForm {
            padding: 0;
        }
        h2 {
            text-align: center;
            border-bottom: none;
        }
        .header, .footer {
            padding: 15px;
        }
        .search-bar input {
            max-width: 100%;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Veritabanı ve diğer fonksiyonlar
def init_db():
    conn = sqlite3.connect("finansal_veriler.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS veriler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarih TEXT,
            usd_try REAL,
            eur_try REAL,
            altin REAL,
            bist_100 REAL
        )
    """)
    conn.commit()
    return conn

def gecmis_verileri_yukle():
    conn = init_db()
    df = pd.read_sql_query("SELECT * FROM veriler ORDER BY tarih DESC", conn)
    conn.close()
    return df

def gecmis_verileri_kaydet(veri):
    conn = init_db()
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("""
        INSERT INTO veriler (tarih, usd_try, eur_try, altin, bist_100)
        VALUES (?, ?, ?, ?, ?)
    """, (timestamp, veri["USD"], veri["EUR"], veri["Altın"], veri["BIST 100"]))
    conn.commit()
    conn.close()

def finansal_verileri_cek():
    url = "https://www.doviz.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        veri = {}
        for key, socket_key in [("USD", "USD"), ("EUR", "EUR"), ("Altın", "gram-altin"), ("BIST 100", "XU100")]:
            value = soup.find("span", {"data-socket-key": socket_key, "class": "value"})
            change = soup.find("div", {"data-socket-key": socket_key, "class": "change-rate"})
            if value:
                veri[key] = float(value.text.strip().replace(".", "").replace(",", "."))
                veri[f"{key}_change"] = change.text if change else "0%"
            else:
                st.error(f"{key} verisi bulunamadı.")
                return None
        gecmis_verileri_kaydet(veri)
        return veri
    except Exception as e:
        st.error(f"Veri çekme hatası: {e}")
        return None

def portfoy_degerini_hesapla(veri, usd_miktar, eur_miktar, altin_miktar, bist_miktar):
    if veri is None:
        return None
    usd_deger = veri["USD"] * usd_miktar
    eur_deger = veri["EUR"] * eur_miktar
    altin_deger = veri["Altın"] * altin_miktar
    bist_deger = veri["BIST 100"] * bist_miktar / 100
    toplam_deger = usd_deger + eur_deger + altin_deger + bist_deger
    return {
        "USD Değeri (TRY)": usd_deger,
        "EUR Değeri (TRY)": eur_deger,
        "Altın Değeri (TRY)": altin_deger,
        "BIST 100 Değeri (TRY)": bist_deger,
        "Toplam Portföy Değeri (TRY)": toplam_deger
    }

def degisim_orani_hesapla(df, column):
    df = df.sort_values(by="tarih")
    df["Degisim_Orani"] = df[column].pct_change() * 100
    return df

# Ana uygulama
def main():
    # Header
    st.markdown("""
        <div class="header">
            <h1>💸 Finansal Gösterge Paneli</h1>
            <p>Dolar, Euro, Altın ve BIST 100'ü gerçek zamanlı olarak takip edin!</p>
        </div>
    """, unsafe_allow_html=True)

    gecmis_veriler = gecmis_verileri_yukle()

    with st.spinner("📊 Veriler yükleniyor..."):
        finansal_veri = finansal_verileri_cek()

    if finansal_veri:
        # Arama Çubuğu
        st.markdown('<div class="search-bar">', unsafe_allow_html=True)
        search_query = st.text_input("", placeholder="Döviz kuru ara (ör. USD, EUR, Altın, BIST 100)...")
        st.markdown('</div>', unsafe_allow_html=True)

        # Güncel Piyasa Değerleri (Arama ile filtrelenmiş)
        st.markdown('<h2>📈 Güncel Piyasa Değerleri</h2>', unsafe_allow_html=True)
        available_keys = ["USD", "EUR", "Altın", "BIST 100"]
        filtered_keys = available_keys

        if search_query:
            search_query = search_query.strip().capitalize()
            filtered_keys = [key for key in available_keys if search_query.lower() in key.lower()]
            if not filtered_keys:
                st.warning(f"'{search_query}' ile eşleşen bir döviz kuru bulunamadı.")

        for key in filtered_keys:
            unit = "TRY" if key in ["USD", "EUR"] else "TRY/gram" if key == "Altın" else "puan"
            change_class = "change-up" if "+" in finansal_veri[f"{key}_change"] else "change-down"
            st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">{key}</div>
                    <div class="metric-value">{finansal_veri[key]:.2f} {unit}</div>
                    <div class="{change_class}">{finansal_veri[f'{key}_change']}</div>
                </div>
            """, unsafe_allow_html=True)

        # Döviz Çevirici
        st.markdown('<h2>💱 Döviz Çevirici</h2>', unsafe_allow_html=True)
        with st.form(key="doviz_cevirici_form"):
            miktar = st.number_input("Miktar", min_value=0.0, value=100.0)
            doviz_turu = st.selectbox("Döviz Türü", ["USD", "EUR"])
            cevir_button = st.form_submit_button(label="Çevir")
        if cevir_button:
            sonuc = miktar * finansal_veri[doviz_turu]
            st.success(f"{miktar} {doviz_turu} = {sonuc:.2f} TRY")

        # Portföy Hesaplama
        st.markdown('<h2>💼 Portföyünüzü Hesaplayın</h2>', unsafe_allow_html=True)
        with st.form(key="portfoy_form"):
            usd_miktar = st.number_input("USD Miktarı", min_value=0.0, value=100.0)
            eur_miktar = st.number_input("EUR Miktarı", min_value=0.0, value=50.0)
            altin_miktar = st.number_input("Altın (gram)", min_value=0.0, value=10.0)
            bist_miktar = st.number_input("BIST 100 Yatırımı", min_value=0.0, value=1000.0)
            submit_button = st.form_submit_button(label="Hesapla")

        if submit_button:
            portfoy = portfoy_degerini_hesapla(finansal_veri, usd_miktar, eur_miktar, altin_miktar, bist_miktar)
            if portfoy:
                st.markdown('<h2>📊 Portföy Değerlendirmesi</h2>', unsafe_allow_html=True)
                for key in portfoy:
                    st.write(f"**{key}**: {portfoy[key]:.2f} TRY")
                df = pd.DataFrame({
                    "Varlık": ["USD", "EUR", "Altın", "BIST 100"],
                    "Değer (TRY)": [portfoy[k] for k in ["USD Değeri (TRY)", "EUR Değeri (TRY)", "Altın Değeri (TRY)", "BIST 100 Değeri (TRY)"]]
                })
                fig = px.pie(df, values="Değer (TRY)", names="Varlık", title="Portföy Dağılımı")
                st.plotly_chart(fig, use_container_width=True)

        # Grafikler
        st.markdown('<h2>📉 Zaman İçindeki Değişim</h2>', unsafe_allow_html=True)
        tabs = st.tabs(["USD/TRY", "EUR/TRY", "Altın", "BIST 100"])
        for i, (col, title) in enumerate([("usd_try", "USD/TRY"), ("eur_try", "EUR/TRY"), ("altin", "Altın"), ("bist_100", "BIST 100")]):
            with tabs[i]:
                if not gecmis_veriler.empty:
                    df = degisim_orani_hesapla(gecmis_veriler, col)
                    fig = px.line(df, x="tarih", y=col, title=f"{title} Değişimi")
                    fig.update_layout(height=300)
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning(f"{title} için veri yok.")

    # Footer
    st.markdown("""
        <div class="footer">
            <p>Developed By: Erkan Turgut | © 2025 Tüm hakları saklıdır.</p>
            <p><a href="mailto:turguterkan55@gmail.com">İletişim</a> | <a href="https://github.com/Erkan3034">GitHub</a></p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()