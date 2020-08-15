# 客製化UI

程式一開始的畫面會呈現這樣~~ 照片都是取自男星楊洋的照片，另外我有加入音樂，所以打開的同時也會循環播放音樂，歌曲是林宥嘉的少女。

功能按鈕有Home, Love Start, Next, Previous, Heart, Play, Close，其中Home就是我們現在的主畫面。

<img width="600" height="550" src="https://github.com/chingi071/PyQt/blob/master/20200214/README_pix/Image%201.jpg"/></div>


按下Love Start後，會跳至卡片的開始內容，按Next接續下一張，按Previous回到上一張。
<img width="600" height="550" src="https://github.com/chingi071/PyQt/blob/master/20200214/README_pix/Image%202.jpg"/></div>


按下Heart，會呈現愛心圖片的畫面，按Click會是另一個愛心圖。
<img width="600" height="550" src="https://github.com/chingi071/PyQt/blob/master/20200214/README_pix/Image%203.jpg"/></div>


按下Game，會呈現猜幸運數字的遊戲，按下Start後，即可開始遊戲
<img width="600" height="550" src="https://github.com/chingi071/PyQt/blob/master/20200214/README_pix/Image%204.jpg"/></div>

按下Close，關閉程式。

# 程式架構
遵循MVC模式，將程式分為三個部分: 模型（Model）、視圖（View）和控制器（Controller）
1. 模型（Model）
   main.py - 所有的功能
  
2. 視圖（View）
   main_ui.py - ui的畫面設計

3. 控制器（Controller）
   content.py - 功能的控制
   
所有的圖片放置在pix資料夾裡，音樂在music資料夾。文字檔為word.txt(即卡片內容)、heart.txt(按下Heart後，畫面呈現的內容文字)

# 使用方式

打開pix資料夾，主畫面的圖為home_pix.jpg，將想放主畫面的圖取代這個圖。卡片圖片名稱為001.jpg, 002.jpg, 003.jpg, 004.jpg，將想放在卡片的圖片取代這些圖片。

卡片內容在word.txt裡，更改裡面的內容即可。(!!注意!!)卡片圖片與文字行數需一致。

若要更改圖片名稱需要更改code裡讀取圖片的名稱並更改icon.qrc裡的名稱，更改後，需按下run_genicon.bat，生成iconqrc.py，才能讓程式讀取到圖片。

Heart內容在heart.txt裡，更改裡面的內容即可。(目前設定2張愛心圖，3行文字。若要更改數量，需要修改code內容)

