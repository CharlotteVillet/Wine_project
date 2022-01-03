# ML in production

Wine-o-meter is a future unicorn application. It allows wine producers to predict the quality score of their wine based on physicochemical inputs. The startup behind this innovation is convinced about its ability to disrupt the world of wine.

## Project

The data-science team has worked together on creating the best model predicting the quality score (from 0 to 10) of multiple wines. The next step is to include this model into the mobile application. The development team is expecting an API endpoint in order to request the model and display the result inside the application.

Your job is to put the trained model into production. Hopefully, the team provided you their work:

    a model.joblib which is the trained model pickled (saved using joblib library),
    the notebook used to train the model (Model_Training.ipynb) and the dataset (winequality.csv), so you can have a look,
    a test notebook (Test_Endpoint.ipynb) so you can assert that your endpoint is meeting the requirements.

## Goals

Your mission is to put this model into production by building an API. To succeed you need to:

    provide a /predict endpoint,
    provide a small documentation for the developer team at the index of your website.
