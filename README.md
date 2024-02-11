# DiUS Interview - Kin Lee

## Part 1
### Exploration 
`exploration.ipynb` contains the exploration code for the data and the training process for the model. This includes processes like data pre-processing, hyperparameter tuning (Grid Search) and Evaluation (MAE). To run this notebook, install the packages in the `requirements.txt` file.
### Findings
Mean Absolute Error from the best Neural Network was **6.39**, evaluated from the test set. Predictions have been saved to `test_pred.csv` alongside the original test dataset for comparison.
### Serving
The `app/` directory contains all the files that the `Dockerfile` will copy to serve the model. You can build and run the image with 
```
docker build -t <YOUR_APP_NAME> .
docker run <YOUR_APP_NAME>
```
### Question - If you had flexibility to choose a model to tackle this problem, what model would that be?
Although using a deep learning model to predict Y was highly accurate, I would still opt for a simpler model like an XGBoost regressor for the reasons below.

1. **Size and nature of the dataset** - As we're only training on 14k  records which are tabular, Neural Networks may not be the best choice as they usually perform better when fed with larger datasets that are unstructured like images and text.
2. **Tradeoff between Accuracy VS Computation** - Running a simple XGBoost Regressor on the dataset, I got a result of a MAE score of **10.68**, which compared to the Neural Network score, is not much worse off given the computing complexity difference between the two models. 
3. **Interpretability of Model** - Understanding an XGBoost model is often times a lot easier than understanding a Neural Network, using tools like SHAP to provide feature importance in the model. 