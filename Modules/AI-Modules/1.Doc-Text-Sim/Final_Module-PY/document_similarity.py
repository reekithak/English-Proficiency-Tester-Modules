from gensim.models.keyedvectors import KeyedVectors
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

model_path = r'D:\working repos\English-Proficiency-Tester\Modules\AI-Modules\1.Doc-Text-Sim\5-4-21\data\GoogleNews-vectors-negative300.bin'

class DocSim:
    def __init__(self, w2v_model, stopwords=None):
        self.w2v_model = w2v_model
        self.stopwords = stopwords if stopwords is not None else []

    def vectorize(self, doc: str) -> np.ndarray:
        """
        Identify the vector values for each word in the given document
        :param doc:
        :return:
        """
        doc = doc.lower()
        words = [w for w in doc.split(" ") if w not in self.stopwords]
        word_vecs = []
        for word in words:
            try:
                vec = self.w2v_model[word]
                word_vecs.append(vec)
            except KeyError:
                # Ignore, if the word doesn't exist in the vocabulary
                pass

        # Assuming that document vector is the mean of all the word vectors
        # PS: There are other & better ways to do it.
        vector = np.mean(word_vecs, axis=0)
        return vector

    def _cosine_sim(self, vecA, vecB):
        """Find the cosine similarity distance between two vectors."""
        csim = np.dot(vecA, vecB) / (np.linalg.norm(vecA) * np.linalg.norm(vecB))
        if np.isnan(np.sum(csim)):
            return 0
        return csim

    def calculate_similarity(self, source_doc, target_docs=None, threshold=0):
        """Calculates & returns similarity scores between given source document & all
        the target documents."""
        if not target_docs:
            return []

        if isinstance(target_docs, str):
            target_docs = [target_docs]

        source_vec = self.vectorize(source_doc)
        results = []
        for doc in target_docs:
            target_vec = self.vectorize(doc)
            sim_score = self._cosine_sim(source_vec, target_vec)
            if sim_score > threshold:
                results.append({"score": sim_score, "doc": doc})
            # Sort results by score in desc order
            results.sort(key=lambda k: k["score"], reverse=True)

        return results






w2v_model = KeyedVectors.load_word2vec_format(model_path, binary=True)

ds = DocSim(w2v_model)

def process_tfidf_similarity(source_doc,target_docs):
    vectorizer = TfidfVectorizer()

    # To make uniformed vectors, both documents need to be combined first.
    target_docs.insert(0, source_doc)
    embeddings = vectorizer.fit_transform(target_docs)

    cosine_similarities = cosine_similarity(embeddings[0:1], embeddings[1:]).flatten()

    highest_score = 0
    highest_score_index = 0
    for i, score in enumerate(cosine_similarities):
        if highest_score < score:
            highest_score = score
            highest_score_index = i

    return highest_score


source_doc = "abcde" # The piece of text that we get from the generator

target_docs = "abbdc" # The text that we get from the converted voice note.

sim_scores = ds.calculate_similarity(source_doc, target_docs)
tf_score = process_tfidf_similarity(source_doc,target_docs)

sim_score = 0
if((sim_scores[0]['score']>=0.9) && (tf_score>=0.8)):
    document_similar = True
    sim_score = (sim_scores[0]['score']+tf_score)/2
else:
    document_similar = False
    sim_score = (sim_scores[0]['score']+tf_score)/2



return sim_score