
import streamlit as st
import openai

# --- OpenAI API Key ---
openai.api_key = st.secrets["OPENAI_API_KEY"]

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="감정 응원 챗봇", page_icon="😊", layout="centered")

st.title("😊 오늘의 감정, 함께 나눠요!")
st.write("지금 느끼는 감정을 선택하고, 간단히 상황을 적어주세요. 힘이 되는 응원과 격려를 전해드릴게요!")

# --- 감정 선택 ---
st.subheader("지금 내 기분은?")
emotion_options = {
    "🙂 행복해요": "행복",
    "😢 슬퍼요": "슬픔",
    "😡 화가나요": "화남",
    "😟 걱정돼요": "걱정"
}
selected_emoji = st.radio("감정을 선택하세요", list(emotion_options.keys()), horizontal=True)
emotion_text = emotion_options[selected_emoji]

# --- 상황 입력 ---
situation = st.text_area("조금 더 이야기해 줄래요?", placeholder="예: 친구랑 다퉈서 속상해요...")

if st.button("응원해줘!"):
    if situation.strip():
        with st.spinner("긍정의 힘을 모으는 중... ✨"):
            prompt = f"""
            너는 따뜻하고 다정한 초등학교 담임선생님이야.
            아이가 {emotion_text} 라고 느끼고 있어. 이렇게 이야기했어: "{situation}"
            이 아이를 위로하고 용기와 자신감을 줄 수 있는 한 문단의 긍정확언을 만들어줘.
            말투는 따뜻하고 존중하며, 초등학생이 이해할 수 있게 쉽게 말해줘.
            """
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": "You are a kind and encouraging teacher."},
                          {"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.8
            )
            reply = response["choices"][0]["message"]["content"]
            st.success("응원 메시지")
            st.write(reply)
    else:
        st.warning("상황을 조금만 더 적어주세요!")
