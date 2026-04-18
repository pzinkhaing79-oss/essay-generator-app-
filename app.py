import streamlit as st
import google.generativeai as genai
import docx
from docx.shared import Mm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# ---------------- UI DESIGN ---------------- #
st.set_page_config(page_title="Professional Essay Generator", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { background-color: #d35400; color: white; border-radius: 5px; height: 3em; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("✍️ Mine Free Myanmar Essay & Emailer")
st.write("ပြိုင်ပွဲစည်းကမ်းချက်များအတိုင်း (A4, 25mm Margin, 12pt, Justified) စာစီစာကုံးကို အလိုအလျောက် ရေးသားပေးပါမည်။")

# ---------------- CONFIGURATION ---------------- #
api_key = st.text_input("🔑 Gemini API Key ကို ထည့်ပါ", type="password")

# ပြိုင်ပွဲဝင် ခေါင်းစဉ် ၄ ခု
topics = [
    "ကျွန်ုပ်တို့၏ လူမှုပတ်ဝန်းကျင်တွင် မြေမြှုပ်မိုင်းများ ဆက်လက်အသုံးပြုမှုကို မည်သို့တားဆီးကြမည်နည်း။",
    "မိမိတို့ဒေသအတွင်း လက်နက်ကိုင်အဖွဲ့အစည်းများ၏ မိုင်းအသုံးပြုမှုကို အဆုံးသတ်နိုင်ရန် လူထုမှလုပ်ဆောင်နိုင်သည့် အဆင့်ဆင့်သော လုပ်ငန်းစဉ်များ။",
    "ကျွန်ုပ်တို့၏ လူမှုအသိုင်းအဝိုင်းကို မြေမြှုပ်မိုင်းကင်းစင်သောဇုန်အဖြစ် မည်သို့ဖော်ဆောင်မည်နည်း။",
    "မြေမြှုပ်မိုင်းကြောင့် ထိခိုက်ရသူများအတွက် ပိုမိုကောင်းမွန်သော လူမှုဘဝဖော်ဆောင်ပေးနိုင်ရန် မိမိတို့လူထုမှ မည်သို့သောလုပ်ငန်းစဉ်များ ဆောင်ရွက်နိုင်သနည်း။"
]
selected_topic = st.selectbox("စာစီစာကုံး ခေါင်းစဉ်ရွေးချယ်ပါ", topics)

# Email Settings
st.subheader("📧 Auto Email ပေးပို့ရန် အချက်အလက်")
sender_email = st.text_input("သင့် Gmail")
app_password = st.text_input("Gmail App Password", type="password")
target_email = "ArtContest@minefreemyanmar.info" #

# ---------------- FUNCTIONS ---------------- #
def create_docx(text, title):
    doc = docx.Document()
    
    # Page setup (A4 Size)
    section = doc.sections[0]
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    
    # Margins (25mm ပတ်လည်)
    section.left_margin = Mm(25)
    section.right_margin = Mm(25)
    section.top_margin = Mm(25)
    section.bottom_margin = Mm(25)
    
    # Title (Center Alignment)
    h = doc.add_paragraph()
    h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_h = h.add_run(title)
    run_h.font.size = Pt(14)
    run_h.font.bold = True
    
    # Body Text (Justified & 12pt)
    paragraphs = text.split('\n')
    for p_text in paragraphs:
        if p_text.strip():
            p = doc.add_paragraph()
            # အနောက်က စာကြောင်းညီအောင် ညှိခြင်း
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY 
            run = p.add_run(p_text.strip())
            run.font.size = Pt(12)
            # စာပိုဒ်အစကို Space ချန်ခြင်း
            p.paragraph_format.first_line_indent = Mm(12.7) 

    file_stream = io.BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)
    return file_stream

def send_email_with_attach(sender, pwd, receiver, subject, content, file_stream):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(content, 'plain'))
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(file_stream.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="Essay_Submission.docx"')
    msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, pwd)
    server.send_message(msg)
    server.quit()

# ---------------- MAIN PROCESS ---------------- #
if st.button("စာစီစာကုံး စတင်ရေးသားမည်"):
    if not api_key:
        st.error("API Key ထည့်ပေးပါ")
    else:
        try:
            with st.spinner("AI မှ ပညာရှင်တစ်ယောက်ကဲ့သို့ ရေးသားနေပါသည်..."):
                genai.configure(api_key=api_key)
                # အရင်က gemini-1.5-pro သို့မဟုတ် gemini-1.5-flash နေရာတွင် 
# အောက်ပါအတိုင်း gemini-3-flash-preview သို့ ပြောင်းလဲပါ
           model = genai.GenerativeModel("gemini-3-flash-preview")

                
model 
                
                # စည်းကမ်းချက်များအတိုင်း Prompt ပေးခြင်း
                prompt = f"""
                ခေါင်းစဉ်- "{selected_topic}"
                
                သင်သည် မြန်မာစာပေ ကျွမ်းကျင်သော ပညာရှင်တစ်ဦး ဖြစ်သည်။ အောက်ပါ စည်းကမ်းချက်များအတိုင်း စာစီစာကုံးကို မြန်မာဘာသာဖြင့် ရေးပေးပါ-
                ၁။ AI ရေးထားမှန်း မသိစေရန် သဘာဝကျကျနှင့် စိတ်လှုပ်ရှားဖွယ် ရေးသားပါ။ (Bullet points များ မသုံးပါနှင့်)
                ၂။ အောက်ပါအချက် ၃ ချက်ကို စာပိုဒ်များအတွင်း မဖြစ်မနေ ထည့်သွင်းပါ-
                   - လက်တွေ့ကျကျ အကောင်အထည်ဖော်မည့် အကြံပြုချက်များ။
                   - အကောင်အထည်ဖော်ရာတွင် ကြုံတွေ့နိုင်သည့် အခက်အခဲများ။
                   - ထိုအခက်အခဲများကို ကျော်လွှားမည့် နည်းလမ်းများ။
                ၃။ စာလုံးရေသည် A4 စာရွက်ဖြင့် ၁.၅ မျက်နှာမှ ၃ မျက်နှာအတွင်း ရှိရမည်။
                """
                
                response = model.generate_content(prompt)
                essay_text = response.text
                
                # Word ဖိုင် ဖန်တီးခြင်း
                docx_output = create_docx(essay_text, selected_topic)
                
                st.success("စာစီစာကုံး ရေးသားပြီးပါပြီ!")
                st.text_area("အကြမ်းဖျင်းဖတ်ရှုရန်", essay_text, height=300)
                
                # Download Button
                st.download_button(
                    label="📥 Word ဖိုင် ဒေါင်းလုဒ်ဆွဲရန်",
                    data=docx_output,
                    file_name="Mine_Free_Myanmar_Essay.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
                
                # Auto Email Sending
                if sender_email and app_password:
                    docx_output.seek(0) # Reset stream
                    send_email_with_attach(
                        sender_email, app_password, target_email, 
                        f"Entry for Essay Contest: {selected_topic[:30]}...", 
                        "စာစီစာကုံးပြိုင်ပွဲအတွက် ပူးတွဲဖိုင်ဖြင့် ပေးပို့အပ်ပါသည်။", 
                        docx_output
                    )
                    st.success(f"Email ကို {target_email} သို့ အလိုအလျောက် ပေးပို့ပြီးပါပြီ!")

        except Exception as e:
            st.error(f"Error: {str(e)}")
