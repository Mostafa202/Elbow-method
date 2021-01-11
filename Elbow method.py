    """ within cluster sum of square to define number of clusters ( k )"""
def calc_wcss(data,n_centroids):
    wcss=[]
    for i in range(n_centroids):
        means=calc_means(i+1,data)
        clusters=find_clusters(means,data)
        clusters_dist=[]
        for j in range(len(clusters)):
            d=0
            items=clusters[j]
            for item in items:
                d+=calc_distance(item,means[j])**2
            clusters_dist.append(d)
            
        wcss.append(sum(clusters_dist))
    return wcss
