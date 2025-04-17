from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
import asyncio
import numpy as np

class KnowledgeClustering:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.clusters = {}

    async def cluster_knowledge(self, content):
        embedding = self.model.encode(content)
        kmeans = KMeans(n_clusters=3)
        cluster_id = kmeans.fit_predict([embedding])[0]
        self.clusters.setdefault(cluster_id, []).append(content)
        return f"Кластеризовано в кластер {cluster_id}"