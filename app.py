import urllib.parse
import streamlit as st

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(
    page_title="StoreAnalyzer | تأجير منصة تحليل المتاجر",
    page_icon="⚡",
    layout="centered",
)

# 2. الهيدر الرئيسي
st.title("⚡ StoreAnalyzer")
st.subheader(
    "المنصة البرمجية الاحترافية لتتبع المنافسين وتحليل المتاجر الإلكترونية"
)

# شريط السعر والتأجير
st.success("💡 متاحة للتأجير الحصري للشركات والمتاجر بـ 200$ شهرياً")

st.markdown("---")

# 3. صندوق مراسلة وتواصل مباشر
st.markdown("### ✉️ تواصل مباشر مع المالك لحجز المنصة")
st.write(
    "اكتب رسالتك أو اسم شركتك بالأسفل، ثم اضغط زر الإرسال لتفتح معك رسالة الجيميل"
    " جاهزة فوراً:"
)

# خانة كتابة الرسالة من قبل الزائر
visitor_message = st.text_area(
    "رسرتك / اسم متجرك / استفسارك:",
    placeholder=(
        "اكتب هنا مثلاً: السلام عليكم، أرغب في تأجير منصة StoreAnalyzer لمتجري..."
    ),
    height=120,
)

# تجهيز رابط الجيميل الديناميكي (ياخد رسالة الزائر ويحطها في الإيميل أوتوماتيك)
default_body = (
    "السلام عليكم، أرغب في الاشتراك وتأجير منصة StoreAnalyzer بـ 200$ شهرياً."
)
message_to_send = (
    visitor_message if visitor_message.strip() else default_body
)
encoded_body = urllib.parse.quote(message_to_send)

gmail_direct_url = (
    "https://mail.google.com/mail/?view=cm&fs=1&to=Anassadek5535@gmail.com&su=طلب%20إيجار%20منصة%20StoreAnalyzer&body="
    + encoded_body
)

# أزرار التواصل المباشر السريعة
col1, col2 = st.columns(2)

with col1:
  st.link_button(
      "✉️ إرسال عبر الجيميل فوراً",
      gmail_direct_url,
      use_container_width=True,
  )

with col2:
  st.link_button(
      "💬 تواصل عبر تيليجرام (@Anas55355)",
      "https://t.me/Anas55355",
      use_container_width=True,
  )

st.markdown("---")

# 4. نبذة سريعة عن الأداة للعميل (تبين له القيمة)
st.markdown("### 🌟 ماذا ستستلم عند إيجار المنصة؟")
st.write("✔️ **رصد أسعار المنافسين:** متابعة لحظية لتغيرات أسعار السوق.")
st.write("✔️ **صائد المنتجات:** كشف المنتجات الرابحة قبل الجميع.")
st.write("✔️ **حاسبة الأرباح:** حساب دقيق لصافي المكسب وعائد الإعلانات.")
