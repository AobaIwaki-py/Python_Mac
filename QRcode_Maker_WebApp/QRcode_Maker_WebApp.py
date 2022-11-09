# QRコードを自動生成するWebアプリ
import streamlit as st
import qrcode as qr
from PIL import Image
import numpy as np

st.title('QRコード自動生成アプリ')

url = st.text_input('QRコードを生成したいURL:')
if st.button('QRコード生成'):
    _img = qr.make(url)
    _img.save('qrcode.png')
    img = Image.open('qrcode.png')
    st.image(img)
