import streamlit as st
import base64, random
def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
if pdf_file is not None:
    # with st.spinner('Uploading your Resume....'):
    #     time.sleep(4)
    save_image_path = 'D:/Yash Python/Streamlit_Trials/Pdfs/' + pdf_file.name
    with open(save_image_path, "wb") as f:
        f.write(pdf_file.getbuffer())
    show_pdf(save_image_path)