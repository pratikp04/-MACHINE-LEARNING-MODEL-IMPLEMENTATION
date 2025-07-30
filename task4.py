import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# 1. Load the dataset
df = pd.read_csv("spam.csv")

# 2. Preprocess the data
df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})
X = df['text']
y = df['label_num']

# 3. Convert text to numbers (Bag of Words)
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.3, random_state=42)

# 5. Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# 6. Evaluate the model
y_pred = model.predict(X_test)
print("\n✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n🔍 Classification Report:\n", classification_report(y_test, y_pred))

# 7. Custom message prediction
sample = ["Congratulations! You've won a prize. Call now!", "Can we meet at 5 pm today?"]
sample_vec = vectorizer.transform(sample)
predictions = model.predict(sample_vec)

print("\n🧪 Custom Predictions:")
for i, msg in enumerate(sample):
    print(f"{msg} --> {'Spam' if predictions[i] else 'Ham'}")
