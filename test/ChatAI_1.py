import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage, # システムメッセージ 
    HumanMessage, # 人間の質問 
    AIMessage, # ChatGPTの返答
)


def main():
    
    ### NOTE ###
    # ChatGPT APIのtemperatureパラメータは、モデルが生成するテキストの"ランダム性"や"多様性"を制御します。
    # 値は0から1までの範囲で設定できます。
    llm = ChatOpenAI(temperature=0) # temperature 0 で ChatGPT Instance を作成する

    # Streamlit の Page設定
    st.set_page_config(
        page_title="My Great ChatGPT", # ページのタイトル
        page_icon="🤗" # ページのアイコン
    )
    # Streamlit の Header 設定
    st.header("My Great ChatGPT 🤗")

    # チャット履歴の初期化
    if "messages" not in st.session_state:
        # NOTE: Streamlit の session_state は、アプリケーションの状態を管理するための機能です
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]

    # ユーザーの入力を監視する => チャットUIでユーザーのインプットの入力を受け付ける
    if user_input := st.chat_input("聞きたいことを入力してね！"):
        # ユーザーからの入力・Msg を 追加する
        st.session_state.messages.append(HumanMessage(content=user_input))

        # ChatGPT が返答を生成している間に表示するスピナー(Loading)
        with st.spinner("ChatGPT is typing ..."):
            response = llm(st.session_state.messages)
        
        # AIモデルからの回答・Msg を追加する
        st.session_state.messages.append(AIMessage(content=response.content))

    # チャット履歴の表示
    messages = st.session_state.get('messages', [])
    for message in messages:
        if isinstance(message, AIMessage):
            with st.chat_message('assistant'):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message('user'):
                st.markdown(message.content)
        else:  # isinstance(message, SystemMessage):
            st.write(f"System message: {message.content}")


if __name__ == '__main__':
    main()



### 
# 動作確認の方法
# 次のコマンドを実行する
# LangChain_ChatApp % cd test
# test % streamlit run ChatAI_1.py 
# 上記、コマンドを実行後に、ターミナルの標準出力を確認する！
## 
