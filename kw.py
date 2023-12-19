import pickle
import streamlit as st
from scipy.sparse import coo_matrix

class Kw:

    """
    Extract keywords from a text using pre-trained TF-IDF model
    """

    def __init__(self):
        self.kw_collection = pickle.load(open('pickles/sec09-kwCollection.pkl', 'rb'))
        self.kw_vectorizer = pickle.load(open('pickles/sec09-kwCountVectorizer.pkl', 'rb'))
        self.model = self.kw_collection = pickle.load(open('pickles/sec09-kwTfIdfModel.pkl', 'rb'))

    def sort_coo(self, coo_matrix: coo_matrix) -> list:
        "Return the sorted coordinate-forma matrix of the pair-wise"
        tuples = zip(coo_matrix.col, coo_matrix.data)
        return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

    def extract_top_n(self, feature_names: list, sorted_items: list, n=5) -> dict:
        """
        From a sorted map, return the top n values and scores
        :param feature_names: List of features that stored in the sorted list
        :param sorted_items: List of the sorted items
        :param n: number of returning results
        :return: Dictionary contains value and score
        """
        top_n = sorted_items[:n]
        scores = []
        values = []
        for idx, score in top_n:
            scores.append(round(score, 3))
            values.append(feature_names[idx])

        results = dict(zip(values, scores))
        return results

    def get_kw(self, text: str, n: int) -> dict:
        """
        Fit the Key words extractor on a given text using TF-IDF
        :param text: Given text
        :param n: number of scored results
        :return: Dictionary of scores
        """
        vector = self.model.transform(self.kw_vectorizer.transform([text]))
        sorted = self.sort_coo(vector.tocoo())
        kw = self.extract_top_n(self.kw_vectorizer.get_feature_names_out(), sorted, n)
        return kw

    def butify(self, kw: dict) -> None:
        """
        Print the vlaues and scores of a given set of key words + scores
        :param kw: Keywords + scores dictionary
        :return: None
        """
        rnk = 1
        st.subheader('Keywords:')
        for k, v in kw.items():
            st.write(f'{rnk}. **{k.capitalize()}** : Score: {v}')
            rnk += 1
