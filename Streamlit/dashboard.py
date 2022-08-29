import imp
from urllib import robotparser
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as pyoff
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
from scipy.stats import pearsonr

st.set_page_config(
    page_title="Kondisi Perikanan Indonesia",
    layout="wide"
)
row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.title('Kondisi Perikanan Indonesia')
with row0_2:
    st.text("")
    st.subheader('Streamlit App by [Angga Chandra Putra](https://www.linkedin.com/in/angga-chandra/)')
row1_spacer1, row1_1, row1_spacer2 = st.columns((.1, 3.2, .1))
with row1_1:
    st.markdown("You can find the source code in:")
    st.markdown("[Analisis Pengaruh Produksi Perikanan Terhadap PDB Sektor Perikanan GitHub Repository](https://github.com/UltEng/Fishery-Culvation-Production-Effect-to-Indonesia-Fishery-Sector-GDP-/)")
    
    st.markdown("""
    Indonesia merupakan negara kepulauan dengan wilayah laut yang lebih luas daripada luas daratannya. Luas seluruh wilayah Indonesia dengan jalur laut 12 mil
    adalah lima juta km2 terdiri dari luas daratan 1,9 juta km2, laut teritorial 0,3 juta km2,
    dan perairan kepulauan seluas 2,8 juta km2. Artinya seluruh laut Indonesia berjumlah
    3,1 juta km2 atau sekitar 62 persen dari seluruh wilayah Indonesia. Selain itu,Indonesia
    juga merupakan negara dengan garis pantai terpanjang di dunia dengan jumlah
    panjang garis pantainya sekitar 81.000 km. Luas laut yang besar ini menjadikan
    Indonesia unggul dalam sektor perikanan dan kelautan""")

    st.markdown("""
    Untuk itu pembangunan sektor kelautan dan perikanan sebagai sektor andalan
    utama pembangunan Indonesia merupakan pilihan yang sangat tepat, hal ini
    didasarkan atas potensi yang dimiliki dan besarnya keterlibatan sumber daya manusia
    yang diperkirakan hampir 12.5 juta orang terlibat di dalam kegiatan perikanan.
    Di samping itu juga didukung atas suksesnya pembangunan perikanan di negara lain,
    seperti Islandia, Norwegia, Thailand, China dan Korea Selatan yang mampu
    memberikan kontribusi ekonomi nasional yang besar dan mendapatkan dukungan
    penuh secara politik, ekonomi, sosial dan dukungan lintas sektoral. Kontribusi sektor
    perikanan terhadap Produk Domestik Bruto di Islandia sebesar 65%, Norwegia 25%
    """)

    st.markdown("""
    Sehingga ingin diketahui lebih jauh bagaimana pengaruh volume produksi perikanan budidaya
    , luas lahan budidaya, jumlah rumah tangga perikanan, jumlah angka konsumsi ikan, volume
    ekspor, volume impor, nilai USD Impor, dan nilai USD Ekspor tehadap nilai produksi perikanan budidaya
    bagaimana pengaruh nilai produksi perikanan budidaya terhadap Produk Domestik Bruto sektor 
    Perikanan
    """)
    
    st.markdown("""
    Asumsi Awal
    * Terdapat korelasi baik kuat maupun lemah volume produksi perikanan budidaya, luas lahan budidaya, jumlah rumah tangga perikanan, jumlah angka konsumsi ikan, volume
    ekspor, volume impor, nilai USD Impor, dan nilai USD Ekspor tehadap nilai produksi perikanan
    * Terdapat hubungan erat antara nilai produksi perikanan budidaya dengan produk domestik bruto sektor perikanan
    """)

import os
if os.path.dirname(os.getcwd()) == "/app":
    d = "/app/Fishery-Culvation-Production-Effect-to-Indonesia-Fishery-Sector-GDP-"
else:
    d=".."

prod = pd.read_csv(d+"/Streamlit/data/prod.csv")
luas = pd.read_csv(d+"/Streamlit/data/luas_lahan.csv")
rtp = pd.read_csv(d+"/Streamlit/data/rtp.csv")
pdb = pd.read_csv(d+"/Streamlit/data/pdb.csv")
aki = pd.read_csv(d+"/Streamlit/data/aki.csv")
imp = pd.read_csv(d+"/Streamlit/data/imp.csv")
eks = pd.read_csv(d+"/Streamlit/data/eks.csv")

row2_spacer1, row2_1, row2_spacer2 = st.columns((.2, 7.1, .2))
with row2_1:

    st.markdown("Dapat dilihat data yang digunakan di bawah ini (diperoleh dari https://statistik.kkp.go.id/home.php)")

    see_data = st.expander('Produksi Perikanan di Indonesia')
    with see_data:
        st.dataframe(data=prod.reset_index(drop=True))
    
    see_data2 = st.expander('Luas Lahan Budidaya di Indonesia')
    with see_data2:
        st.dataframe(data=luas.reset_index(drop=True))

    see_data3 = st.expander('Rumah Tangga Perikanan di Indonesia')
    with see_data3:
        st.dataframe(data=rtp.reset_index(drop=True))

    see_data4 = st.expander('Angka Konsumsi Ikan di Indonesia')
    with see_data4:
        st.dataframe(data=aki.reset_index(drop=True))

    see_data5 = st.expander('Impor Perikanan Indonesia')
    with see_data5:
        st.dataframe(data=imp.reset_index(drop=True))

    see_data6 = st.expander('Ekspor Perikanan Indonesia')
    with see_data6:
        st.dataframe(data=eks.reset_index(drop=True))

    see_data7 = st.expander('Produk Domestik Bruto Perikanan di Indonesia')
    with see_data7:
        st.dataframe(data=pdb.reset_index(drop=True))
st.text('')
    
row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
with row3_1:
    st.subheader('Perbandingan Produksi Perikanan')
    st.markdown("##### Jenis usaha apa yang menghasilkan produksi dan nilai produksi perikanan terbanyak?")
    st.markdown('')

jum_group = prod.groupby(['Jenis Usaha', 'Tahun']).sum()['Volume Produksi']
jum_group.to_frame()
jum_group = jum_group.reset_index(level= ['Jenis Usaha', 'Tahun'])


prod_group = prod.groupby(['Jenis Usaha', 'Tahun']).sum()['Nilai Produksi']
prod_group.to_frame()
prod_group = prod_group.reset_index(level= ['Jenis Usaha', 'Tahun'])

row4_spacer1, row4_1, row4_spacer2, row4_2, row4_spacer3  = st.columns((.2, 6.4, 0.1, 6.4, .2))
with row4_1:
    
    fig= px.line(jum_group, y = 'Volume Produksi', 
             labels = { 'Volume Produksi': 'Volume'}, 
              x = 'Tahun', color = 'Jenis Usaha',
             title = "Volume Produksi Tahunan Berdasarkan Jenis Usaha")
    fig.layout.plot_bgcolor = "light grey"
    st.plotly_chart(fig, use_container_width=True)

with row4_2:

    
    fig1= px.line(prod_group, y = 'Nilai Produksi', 
             labels = { 'Nilai Produksi': 'Nilai'}, 
              x = 'Tahun', color = 'Jenis Usaha',
             title = "Nilai Produksi Tahunan Berdasarkan Jenis Usaha")
    fig1.layout.plot_bgcolor = "light grey"
    st.plotly_chart(fig1, use_container_width=True)

rtp_group = rtp.groupby(['tahun', 'jenis']).sum()['jumlah RTP']
rtp_group.to_frame()
rtp_group = rtp_group.reset_index(level=['tahun', 'jenis'])

row5_spacer1, row5_1, row5_spacer2, row5_2, row5_spacer3 = st.columns((.2, 6.4, 0.1, 6.4, .2))
with row5_1:
    fig2= px.line(rtp_group, y = 'jumlah RTP', 
             labels = { 'jumlah RTP': 'Jumlah'}, 
              x = 'tahun', color = 'jenis',
             title = "Jumlah RTP Tahunan Berdasarkan Jenis Usaha")
    fig2.layout.plot_bgcolor = "light grey"
    st.plotly_chart(fig2, use_container_width=True)

with row5_2:
    st.markdown("""
    Dapat dilihat walaupun volume produksi perikanan budidaya lebih tinggi dibandingkan 
    tangkap laut dan tangkap PUD
    """)
    st.markdown("""
    nilai produksi perikanan budidaya sendiri masih dekat dengan nilai produksi perikanan 
    tangkap laut sehingga kita tidak bisa hanya melihat dari volume produksinya saja
    """)
    st.markdown("""
    Perlu kita perhatikan juga bahwa walau rumah tangga perikanan budidaya lebih banyak
    dibandingkan rumah tangga perikanan laut dan PUD, rumah tangga perikanan laut akhir-
    akhir ini mengalami kenaikan 
    """)

luas_group = luas.groupby(['tahun', 'provinsi']).sum()['luas lahan']
luas_group.to_frame()
luas_group = luas_group.reset_index(level=['tahun', 'provinsi'])


row6_spacer1, row6_1, row6_spacer2 = st.columns((.2, 7.1, .2))
with row6_1:

    st.subheader('Luas Tahan Budidaya Tiap Provinsi di Indonesia')
    st.markdown("Bagaimana pemanfaatan lahan budidaya provinsi di Indonesia?")

    fig3= px.line(luas_group, y = 'luas lahan', 
             labels = { 'luas lahan': 'Luas'}, 
              x = 'tahun', color = 'provinsi',
             title = "Luas Lahan Budidaya Tahunan Berdasarkan Provinsi")
    fig3.layout.plot_bgcolor = "light grey"
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("""
        * Sumatera memiliki luas lahan budidaya terbesar
        * Pada tahun 2017 - 2020, Jawa Barat mengalami penurunan dan kenaikan dratis mulai dari 
          penurunan dratis pada dari 2017 menuju 2018 lalu 2018 menuju 2019 mengalami kenaikan dratis
          lalu 2019 menuju 2020 mengalami penurunan dratis lagi 
    """)

aki_group = aki.groupby(['Tahun', 'Provinsi']).sum()['Jumlah AKI']
aki_group.to_frame()
aki_group = aki_group.reset_index(level=['Tahun', 'Provinsi'])

row7_spacer1, row7_1, row7_spacer2 = st.columns((.2, 7.1, .2))
with row7_1:

    st.subheader('Angka Konsumsi Ikan Tiap Provinsi di Indonesia')
    st.markdown("Provinsi mana yang memiliki angka konsumsi ikan terbanyak di Indonesia?")

    fig4= px.line(aki_group, y = 'Jumlah AKI', 
             labels = { 'Jumlah AKI': 'Jumlah'}, 
              x = 'Tahun', color = 'Provinsi',
             title = "Jumlah Angka Konsumsi Ikan Tahunan Berdasarkan Provinsi")
    fig4.layout.plot_bgcolor = "light grey"
    st.plotly_chart(fig4, use_container_width=True)
    st.markdown("""
        * Maluku Utara memiliki angka konsumsi ikan terbanyak diikutin dengan Maluku
        * Kalimantan Utara pada tahun awal dapat diketahui karena kalimantan utara merupakan 
          provinsi baru terbentuk akan tetapi di tahun akhir-akhir ini malah mengalami kenaikan dratis
          mendekatin Maluku Utara dan Maluku
        * Secara keseluruhan tiap provinsi Angka Konsumsi Ikan terus meningkat dari tahun ke tahun untuk 
    """)

row8_spacer1, row8_1, row8_spacer2 = st.columns((.2, 7.1, .2))
with row8_1:
    st.subheader('Perbandingan Impor dan Ekspor Perikanan')
    st.markdown("Bagaimana perbandingan impor dan ekspor perikanan di Indonesia?")
    st.markdown('')

row9_spacer1, row9_1, row9_spacer2, row9_2, row9_spacer3  = st.columns((.2, 6.4, 0.1, 6.4, .2))
with row9_1:
    
    fig5= px.line(imp, y = 'Volume Impor', 
             labels = { 'Volume Impor': 'Volume'}, 
              x = 'Tahun',
             title = "Volume Impor Tahunan")
    fig5.layout.plot_bgcolor = "light grey"
    st.plotly_chart(fig5, use_container_width=True)

    fig6= px.line(imp, y = 'Nilai USD Impor', 
             labels = { 'Nilai USD Impor': 'Nilai USD'}, 
              x = 'Tahun',
             title = "Nilai USD Impor Tahunan")
    fig6.layout.plot_bgcolor = "light grey"
    st.plotly_chart(fig6, use_container_width=True)

with row9_2:
    
    fig7= px.line(eks, y = 'Volume Ekspor', 
             labels = { 'Volume Ekspor': 'Volume'}, 
              x = 'Tahun',
             title = "Volume Ekspor Tahunan")
    fig7.layout.plot_bgcolor = "light grey"
    st.plotly_chart(fig7, use_container_width=True)

    fig8= px.line(eks, y = 'Nilai USD Ekspor', 
             labels = { 'Nilai USD Ekspor': 'Nilai USD'}, 
              x = 'Tahun',
             title = "Nilai USD Ekspor Tahunan")
    fig8.layout.plot_bgcolor = "light grey"
    st.plotly_chart(fig8, use_container_width=True)

row10_spacer1, row10_1, row10_spacer2 = st.columns((.2, 7.1, .2))
with row10_1:
    st.markdown("""
    * Terlihat dari perbandingan tersebut indonesia memiliki kekuatan ekspor yang sangat baik
      walaupun volume ekspornya mengalami penurunan volumenya tetap lebih besar dibandingkan
      volume impor.
    * Perbandingan nilai ekspor pun cukup jauh dengan nilai ekspor sekitar 5,21 Billion USD dan
      nilai impor sekitar 500 Million USD
    """)

prod_corr = prod_group[prod_group['Jenis Usaha'] == 'BUDIDAYA']
prod_corr.drop('Jenis Usaha', axis=1, inplace=True)

jum_corr = jum_group[jum_group['Jenis Usaha'] == 'BUDIDAYA']
jum_corr.drop('Jenis Usaha', axis=1, inplace=True)

luas_corr = luas.groupby(['tahun']).sum()['luas lahan']
luas_corr.to_frame()
luas_corr = luas_corr.reset_index(level=['tahun'])
luas_corr = luas_corr.rename({'tahun':'Tahun', 'luas lahan':'Luas Lahan'}, axis =1)

aki_corr = aki.groupby(['Tahun']).sum()['Jumlah AKI']
aki_corr.to_frame()
aki_corr = aki_corr.reset_index(level=0)

rtp_corr = rtp_group[rtp_group['jenis'] == 'Budidaya']
rtp_corr.drop('jenis', axis=1, inplace=True)
rtp_corr = rtp_corr.rename({'tahun':'Tahun','jumlah RTP':'Jumlah RTP'}, axis =1)

corr = prod_corr.merge(jum_corr, on='Tahun').merge(luas_corr, on='Tahun').merge(rtp_corr, on='Tahun').merge(aki_corr, on='Tahun').merge(imp, on= 'Tahun').merge(eks, on= 'Tahun')


row11_spacer1, row11_1, row11_spacer2 = st.columns((.2, 7.1, .2))
with row11_1:

    st.subheader('Uji Korelasi Variabel Lain Terhadap Nilai Produksi Budidaya')
    st.markdown("Variabel mana yang dapat dijadikan prediktor untuk nilai produksi perikanan budidaya?")
    st.markdown('')

    df_corr = corr[['Nilai Produksi', 'Volume Produksi', 'Luas Lahan', 'Jumlah RTP', 'Jumlah AKI',
                'Volume Impor', 'Nilai USD Impor','Volume Ekspor', 'Nilai USD Ekspor' ]].corr()
    x = list(df_corr.columns)
    y = list(df_corr.index)
    z = np.array(df_corr)

    fig9 = px.imshow(z, x=x, y=y, color_continuous_scale='Viridis', aspect="auto")
    fig9.update_traces(text=np.around(z, decimals=2), texttemplate="%{text}")
    fig9.update_xaxes(side="top")
    st.plotly_chart(fig9, use_container_width=True)

    st.markdown('''Dari uji korelasi tersebut dapat dilihat angka konsumsi ikan, nilai USD Ekspor, 
    volume produksi dapat dijadikan prediktor karena memiliki korelasi positif kuat dan juga
    volume ekspor karena memiliki korelasi negatif kuat''')

pdb_group = pdb.groupby('Tahun').sum()['PDB']
pdb_group.to_frame()
pdb_group = pdb_group.reset_index(level=0)

corr1 = prod_corr.merge(pdb_group, on='Tahun')

row12_spacer1, row12_1, row12_spacer2 = st.columns((.2, 7.1, .2))
with row12_1:
    
    st.subheader('Pengaruh Nilai Produksi Budidaya terhadap PDB Sektor Perikanan')
    st.markdown("Seberapa besar korelasi antara nilai produksi budidaya dengan PDB Sektor Perikanan")
    st.markdown('')

    fig10 = px.scatter(corr1, x="Nilai Produksi", y="PDB")
    st.plotly_chart(fig10, use_container_width=True) 

    st.markdown("Pearsons correlation: 0.951")
    st.markdown("Hubungan sangat kuat")

