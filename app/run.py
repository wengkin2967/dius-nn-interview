import pandas as pd
import numpy as np
import keras

model = keras.models.load_model('best_model.keras')

# Read Sample data in
df = pd.read_csv('test_sample.csv')

# Linear Scaling - Help Gradient descent converge quicker towards minima
df_x1_x9 = df.drop(['X10'],axis=1)
df_x1_x9 = (df_x1_x9 - df_x1_x9.min()) / (df_x1_x9.max() - df_x1_x9.min())

# One Hot Encoding for categorical column 
df_x10 = pd.get_dummies(df['X10'],dtype=int)

df_processed = np.array(pd.concat([df_x1_x9,df_x10],axis=1))

print(model.predict(df_processed))



