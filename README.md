# line_fastapi

●node.js は扱いに不慣れなため、一旦python : FAST APIを作成する。

●使用環境
・サーバー側システム：FAST API
・アプリ登録：deta space　　＊Herokuが有料となったため。

① FAST APIの動作確認
★参考サイト
https://qiita.com/buntako/items/2ed3700e14060cc03a90
https://qiita.com/kakiuchis/items/80f6239f6319066ee18d

・VScode開く
・ターミナル開く
・space login : ログイン
　new token 41char の方
・space new  : 新しいdata.space用のプログラム作成
　ファイル名入力
　→ .space  /  meta / READMEなど色々作られる。
・リンク先に従って、main.py requrements.txt 作成
・space push : デプロイ

※デフォルトでは非公開設定になっているためログインを求められる。
　Spacefileに public:trueの記載が必要。

② flaskのver : LINE動作の確認

★参考サイト
https://qiita.com/Threen/items/3a5162b3002d2c77c63b
https://cacaca-blog.vercel.app/blogs/18dbb090-b297-11ed-802c-67a3e1f71abf


●良い例
https://detaspaceline3-1-j6456234.deta.app/
https://detaspaceline3-1-j6456234.deta.app/callback/

×悪い例
https://20230625_linebot-1-t1058518.deta.app
https://20230625_linebot-1-t1058518.deta.app/callback


※ 登録名でアンダーバーを使うとLINEdeveloperでerrorが発生する。
※ error : レスポンスerror
LINE DevelopesのWebhook URLの接続確認でエラーが出る件について -
Qiita![image](https://github.com/shohei0990/line_fastapi/assets/88127457/90dce221-4f4b-4b9a-9f44-b80269f53e63)
