import streamlit as st
#import openai
from openai import OpenAI

client = OpenAI(
  api_key=st.secrets["api_key"],
)  
#openai api key
#openai.api_key = st.secrets["api_key"]

#페이지 레이아웃 설정
st.set_page_config(layout="wide")

#페이지의 메인 이름
st.title("이야기를 꾸며 책 만들기")

# #가로 줄
st.divider()

# #헤더 
st.header("예시 자료")

# #텍스트 출력하기
text = '''
어린이 동물원을 주제로 흥미진진한 이야기를 지어줘
파도치는 바다를 주제로 무서운 이야기를 지워줘
딱지치기, 연날리기, 팽이돌리기 등의 전통놀이를 주제로 따스한 이야기를 지어줘
우주비행사를 주제로 신나는 이야기를 지어줘
'''
st.write(text)
# # st.write("~~~") 의 형태로도 출력 가능

# #링크 넣기
st.markdown("[4단원 9-10차시 '이야기를 꾸며 책 만들기' 146-151쪽](https://youtu.be/ZT5fbYn6ISQ)")

# #학생들이 텍스트 입력하는 곳 만들기
# #조사한 자료를 research에 저장
research = st.text_input("어떤 이야기를 짓고 싶나요? : ")

st.write(research)

st.divider()

# #ChatGPT API 활용하기 response를 불러오는 함수 만들기
# @st.cache_data #반복 수행을 막아줌
def gptapi(persona, user):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content" : persona},
        {"role": "user", "content": user}
    ],
    max_tokens = 1000,
    temperature = 1
    )
    return response.choices[0].message.content

# #prompt 설정하기
persona_prompt1 = '''
너는 초등학교 4학년 학생이야. 수준에 맞게 4장면의 이야기를 지어줘. 장면당 1문장으로 만들어 줘.
'''

# persona_prompt2 = '''
#     너는 역사선생님이야. 학생들이 조사해온 자료를 요악한 내용을 보고, 문제를 만들어줘
#     '''

# #클릭해야 실행되도록 버튼 만들기
if st.button("이야기 만들기"): 
    #복잡한 단계는 나누어 진행하기
    step1 = gptapi(persona_prompt1, research)
    st.write(step1)

#     step2 = gptapi(persona_prompt2, step1)
#     st.write(step2)