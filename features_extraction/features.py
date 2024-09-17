import os
from collections import Counter
from string import punctuation
import spacy
from nltk.util import ngrams

nlp = spacy.load ("en_core_web_trf") #modello consigliato da Spacy.io per una maggiore accuratezza

def get_most_freq (path:str)->list:
    """
    The function returns the 20 most common tokens in a text.
    
    Parameters:
    path (str): the path of the text file.
    
    Returns: 
    list: A list of 20 tuples, each containing a token and its frequency
    """
    with open(path, "r", encoding="utf-8") as infile:
        text = infile.read()
        text = text.lower()
        doc= nlp(text)
        tokens = []
        for token in doc:
            if not token.is_space:
                tokens.append(token.text)
        counting_tokens = Counter(tokens)
        the_20_most_freq = counting_tokens.most_common(20)
    return the_20_most_freq


def get_most_freq_no_punct (path:str)->list: 
    """
    The function returns the 20 most common tokens in a text, exluding punctuation.
    
    Parameters:
    path (str): the path of the text file.
    
    Returns: 
    list: A list of 20 tuples, each containing a token and its frequency
    """
    with open(path, "r", encoding="utf-8") as infile:
        text = infile.read()
        text = text.lower()
        for i in list(punctuation):
            if i in text:
                text = text.replace(i, "")
        doc= nlp(text)
        tokens = []
        for token in doc:
            if not token.is_space:
                tokens.append(token.text)
        counting_tokens_no_punct = Counter(tokens)
        the_20_most_freq_no_punct = counting_tokens_no_punct.most_common(20)
    return the_20_most_freq_no_punct
    
def get_most_freq_no_stopwords (path:str)->list:
    """
    The function returns the 20 most common tokens in a text, exluding the stopwords.
    
    Parameters:
    path (str): the path of the text file.
    
    Returns: 
    list: A list of 20 tuples, each containing a token and its frequency
    """
    with open(path, "r", encoding="utf-8") as infile:
        text = infile.read()
        text = text.lower()
        for i in list(punctuation):
            if i in text:
                text = text.replace(i, "")
        doc= nlp(text)
        tokens = []
        for token in doc:
            if not token.is_space:
                tokens.append(token.text)
    stop_words = nlp.Defaults.stop_words
    tokens_no_stopwords= []
    for i in tokens:
        if i not in stop_words:
            tokens_no_stopwords.append(i)
    counting_no_stop_words = Counter(tokens_no_stopwords)
    the_20_most_freq_no_stopwords = counting_no_stop_words.most_common(20)
    return the_20_most_freq_no_stopwords
                    

def get_bigrams_no_punct (path:str)->list:
    """
    The function returns the 20 most common bigrams in a text, exluding punctuation.
    
    Parameters:
    path (str): the path of the text file.
    
    Returns: 
    list: A list of 20 tuples, each containing a bigram and its frequency
    """
    with open(path, "r", encoding="utf-8") as infile:
        text = infile.read()
        text = text.lower()
        doc= nlp(text)
        words = [token.text for token in doc if token.is_alpha] #elimina punteggiatura e spazi
        bigrams = [' '.join(gram) for gram in ngrams(words, 2)]
        counting_bigrams_no_punct = Counter(bigrams)
        the_20_most_freq_bigrams_no_punct = counting_bigrams_no_punct.most_common(20)
    return the_20_most_freq_bigrams_no_punct
    
def get_bigrams (path:str)->list:
    """
    The function return the 20 most common bigrams in a text.
    
    Parameters:
    path (str): the path of the text file.
    
    Returns: 
    list: A list of 20 tuples, each containing a bigram and its frequency
    """
    with open (path, "r", encoding="utf-8")as infile:
        text = infile.read()
        text = text.lower()
        doc = nlp(text)
        words = [token.text for token in doc if not token.is_space]
        bigrams = [' '.join(gram) for gram in ngrams(words, 2)]
        counting_bigrams = Counter(bigrams)
        the_20_most_freq_bigrams = counting_bigrams.most_common(20)
    return the_20_most_freq_bigrams
    
def get_bigrams_no_stopwords (path:str)->list:
    """
    The function return the 20 most common bigrams in a text, the stopwords.
    
    Parameters:
    path (str): the path of the text file.
    
    Returns: 
    list: A list of 20 tuples, each containing a bigram and its frequency.
    """
    with open(path, "r", encoding="utf-8") as infile:
        text = infile.read()
        text = text.lower()
        for i in list(punctuation):
            if i in text:
                text = text.replace(i, "")
        doc= nlp(text)
        tokens = []
        for token in doc:
            if not token.is_space:
                tokens.append(token.text)
    stop_words = nlp.Defaults.stop_words
    tokens_no_stopwords= []
    for i in tokens:
        if i not in stop_words:
            tokens_no_stopwords.append(i)
    bigrams = [' '.join(gram) for gram in ngrams(tokens_no_stopwords, 2)]
    counting_bigrams_no_stop_words = Counter(bigrams)
    the_20_most_freq_bigrams_no_stopwords = counting_bigrams_no_stop_words.most_common(20)
    return the_20_most_freq_bigrams_no_stopwords

def get_tokens (path: str)-> int:
    """
    The function counts the number of tokens in a text.
    
    Parameters:
    path (str): the path of the text file.
    
    Returns:
    int: the number of tokens in a text.
    """
    with open(path, "r", encoding="utf-8") as infile:
        text = infile.read()
        text = text.lower()
        doc= nlp(text)
        tokens = []
        for token in doc:
            if not token.is_space:
                tokens.append(token)
    return len(tokens)


def get_sents (path: str)-> int:
    """
    The function counts the number of sents in a text.
    
    Parameters:
    path (str): the path of the text file.
    
    Returns:
    int: the number of sents in a text.
    """
    with open(path, "r", encoding="utf-8") as infile:
        text = infile.read()
        text = text.lower()
        doc= nlp(text)
        sents = []
        for sent in doc.sents:
            sents.append(sent)
    return len(sents)

def sentence_word_ratio(path: str, get_token=None, get_sents= None) -> float:
    """
    Calculate the ratio of sentences to words in a text file.

    Parameters:

    path (str): The path to the text file.
    get_token : callable, optional 
    get_sents : callable, optional

    Returns:
    float: the ratio of sentences to words
    """
    if get_tokens is None or get_sents is None:
        raise ValueError("Both get_tokens and get_sents functions must be provided.")
    num_tokens = get_tokens(path)
    num_sents = get_sents(path)
    
    ratio = num_sents/num_tokens
    print(num_sents, num_tokens)
    return ratio

def get_pos (path: str)->list:
    """
    Analyzes the text in a file and returns the most common part-of-speech (POS) tags.

    Parameters:
    path (str): The path to the text file.

    Returns:
    list: A list of tuples, each containing a POS tag and its frequency, ordered from the most to the least common.
    """
    with open(path, "r", encoding="utf-8") as infile:
        text = infile.read()
        text = text.lower()
        doc = nlp(text)
        token_pos = []
        for token in doc:
            token_pos.append(token.pos_)
        counting_pos = Counter(token_pos)
        the_most_common_pos = counting_pos.most_common()
    return the_most_common_pos

def token_ratio (path:str)->float:
    """
    Calculate the ratio of unique tokens to the total number of tokens in a text file.

    Parameters:
    path(str): The path to the text file.

    Return: 
    float
     
    """
    with open(path, "r", encoding="utf-8") as infile:
        text = infile.read()
        text = text.lower()
        doc= nlp(text)
        tokens = []
        for token in doc:
            if not token.is_space:
                tokens.append(token.text)
        unique_tokens = set(tokens)
        token_ratio = len(unique_tokens)/len(tokens)
    return token_ratio

