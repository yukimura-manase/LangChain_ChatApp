# Streamlit と LangChain で作成する 最低限の ChatApp

## アプリ概要 (Summary)

- Streamlit と LangChain & OpenAI-API を使って、ChatGPT の Clone アプリを作成します。

- Streamlit とは、Web アプリをすばやく作成・共有するための Python ベースの OSS フレームワークです。

- LangChain とは、ChatGPT をはじめとする LLM を利用したアプリケーションの開発支援を目的としたライブラリです。

- LangChain を利用することで、特定の文書に対する質問応答機能を持つアプリや、チャットボット、エージェント（自己決定的な行動をとる AI）などを簡単に行うことができます。

- LangChain でできること、一部抜粋。

  - LLM の呼び出しができる

  - Youtube, WEB サイト, PDF などからコンテンツを取得する(データ抽出)

  - 取得したコンテンツを Vector Store に格納する

  - 各種データベースなどとの接続もサポート

  - 取得したコンテンツの要約を行う

## 環境構築方法(初期 setup)

- 環境構築方法を説明します。

### OpenAI アカウント (API Key)の取得

- ChatGPT を活用した AI アプリ開発に必要な API を準備しましょう。

```bash
export OPENAI_API_KEY="sk-..."
```

### OpenAI ライブラリのインストール

```bash
pip install openai
```

### Streamlit のインストール

```bash
pip install streamlit

# 正常にインストールされたことの確認
streamlit hello
```

### LangChain のインストール

```bash
pip install langchain
```

## プロジェクトを立ち上げる方法

```bash

# プロジェクトに移動する
cd LangChain_ChatApp

# main.py を実行する
streamlit run main.py
```

## 【参考・引用】

1. [つくりながら学ぶ！AI アプリ開発入門 - LangChain & Streamlit による ChatGPT API 徹底活用](https://zenn.dev/ml_bear/books/d1f060a3f166a5)
