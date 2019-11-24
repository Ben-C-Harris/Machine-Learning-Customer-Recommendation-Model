# Machine Learning Customer Product Recommendation Model
Machine Learning recommender model for recommending new products to customers

Currently developing some new recommender models and creating a GUI to test their real time capabilities for including content and collaborative filtering.

Uploaded is an early stage basic KNN model applied to the well known movielens-100k dataset.

    KNN Basic Recommender Model has achieved:
        RMSE: 0.990
        MAE : 0.782

Current work is looking into higher performing models in Surprise (https://github.com/NicolasHug/Surprise/tree/f98907f84251e88f96669eb29284bd7976a8eecc) while also looking into LightFM (https://github.com/lyst/lightfm) and SparkML (https://spark.apache.org/docs/1.2.2/ml-guide.html).

Further work will include ways to minimise cold start issues and challenges related to introducing new products which are under-sampled.
