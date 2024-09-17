# ***"The Federalist Papers"*: analisi stilometrica per l'attribuzione dell'Autore tramite tecniche di *machine learning***

## Abstract
Il progetto si concentra sull'analisi dei 'Federalist Papers', una serie di 85 articoli scritti tra il 1787 e il 1788 da tre autori distinti (*Alexander Hamilton, John Jay, James Madison*) sotto lo pseudonimo *Publius*. L'obiettivo di questo lavoro è attribuire ciascun testo al suo autore di riferimento basandosi su caratteristiche stilistiche. voro sono state estratte delle caratteristiche stilistiche dei testi. È stato creato un dataset  a partire dalle metriche stilistich e sviluppato un modello di *machine learning* per l'attribuzion dell'autore. I risultati ottenuti mostrano che il modello *Random Forest* ha raggiunto un'accuratezza del 82% con una deviazione standard di 0.055.

## Research questions
- È possibile attribuire un singolo testo all'autore di rierimento basandosi esclusivamente sugli aspetti stilistici?

## Dataset
Il Dataset utilizzato in questo progetto è stato creato a partire dai testi grezzi degli 85 papers, scaricati dal sito **Project Gutenberg** (https://www.gutenberg.org/). È composto da 85 righe (una per ogni testo) e 12 colonne, ciascuna contenente metriche calcolate sui singoli testi:
- **'Number of tokens'**: numero di tokens per testo.
- **'Most frequent tokens'**: lista di tuple costituite dai 20 tokens più frequenti e la loro frequenza.
- **'Most frequent tokens, no punctuation'**: lista di tuple costituite dai 20 tokens più frequenti (esclusa la punteggiatura) e la loro frequenza.
- **'Most frequent tokens, no stopwords'**: lista di tuple costituite dai 20 tokens più frequenti (escluse le *stopwords*) e la loro frequenza.
- **'Most frequent bigrams'**: lista di tuple costituite dai 20 bigrammi più frequenti e la loro frequenza.
- **'Most frequent bigrams, no punctuation'**: lista di tuple costituite dai 20 bigrammi più frequenti (esclusa la punteggiatura) e la loro frequenza.
- **'Most frequent bigrams, no stopwords'**:lista di tuple costituite dai 20 bigrammi più frequenti (escluse le *stopwords*) e la loro frequenza.
- **'Number of sents'**: il numero di frasi per testo.
- **'Most frequent PoS'**: lista di tuple costituite dalle categorie grammaticali (*Part of Speech*) e la loro frequenza. 
- **'Sentence Word Ratio'**: rapporto tra le frasi presenti in un testo e il numero di tokens totali. 
- **'Type Token Ratio'**: rapporto tra il set dei tokens presenti in un testo e il numero totale di questi.
- **'Target'**: nome dell'autore.

## A tentative list of milestones for the project
- **Fase 1 (Luglio 2024)**: raccolta dati e individuazione caratterstiche stilistiche da estrarre.
- **Fase 2 (Agosto 2024)**: sviluppo degli scripts per l'estrazione delle carattersitche e successiva creazione del dataset.
- **Fase 3 (Settembre 2024)**: addestramento del modello e valutazione delle prestazioni. 

## Documentation
La repository contiene le seguenti cartelle e i seugenti documenti:
- doc\: contiene il report del progetto che include la metologia, i risultati e le conclusioni.
- data\: contiene gli 85 testi in formato .txt 
- features_extraction\:
    - **features.py**: script delle funzioni per l'estrazione delle caratteristiche stilistiche
- src\:
    - **dataset.py**: script usato per la creazione del Dataset
    - **model.py**: script di addestramento e valutazione del modello di *Machine Learning*
- out\: contiene il Dataset e la matrice di confusione in formato *.png*.
- requirements.txt: elenco delle dipendenze del progetto.
- venv\: ambiente virtuale.
- .gitignore: contiene i file non necessari nel controllo di versione. 