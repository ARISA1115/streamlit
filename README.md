# streamlit

## セットアップ手順

### 1. 仮想環境を作成
```bash
python3 -m venv myenv
```

### 2. 仮想環境を有効化する
以下のコマンドで仮想環境を有効化します：
- Windowsの場合
```bash
myenv\Scripts\activate
```

- Mac\Linuxの場合
```bash
source myenv/bin/activate
```

仮想環境が有効になるとプロンプトの先頭に(myenv)のような表示が出ます。

### 3. 必要なパッケージのインストール
```bash
pip install -r requirements.txt
```

### 4. アプリケーション起動
以下のコマンドでStreamlitアプリを起動します：
```bash
streamlit run app.py
```
ブラウザが自動で開かない場合は、`http://localhost:8501/`にアクセスしてください。

### 5. 仮想環境の終了
以下のコマンドで仮想環境を終了します：
```bash
deactivate
```

## ディレクトリ構成
streamlit-app/
├── .gitignore
├── app.py               
├── README.md
└── requirements.txt
