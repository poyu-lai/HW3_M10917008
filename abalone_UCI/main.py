from abaloneProcess import Abalone
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import numpy as np
import time

def purityCaculate(AB, result):
    sn = len(AB.ab_type)

    resultclass = []
    purity = 0
    rc = 0
    for i in range(sn):
        if AB.ab_typenum[i] == 0:
            continue
        unique, counts = np.unique(result[rc:rc+AB.ab_typenum[i]], return_counts=True)
        rc += AB.ab_typenum[i]
        # print(unique, counts) #顯示種列 跟數量
        maxcount = max(counts)
        resultclass.append(unique[counts==maxcount])
        purity += maxcount/sum(AB.ab_typenum)

    return purity, resultclass


print('UCIdataset-Abalone cluster')
datapath = 'abalone_prepare.csv'
AB = Abalone()
AB.loadAbCSV(datapath)
sn = len(AB.ab_type)


# #kmeans
kmeans = KMeans(n_clusters=sn, init='k-means++' ,random_state=101, n_init=15, max_iter=300)
k_time = time.perf_counter()            #time start
kmeans.fit(AB.ab_conarray)
k_time = time.perf_counter() - k_time   #time end
k_result = kmeans.fit_predict(AB.ab_conarray)
k_purity, kclass_type = purityCaculate(AB, k_result)
print('kmeans_purity = ', k_purity)
print('kmeans_usingTime = ', k_time)
print()

#hierarchical 
hierarchical = AgglomerativeClustering(n_clusters=sn, linkage='ward')
h_time = time.perf_counter()            #time start
hierarchical.fit(AB.ab_conarray)
h_time = time.perf_counter() - h_time   #time end
h_result = hierarchical.fit_predict(AB.ab_conarray)
h_purity, hclass_type = purityCaculate(AB, h_result)
print('hierarchical_purity = ', h_purity)
print('hierarchical_usingTime = ', h_time)
print()

#DBscan
dbscan = DBSCAN(eps=0.3, min_samples=5)
db_time = time.perf_counter()            #time start
dbscan.fit(AB.ab_conarray)
db_time = time.perf_counter() - h_time   #time end
db_result = dbscan.fit_predict(AB.ab_conarray_class_flatten)
db_purity, dbclass_type = purityCaculate(AB, db_result)
print('dbscan_purity = ', db_purity)
print('dbscan_usingTime = ', db_time)
print()


# hierarchical Plots the dendrogram
from scipy.cluster.hierarchy import dendrogram, linkage
linkage_matrix = linkage(AB.ab_conarray, 'ward')
figure = plt.figure(figsize=(12, 5))

dendrogram(linkage_matrix)
plt.title('Abalone Hierarchical Clustering Dendrogram (Ward)')
plt.xlabel('sample index')
plt.ylabel('distance')
plt.tight_layout()
plt.show()
