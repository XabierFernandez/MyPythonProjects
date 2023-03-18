# Random forest model
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("possum.csv")
df.sample(5, random_state=44)

# Lets do a quick clean up and remove any rows with missing data with
df = df.dropna()
# Now lets remove the unnecessary columns, 
#then store the features and the label data in separate variables
X = df.drop(["case", "site", "Pop", "sex"], axis=1)
y = df["sex"]

"""
Let me break the above code down for you 
(although I think it’s already familiar to you at this 
point if you’ve read the previous articles on machine learning models):
from sklearn.model_selection import train_test_split >> 
This line imports train_test_split which we’ll make it possible to randomly 
separate our dataset into train and test data.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=44) >> 
This is where we allocate 30% (test_size=0.3) of our data to training features (X_train) and labels (y_train), 
while the rest goes to test data (X_test, y_test). 
You may choose to use random_state=44 as well to get the same results as I.
from sklearn.ensemble import RandomForestClassifier >> We finally import the random forest model. 
The ensemble part from sklearn.ensemble is a telltale sign that random forests are ensemble models. 
It’s a fancy way of saying that this model uses multiple models in the background (=multiple decision trees in this case).
rf_model = RandomForestClassifier(n_estimators=50, max_features="auto", random_state=44) >> 
This is where we create our model with our chosen settings.
n_estimators determines the number of decision trees that make up our random forest. The more, the better.
max_features defines the number of features that each decision tree takes into consideration at each split. 
If you read the scikit-learn documentation, you’ll know that the default value for max_features is auto, 
which is actually the same as sqrt (=the square root of the number of features)). Using sqrt is the recommended setting.
rf_model.fit(X_train, y_train) >> Finally, we create our model based on the training data.
You may wonder why there’s no setting for bootstrapping. Actually, there is one: bootstrap=True, 
but since it’s the default setting, I’ve simply left it out 
https://data36.com/random-forest-in-python/
"""
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=44)
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(n_estimators=50, max_features="sqrt", random_state=44)
rf_model.fit(X_train, y_train)

predictions = rf_model.predict(X_test)
predictions