import numpy as np
import pickle
import process_text as pt
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences



class DialectModel:
    def __init__(self):
        self.dialect_map = {'EG': 0,'LY': 1,'LB': 2,'SD': 3,'MA': 4}
        print("Loading Models...")
        # load bow vectroizer for the NB model
        with open('BOW.pickle', 'rb') as handle:
            self.cv = pickle.load(handle)

        # load NB model
        with open('NB_model.pickle', 'rb') as handle:
            self.NB = pickle.load(handle)

        # load tokenizer
        with open('tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)

        # load LSTM Model
        self.LSTM_model = tf.keras.models.load_model('LSTM_model.h5')
        print("Models Loaded!")

    def predict_NB(self, text):
        text = pt.pre_process_text(text)
        text_vec = self.cv.transform([text])
        return self.get_key_by_value(self.dialect_map, self.NB.predict(text_vec))
    

    
    def predict_LSTM(self, text):
        text = pt.pre_process_text(text)
        sequence = self.tokenizer.texts_to_sequences([text])
        padded_sequence = pad_sequences(sequence, maxlen=100)
        return self.get_key_by_value(self.dialect_map, np.argmax(self.LSTM_model.predict(padded_sequence, verbose=0)))
    
    def get_key_by_value(self, dictionary, value):
        for key, val in dictionary.items():
            if val == value:
                return key
        return None



