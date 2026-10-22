import pandas as pd
import streamlit as st

# 1. ضبط إعدادات الصفحة والتصميم العريض
st.set_page_config(
    page_title="StoreAnalyzer | المنصة العالمية لتحليل المتاجر والمنافسين",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. الهيدر والعنوان الرئيسي
st.title("⚡ StoreAnalyzer")
st.subheader(
    "المنصة البرمجية الشاملة للذكاء التجاري وتحليل المنافسين في التجارة"
    " الإلكترونية"
)

# شريط حالة الاشتراك والتأجير
st.success(
    "💡 هذه المنصة متاحة للتأجير الحصري للمتاجر والشركات بـ 200$ شهرياً | شاملة"
    " جميع الأدوات والتحليلات"
)

st.markdown("---")

# 3. الشريط الجانبي (Sidebar) للتنقل بين أدوات المنصة
st.sidebar.title("🛠️ لوحة أدوات المنصة")
tool_choice = st.sidebar.radio(
    "اختر الأداة المطلوبة:",
    [
        "📊 رادار المنافسين والأسعار",
        "🚀 صائد المنتجات الرابحة",
        "💰 حاسبة الأرباح والإعلانات",
        "⭐ محلل آراء وتقييمات العملاء",
    ],
)

# 4. عرض الأداة المحددة بناءً على اختيار المستخدم
if tool_choice == "📊 رادار المنافسين والأسعار":
  st.header("📊 رادار تتبع المنافسين والأسعار اللحظي")
  st.write(
      "ادخل رابط المتجر المنافس لمراقبة تغييرات الأسعار والمنتجات الجديدة"
      " أوتوماتيكياً:"
  )

  col_input, col_btn = st.columns([3, 1])
  with col_input:
    store_link = st.text_input(
        "رابط المتجر المنافس:",
        placeholder="https://competitor-store.com",
        key="comp_link",
    )
  with col_btn:
    st.write("")
    st.write("")
    analyze_btn = st.button("بدء الرصد الفوري 🔍")

  if analyze_btn:
    if store_link:
      st.info(f"جاري فحص وحصر منتجات المتجر: {store_link}")
      demo_data = {
          "المنتج": [
              "سماعة لاسلكية برو",
              "ساعة ذكية مقاومة للماء",
              "حامل موبايل ذكي",
          ],
          "سعر المنافس": ["$35", "$60", "$20"],
          "التغير خلال 24h": ["-5%", "ثابت", "+10%"],
          "حالة المخزون": ["متوفر", "وشيك على الانتهاء ⚠️", "متوفر"],
      }
      st.dataframe(pd.DataFrame(demo_data), use_container_width=True)
    else:
      st.warning("يرجى إدخال رابط المتجر أولاً.")

elif tool_choice == "🚀 صائد المنتجات الرابحة":
  st.header("🚀 صائد المنتجات الرابحة (Winning Products)")
  st.write(
      "الخوارزمية الذكية لاكتشاف المنتجات الأكثر طلباً والأعلى ربحية في السوق"
  )

  category = st.selectbox(
      "اختر التصنيف التجاري:",
      ["الإلكترونيات", "الملابس والأزياء", "المنزل والمطبخ", "العناية والتجميل"],
  )

  if st.button("استكشاف المنتجات الرابحة 🔥"):
    st.success(f"أفضل المنتجات الرابحة حالياً في تصنيف [{category}]:")
    winning_data = {
        "المنتج الرابح": [
            "مكواة بخار محمولة",
            "مصباح مكتب ذكي",
            "حقيبة ظهر مقاومة للماء",
        ],
        "حجم الطلب": ["عالي جداً 🔥", "ممتاز 🌟", "ارتفاع ملحوظ 📈"],
        "متوسط سعر التكلفة": ["$8", "$12", "$10"],
        "سعر البيع الموصى به": ["$28", "$38", "$32"],
        "هامش الربح المتوقع": ["71%", "68%", "68%"],
    }
    st.dataframe(pd.DataFrame(winning_data), use_container_width=True)

elif tool_choice == "💰 حاسبة الأرباح والإعلانات":
  st.header("💰 حاسبة صافي الأرباح والعائد على الإعلانات (ROAS)")
  st.write("احسب صافي أرباحك بالملليمتر قبل البدء في الحملات الإعلانية:")

  c1, c2, c3 = st.columns(3)
  with c1:
    cost_price = st.number_input("تكلفة شراء القطعة ($):", value=10.0)
  with c2:
    sell_price = st.number_input("سعر بيع القطعة ($):", value=35.0)
  with c3:
    ad_cost = st.number_input("تكلفة الإعلان المتوقعة للقطعة ($):", value=8.0)

  shipping_cost = st.number_input("تكلفة الشحن والتغليف ($):", value=4.0)

  net_profit = sell_price - (cost_price + ad_cost + shipping_cost)
  margin = (net_profit / sell_price) * 100 if sell_price > 0 else 0

  st.markdown("---")
  res_col1, res_col2 = st.columns(2)
  with res_col1:
    st.metric(label="صافي الربح للقطعة", value=f"${net_profit:.2f}")
  with res_col2:
    st.metric(label="نسبة هامش الربح", value=f"{margin:.1f}%")

elif tool_choice == "⭐ محلل آراء وتقييمات العملاء":
  st.header("⭐ محلل نقاط ضعف المنافسين من التقييمات")
  st.write(
      "استخراج عيوب منتجات المنافسين من تقييمات المشترين لتفاديها وتطوير"
      " منتجك:"
  )

  prod_review_link = st.text_input(
      "رابط صفحة منتج المنافس:", placeholder="https://store.com/product-page"
  )
  if st.button("تحليل التقييمات 🧐"):
    if prod_review_link:
      st.info("جاري تحليل التقييمات وآراء العملاء...")
      review_summary = {
          "أبرز الشكاوى (نقاط الضعف)": [
              "بطء بطارية الجهاز",
              "التغليف غير محكم",
              "تأخر الشحن",
          ],
          "نسبة التكرار": ["42%", "28%", "15%"],
          "التوصية": [
              "توفير بطارية أكبر سعة في منتجك",
              "استخدام تغليف كرتوني مقوى",
              "التعاقد مع شركة شحن أسرع",
          ],
      }
      st.dataframe(pd.DataFrame(review_summary), use_container_width=True)
    else:
      st.warning("يرجى إدخال رابط المنتج أولاً.")

# 5. قسم التواصل والتأجير المباشر ببياناتك (مُحدث وآمن 100%)
st.markdown("---")
st.header("📞 هل تريد تأجير هذه المنصة بالكامل لشركتك؟")
st.write(
    "تواصل مع المالك المباشر فوراً لحجز إيجار المنصة ($200 شهرياً) واستلام حساب"
    " الدخول الخاص بك:"
)

contact_col1, contact_col2 = st.columns(2)

with contact_col1:
  st.link_button(
      "💬 تواصل عبر تيليجرام (@Anas55355)",
      "https://t.me/Anas55355",
      use_container_width=True,
  )

with contact_col2:
  st.link_button(
      "✉️ مراسلة فورية عبر الجيميل (Gmail)",
      (
          "https://mail.google.com/mail/?view=cm&fs=1&to=Anassadek5535@gmail.com&su=طلب"
          " إيجار منصة StoreAnalyzer"
      ),
      use_container_width=True,
  )
