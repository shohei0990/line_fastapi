# line_fastapi

●node.js は扱いに不慣れなため、一旦python : FAST APIを作成する。

●使用環境
・サーバー側システム：FAST API
・アプリ登録：deta space　　＊Herokuが有料となったため。

① FAST APIの動作確認
★参考サイト
https://qiita.com/buntako/items/2ed3700e14060cc03a90
https://qiita.com/kakiuchis/items/80f6239f6319066ee18d

・VScode開く<br>
・ターミナル開く<br>
・space login : ログイン<br>
　new token 41char の方（それぞれ）<br>
・space new  : 新しいdata.space用のプログラム作成<br>
　ファイル名入力<br>
　→ .space  /  meta / READMEなど色々作られる。<br>
・リンク先に従って、main.py requrements.txt 作成<br>
・space push : デプロイ<br>


※デフォルトでは非公開設定になっているためログインを求められる。<br>
　Spacefileに public:trueの記載が必要。<br>

② flaskのver : LINE動作の確認<br>

★参考サイト<br>
https://qiita.com/Threen/items/3a5162b3002d2c77c63b<br>
https://cacaca-blog.vercel.app/blogs/18dbb090-b297-11ed-802c-67a3e1f71abf<br>


●良い例<br>
https://detaspaceline3-1-j6456234.deta.app/<br>
https://detaspaceline3-1-j6456234.deta.app/callback/<br>

×悪い例<br>
https://20230625_linebot-1-t1058518.deta.app<br>
https://20230625_linebot-1-t1058518.deta.app/callback<br>


※ 登録名でアンダーバーを使うとLINEdeveloperでerrorが発生する。<br>
※ error : レスポンスerror<br>
LINE DevelopesのWebhook URLの接続確認でエラーが出る件について -<br>
Qiita![image](https://github.com/shohei0990/line_fastapi/assets/88127457/90dce221-4f4b-4b9a-9f44-b80269f53e63)<br>
