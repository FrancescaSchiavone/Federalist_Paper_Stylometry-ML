import pandas as pd
import scipy.sparse as sp
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils import resample
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("out\Dataset.csv")

#ripopolamento classe minoritaria = 'Jay' 
df_maggioritaria = df[df['Target'] == 'Hamilton']
df_classe_1 = df[df['Target'] == 'Madison']  # seconda classe maggioritaria
df_classe_2 = df[df['Target'] == 'Jay']  #classe meno rappresentata
df_classe_2_upsampled = resample(df_classe_2, replace=True, n_samples=len(df_classe_1), random_state=42) #random_state per la riproducibilità dei risultati

# Combina le classi bilanciate
df_balanced = pd.concat([df_maggioritaria, df_classe_1, df_classe_2_upsampled])

#vettorizzazione dati non numerici
vectorizer = CountVectorizer()
X_tokens = vectorizer.fit_transform(df_balanced['Most frequent tokens'].apply(lambda x: ' '.join([token for token, count in eval(x)])))
X_bigrams = vectorizer.fit_transform(df_balanced['Most frequent bigrams'].apply(lambda x: ' '.join([bigram for bigram, count in eval(x)])))
X_tokens_no_punctuation = vectorizer.fit_transform(df_balanced["Most frequent tokens, no punctuation"].apply(lambda x:' '.join([token for token, count in eval(x)])))
X_tokens_no_stopwords = vectorizer.fit_transform(df_balanced["Most frequent tokens, no stopwords"].apply(lambda x: ' '.join([token for token, count in eval(x)])))
X_bigrams_no_punctuation = vectorizer.fit_transform(df_balanced["Most frequent bigrams, no punctuation"].apply(lambda x: ' '.join([token for token, count in eval(x)])))
X_bigrams_no_stopwords = vectorizer.fit_transform(df_balanced["Most frequent bigrams, no stopwords"].apply(lambda x: ' '.join([token for token, count in eval(x)]))) 
X_pos = vectorizer.fit_transform(df_balanced["Most frequent PoS"].apply(lambda x: ' '.join([token for token, count in eval(x)])))

#standardizzazione dati numerici
scaler = StandardScaler()
X_numeric_scaled = scaler.fit_transform(df_balanced[['Number of tokens', 'Number of sents', 'Sentence Word Ratio', 'Type Token Ratio']])

# concatenazione matrici sparce in un'unica matrice
X = sp.hstack([X_tokens, X_bigrams, X_tokens_no_punctuation, X_bigrams_no_stopwords, X_bigrams_no_punctuation, X_bigrams_no_stopwords, X_pos, sp.csr_matrix(X_numeric_scaled)])
y = df_balanced["Target"]

# Divisione dei dati in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y) ##random_state per la riproducibilità dei risultati

# Modello RandomForest
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)  # Addestramento

# Valutazione del modello
y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
print(classification_report(y_test, y_pred))

# Cross-validation con StratifiedKFold
skf = StratifiedKFold(n_splits=5)
cv_scores = cross_val_score(rf, X, y, cv=skf)

# Media e deviazione standard della cross-validation
mean_score = cv_scores.mean()
sd = cv_scores.std()

print(f'Cross-validation mean accuracy: {mean_score}')
print(f'Cross-validation standard deviation: {sd}')

# Matrice di confusione
plt.style.use("ggplot")
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap='Purples', xticklabels=["Hamilton", "Jay", "Madison"], yticklabels=['Hamilton', 'Jay', 'Madison'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.savefig('out\confusion_matrix.png')
plt.show()




