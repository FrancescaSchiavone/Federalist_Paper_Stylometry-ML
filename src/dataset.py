import os
import pandas as pd
from features_extraction.features import get_tokens, get_most_freq, get_most_freq_no_punct, get_most_freq_no_stopwords, get_bigrams, get_bigrams_no_punct, get_bigrams_no_stopwords, get_sents, get_pos, sentence_word_ratio, token_ratio

def analysis_files_directory(directory_path:str)->pd.DataFrame:
    """
    Analyze all text files in a specified directory and its subdirectories.

    This function takes the path to a directory, searches for all text files within that directory (and its subdirectories), 
    and performs various linguistic analyses on each file. The results are compiled into a pandas DataFrame.

    Parameters:
    directory: (str) The path to the directory containing the text files to be analyzed.

    Returns:    
    (pd.DataFrame) A pandas DataFrame in which each row represents the analysis of a text file, 
        and each column contains the results of a specific analysis, such as:
        - Number of tokens
        - Most frequent tokens
        - Most frequent tokens without punctuation
        - Most frequent tokens without stopwords
        - Most frequent bigrams
        - Most frequent bigrams without punctuation
        - Most frequent bigrams without stopwords
        - Number of sentences
        - Most frequent parts of speech (PoS)
        - Sentence-to-word ratio
        - Type-to-token ratio
    """
    results = []
    files_paths=[]
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for file in filenames:
            if file.endswith(".txt"):
                files_paths.append(os.path.join(dirpath, file))
    
    print(f"Found {len(files_paths)} text files.") 


    for i in files_paths:
        try:
            file_results = {} 
            file_results["File"] = i.split('/')[-1] # estrazione del file dal nome del path
            file_results["Number of tokens"] = get_tokens(i)
            file_results["Most frequent tokens"] = get_most_freq(i)
            file_results["Most frequent tokens, no punctuation"] = get_most_freq_no_punct(i)
            file_results["Most frequent tokens, no stopwords"] = get_most_freq_no_stopwords(i)
            file_results["Most frequent bigrams"] = get_bigrams(i)
            file_results["Most frequent bigrams, no punctuation"] = get_bigrams_no_punct(i)
            file_results["Most frequent bigrams, no stopwords"] = get_bigrams_no_stopwords(i)
            file_results["Number of sents"] = get_sents(i)
            file_results["Most frequent PoS"] = get_pos(i)
            file_results["Sentence Word Ratio"] = sentence_word_ratio(i, get_tokens, get_sents)
            file_results["Type Token Ratio"] = token_ratio(i)

            results.append(file_results) 
        except Exception as e:
            print(f"Error processing file {files_paths}: {e}")
    df = pd.DataFrame(results)
    return df


df = analysis_files_directory("data")
df.to_csv("out/Dataset.csv", encoding="utf-8", index=False)

#il df non è ordinato per nome del file:
df["file_number"] = df["File"].str.extract(r"(\d+)").astype(int) #estrazione della parte numerica dalla colonna 'File' usando un'espressione regolare, converte la stringa numerica in int e assegna questi numeri ad una nuova colonna
df = df.sort_values(by="file_number") #ordina il df in ordine ascendente.
df= df.drop(columns=["File"])

df["Target"] = ["Hamilton", "Jay", "Jay", "Jay", "Jay", "Hamilton", "Hamilton","Hamilton","Hamilton", 
    "Madison", "Hamilton","Hamilton","Hamilton", "Madison","Hamilton","Hamilton","Hamilton", 
    "Madison", "Madison", "Madison", "Hamilton","Hamilton","Hamilton","Hamilton","Hamilton",
    "Hamilton","Hamilton","Hamilton","Hamilton","Hamilton","Hamilton","Hamilton","Hamilton",
    "Hamilton","Hamilton","Hamilton", "Madison", "Madison", "Madison", "Madison","Madison","Madison",
    "Madison","Madison","Madison","Madison","Madison","Madison", "Madison", "Madison","Madison","Madison","Madison",
    "Madison","Madison","Madison","Madison","Madison", "Hamilton", "Hamilton", "Hamilton", "Madison", 
    "Madison", "Jay", "Hamilton", "Hamilton", "Hamilton", "Hamilton", "Hamilton", "Hamilton", "Hamilton", "Hamilton", "Hamilton", 
    "Hamilton", "Hamilton", "Hamilton", "Hamilton", "Hamilton", "Hamilton", "Hamilton", "Hamilton", "Hamilton", "Hamilton", "Hamilton", "Hamilton"]

df = df.drop(columns=["file_number"])
df.to_csv("out\\Dataset.csv", index=False)
