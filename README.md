# -MACHINE-LEARNING-MODEL-IMPLEMENTATION
COMPANY: CODTECH IT SOLUTIONS

NAME: PRATIK PATIL

"INTERN ID: CT06DH2258

"DOMAIN: PYTHON PROGRAMMING

"DURATION: 6 WEEEKS

*MENTOR: NEELA SANTOSH

Objective: The aim of Task 4 was to build a simple Machine Learning (ML) model using scikit-learn that can classify messages as either spam or not spam. This task introduced core ML steps: data loading, preprocessing, training, and evaluation.

Tools and Libraries Used:

pandas: For data loading and manipulation

scikit-learn: For building, training, and testing the ML model

CountVectorizer: To convert text into numerical features

MultinomialNB: A Naive Bayes classifier suitable for text classification

Approach: First, I created a CSV file called spam.csv with sample data that included text messages and their corresponding labels: 'spam' or 'ham' (not spam). Using pandas, I read the data and cleaned it for analysis.

Next, I used CountVectorizer to convert the text messages into numerical feature vectors, enabling the ML model to process the data. The dataset was split into training and testing sets using train_test_split.

Then, I trained a Naive Bayes classifier using MultinomialNB, which is ideal for text-based data. After training, I used the model to predict the test set labels and calculated the accuracy using accuracy_score.

I also included a classification_report which shows precision, recall, and F1-score — important metrics in evaluating classification models. Additionally, I allowed users to input custom messages to see if the model could correctly classify them as spam or ham.

Output and Performance:

Printed accuracy of the model (e.g., 90%)

Classification report with precision and recall values

Custom message predictions:

“Congratulations! You won a prize” → Spam

“Let’s meet at 5 PM” → Ham

Learning Outcomes:

Understood the full ML pipeline: data → features → model → evaluation

Learned how to use CountVectorizer for text classification

Gained practical experience with Naive Bayes, a popular algorithm in NLP

Realized the importance of data quality and balance in classification problems

Conclusion: This task gave hands-on experience in applying machine learning to a real-world problem: spam detection. It involved everything from loading data and cleaning it, to building a model and evaluating it. With slight modifications, this same pipeline can be used for many other classification tasks like sentiment analysis, product categorization, etc.

<img width="1004" height="687" alt="Image" src="https://github.com/user-attachments/assets/89e121d3-2a5f-4819-b75c-20d721f2af5e" />

Output 
[predictions.csv](https://github.com/user-attachments/files/21511083/predictions.csv)
