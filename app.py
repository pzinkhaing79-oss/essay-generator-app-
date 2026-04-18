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

# ---------------- ၁။ App ၏ မျက်နှာစာ ဒီဇိုင်း ---------------- #
st.set_page_config(page_title="Professional Essay Generator", layout="centered")
st.markdown("""
    <style>
    .main { background-color: #fdfcfb; }
    .stButton>button { 
        background-color: #d35400; 
        color: white; 
        border-radius: 8px; 
        height: 3.5em; 
        width: 100%;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✍️ Mine Free Myanmar Essay Creator")
st.info("ဤ App သည် ပြိုင်ပွဲဝင် စည်းကမ်းချက်များဖြစ်သော A4၊ Margin 25mm၊ Font 12pt နှင့် Justified စနစ်တို့ဖြင့် Word ဖိုင်ကို တိုက်ရိုက် ထုတ်ပေးမည်ဖြစ်ပါသည်။")

# ---------------- ၂။ Configuration & Inputs ---------------- #
api_key = st.text_input("🔑 Google AI Studio API Key ကို ထည့်ပါ", type="password")

# ပြိုင်ပွဲဝင် ခေါင်းစဉ်များ
topics = [
    "ကျွန်ုပ်တို့၏ လူမှုပတ်ဝန်းကျင်တွင် မြေမြှုပ်မိုင်းများ ဆက်လက်အသုံးပြုမှုကို မည်သို့တားဆီးကြမည်နည်း။",
    "မိမိတို့ဒေသအတွင်း လက်နက်ကိုင်အဖွဲ့အစည်းများ၏ မိုင်းအသုံးပြုမှုကို အဆုံးသတ်နိုင်ရန် လူထုမှလုပ်ဆောင်နိုင်သည့် အဆင့်ဆင့်သော လုပ်ငန်းစဉ်များ။",
    "ကျွန်ုပ်တို့၏ လူမှုအသိုင်းအဝိုင်းကို မြေမြှုပ်မိုင်းကင်းစင်သောဇုန်အဖြစ် မည်သို့ဖော်ဆောင်မည်နည်း။",
    "မြေမြှုပ်မိုင်းကြောင့် ထိခိုက်ရသူများအတွက် ပိုမိုကောင်းမွန်သော လူမှုဘဝဖော်ဆောင်ပေးနိုင်ရန် မိမိတို့လူထုမှ မည်သို့သောလုပ်ငန်းစဉ်များ ဆောင်ရွက်နိုင်သနည်း။"
]
selected_topic = st.selectbox("စာစီစာကုံး ခေါင်းစဉ်ရွေးချယ်ပါ", topics)

st.subheader("📧 Email ပို့ရန် အချက်အလက် (Optional)")
col1, col2 = st.columns(2)
with col1:
    sender_email = st.text_input("သင့် Gmail လိပ်စာ")
with col2:
    app_password = st.text_input("Gmail App Password", type="password", help="Gmail Settings ထဲမှ ရယူထားသော စကားလုံး ၁၆ လုံးပါ Code")

target_email = "ArtContest@minefreemyanmar.info" #

# ---------------- ၃။ Word ဖိုင် ဖန်တီးသည့် Function ---------------- #
def create_docx(text, title):
    doc = docx.Document()
    
    # A4 Size Setup
    section = doc.sections[0]
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    
    # Margins 25mm ပတ်လည်
    section.left_margin = Mm(25)
    section.right_margin = Mm(25)
    section.top_margin = Mm(25)
    section.bottom_margin = Mm(25)
    
    # Title - Center Aligned
    h = doc.add_paragraph()
    h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_h = h.add_run(title)
    run_h.font.size = Pt(14)
    run_h.font.bold = True
    
    doc.add_paragraph("") # Space တစ်ကြောင်းခြား

    # Body Text - Justified (စာကြောင်းအနောက်ညီစေရန်)
    paragraphs = text.split('\n')
    for p_text in paragraphs:
        if p_text.strip():
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY # ဤနေရာတွင် စာကြောင်းညီအောင် ညှိသည်
            run = p.add_run(p_text.strip())
            run.font.size = Pt(12) #
            p.paragraph_format.first_line_indent = Mm(12.7) # စာပိုဒ်အစကို Space ချန်သည်

    file_stream = io.BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)
    return file_stream

# ---------------- ၄။ Email ပို့သည့် Function ---------------- #
def send_essay_email(sender, pwd, receiver, subject, file_stream):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText("စာစီစာကုံးပြိုင်ပွဲအတွက် ပူးတွဲပါ Word ဖိုင်ဖြင့် ပေးပို့အပ်ပါသည်။", 'plain'))
        
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file_stream.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="Essay_Entry.docx"')
        msg.attach(part)
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, pwd)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Email ပို့ရာတွင် အမှားအယွင်းရှိပါသည်: {str(e)}")
        return False

# ---------------- ၅။ စာစီစာကုံး ရေးသားမည့် Process ---------------- #
if st.button("စာစီစာကုံး စတင်ရေးသားမည်"):
    if not api_key:
        st.warning("ကျေးဇူးပြု၍ API Key အရင်ထည့်ပေးပါ")
    else:
        try:
            with st.spinner("Gemini 3 Flash Preview မှ ပညာရှင်တစ်ယောက်ကဲ့သို့ ရေးသားနေပါသည်..."):
                genai.configure(api_key=api_key)
                # Gemini 3 Flash Preview အသုံးပြုခြင်း
                model = genai.GenerativeModel("gemini-3-flash-preview")
                
                # စည်းကမ်းချက်များနှင့်အညီ Prompt ပေးခြင်း
                prompt = f"""
                မင်းက မြန်မာစာပေနဲ့ လူမှုရေးရာ ကျွမ်းကျင်တဲ့ ပညာရှင်တစ်ယောက် ဖြစ်တယ်။
                ခေါင်းစဉ်- "{selected_topic}"
                
                အောက်ပါ စည်းကမ်းချက်အတိုင်း စာစီစာကုံး ရေးသားပါ-
                ၁။ AI ရေးထားမှန်း မသိသာစေရန် သဘာဝကျကျနှင့် ရသပါအောင် ရေးပါ။ Bullet points လုံးဝ မသုံးရ။
                ၂။ အချက်အလက် (၃) ချက်ကို စာပိုဒ်များအတွင်း ထည့်ရေးပါ-
                   - လက်တွေ့ကျသော အကြံပြုချက်များ။
                   - ကြုံတွေ့နိုင်သော အခက်အခဲများ။
                   - ထိုအခက်အခဲများကို ကျော်လွှားမည့် နည်းလမ်းများ။
                ၃။ စာလုံးရေသည် A4 စာရွက်ဖြင့် ၁.၅ မျက်နှာမှ ၃ မျက်နှာအတွင်း ရှိရမည်။
                ၄။ မြန်မာဘာသာဖြင့်သာ ရေးသားပါ။
                """
                
                response = model.generate_content(prompt)
                essay_content = response.text
                
                # Word ဖိုင် ထုတ်ယူခြင်း
                word_file = create_docx(essay_content, selected_topic)
                
                st.success("စာစီစာကုံး ရေးသားမှု အောင်မြင်ပါသည်!")
                st.text_area("ရေးသားထားသော စာသားများ (Preview):", essay_content, height=400)
                
                # Download ခလုတ်
                st.download_button(
                    label="📥 Word ဖိုင် ဒေါင်းလုဒ်လုပ်ရန်",
                    data=word_file,
                    file_name="Mine_Free_Myanmar_Essay.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
                
                # Email အလိုအလျောက် ပို့ခြင်း
                if sender_email and app_password:
                    word_file.seek(0)
                    if send_essay_email(sender_email, app_password, target_email, f"Essay Contest Entry: {selected_topic[:30]}", word_file):
                        st.success(f"Email ကို {target_email} သို့ ပေးပို့ပြီးပါပြီ!")

        except Exception as e:
            # Quota Error (429) ကို ကိုင်တွယ်ခြင်း
            if "429" in str(e):
                st.error("အသုံးပြုမှု အကြိမ်ရေ ကန့်သတ်ချက် ပြည့်သွားပါပြီ။ ၁ မိနစ်ခန့် စောင့်ပြီးမှ ပြန်လည် ကြိုးစားပါ။")
            else:
                st.error(f"Error ဖြစ်ပေါ်နေပါသည်: {str(e)}")
