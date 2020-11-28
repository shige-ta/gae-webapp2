# gae-webapp2
Google app engine webapp2 RESTAPIサンプル python2 ver.


```bash
mkdir lib
pip install -t lib -r requirements.txt
```

gcloudコマンドインストール
https://cloud.google.com/sdk/docs/install?hl=JA

```bash
gcloud init
```
googleアカウント指定
GCPプロジェクト指定
タイムゾーン指定(asia-northeast1)

```bash
gcloud app deploy
```
ドメイン情報等確認 y


```bash
curl https://〇〇〇〇〇〇〇〇.an.r.appspot.com/post -X POST -H "Content-Type: application/json" --data '{"key": "value"}'
```