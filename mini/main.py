from miniProcess import MiniNews
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import numpy as np
import time

def purityCaculate(sn, result):
    resultclass = []
    purity = 0
    for i in range(sn):
        unique, counts = np.unique(result[i*100:(i+1)*100], return_counts=True)
        print(unique, counts) #顯示種列 跟數量
        maxcount = max(counts)
        resultclass.append(unique[counts==maxcount])
        purity += maxcount/(sn*100)

    return purity, resultclass


print('Minidataset-Abalone cluster')
datapath = 'mini_newsgroups'
MN = MiniNews()
MN.loadNews(datapath)
sn = len(MN.news_type)


#kmeans
kmeans = KMeans(n_clusters=sn, init='k-means++' ,random_state=101, n_init=15, max_iter=300)
k_time = time.perf_counter()            #time start
kmeans.fit(MN.news_conarray)
k_time = time.perf_counter() - k_time   #time end
k_result = kmeans.fit_predict(MN.news_conarray)
k_purity, kclass_type = purityCaculate(sn, k_result)
print('kmeans_purity = ', k_purity)
print('kmeans_usingTime = ', k_time)
print()


#hierarchical 
hierarchical = AgglomerativeClustering(n_clusters=sn, linkage='ward')
h_time = time.perf_counter()            #time start
hierarchical.fit(MN.news_conarray)
h_time = time.perf_counter() - h_time   #time end
h_result = hierarchical.fit_predict(MN.news_conarray)
h_purity, hclass_type = purityCaculate(sn, h_result)
print('hierarchical_purity = ', h_purity)
print('hierarchical_usingTime = ', h_time)
print()


#DBscan
dbscan = DBSCAN(eps=1.1, min_samples=3)
db_time = time.perf_counter()            #time start
dbscan.fit(MN.news_conarray)
db_time = time.perf_counter() - h_time   #time end
db_result = dbscan.fit_predict(MN.news_conarray)
db_purity, dbclass_type = purityCaculate(sn, db_result)
print('dbscan_purity = ', db_purity)
print('dbscan_usingTime = ', db_time)
print()


# hierarchical  Plots the dendrogram
from scipy.cluster.hierarchy import dendrogram, linkage
linkage_matrix = linkage(MN.news_conarray, 'ward')
figure = plt.figure(figsize=(12, 5))

dendrogram(linkage_matrix)
plt.title('Mini Hierarchical Clustering Dendrogram (Ward)')
plt.xlabel('sample index')
plt.ylabel('distance')
plt.tight_layout()
plt.show()