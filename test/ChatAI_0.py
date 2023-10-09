from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,  # システムメッセージ
    HumanMessage,  # 人間の質問
    AIMessage  # ChatGPTの返答
)

###
# ChatGPT とやり取りする最低限の形 => これだけで、Chatができる！
###

llm = ChatOpenAI()  # ChatGPT APIを呼んでくれる機能
message = "ロボロフスキー・ハムスターとは？"  # あなたの質問をここに書く

messages = [
    SystemMessage(content="絶対に関西弁で返答してください"), # System Message = AIの「キャラ設定」のようなもの 
    HumanMessage(content=message)
]
response = llm(messages)
print(response)

### 
# 動作確認の方法
# 次のコマンドを実行する
# LangChain_ChatApp % cd test
# test % streamlit run ChatAI_0.py 
# 上記、コマンドを実行後に、ターミナルの標準出力を確認する！
## 
