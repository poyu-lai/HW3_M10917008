# HW3_M10917008
# DATA MINE HW3 Cluster

### 題目內容
利用Python軟體實作群聚分析
資料集一：
使用mini 20 Newsgroups資料集
分別使用K-means、階層式分群、DBSCAN，將資料分成20群，並比較分群所花費時間，使用Purity指標衡量分群品質。
請劃出階層式分群的階層樹(Dendrogram)。
資料集二：
請從UCI ML repository中自選一個資料集，資料筆數必須大於1000筆。
分別使用K-means、階層式分群、DBSCAN進行群聚分析，並比較分群所花費時間以及選擇一個分群品質衡量指標比較分群結果。
請劃出階層式分群的階層樹(Dendrogram)。


### 資料格式
依據題目要求分成兩部分，第一部分使用mini 20 Newsgroups，第二部分是使用UCI上的資料集(此處我們使用的是abalone的資料)
* abalone_UCI
  * abalone_prepare.csv (可透過original_data準備)
  * abaloneProcess.py
  * main.py
  * original_data
    * abalone.data (原資料集)
    * abalone.names (資料集說明)
    * dataPrepare_abalone.py

* mini
  * minProcess.py
  * main.py
  * mini_newsgroups (可透過original_data準備)
    * mini-dataset...
  * original_data
    * mini_newsgroups.tar.gz(原資料集)
    * dis_targz.py



### 運作方法
若需要處理最原先的資料，只要先進入original_data資料夾中執行裡面python檔便能取得是前處理後的檔案，再將檔案移動到上層資料夾。

透過在個別資料夾(mini/abalone_UCI)，並在底下執行main.py即可運作
