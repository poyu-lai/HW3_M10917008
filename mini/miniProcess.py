import os
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

class MiniNews:
    def __init__(self):
        self.news_type = []
        self.news_count = []
        self.news_content = []  # 2dimension

        self.news_conarray = []
        self.news_contype = []

    def content2Vector(self):
        vectorizer = CountVectorizer()
        convector = vectorizer.fit_transform(self.news_content).toarray()
        self.news_conarray = convector
        self.news_contype = vectorizer.get_feature_names

    def loadNews(self, data_path):
        news_folders = os.listdir(data_path)
        for folder_name in news_folders:
            self.news_type.append(folder_name)
            folder_path = os.path.join(data_path, folder_name)
            news_files = os.listdir(folder_path)
            self.news_count.append(len(news_files))
            for file_name in news_files:
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'r', encoding='utf-8',errors='ignore') as fr:
                    file_content = fr.read()
                    self.news_content.append(file_content)

        self.content2Vector()

