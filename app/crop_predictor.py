import numpy as np


class CropPredictor:
    """
    This class is used to predict the crop based on the input data.
    """

    def __init__(self):
        self.model_beta, self.model_means, self.model_stds = self._load_model()

    def _load_model(self):
        """
        Load the model from the coefficient trained
        """
        # Load the the saved model coefficients from vocareum
        beta = np.array(
            [
                241629.1869565217,
                39265.97669378473,
                5079.212842448195,
                5927.713531727847,
                -11453.875508597243,
                -22043.639524365553,
            ]
        )
        means = np.array(
            [
                14.675652173913042,
                269.0869565217391,
                1884.2452173913043,
                3612.4569565217394,
                368.4889913043478,
            ]
        )
        stds = np.array(
            [
                12.373933270171985,
                4.074448946238123,
                176.49244348572384,
                313.71294648943814,
                508.8253371232129,
            ]
        )
        return beta, means, stds

    def _preprocess_features(self, inputs: dict) -> np.ndarray:
        """
        Preprocesses the user inputs into a feature vector suitable for prediction.
        Parameters:
        - inputs: A dictionary containing user inputs (e.g., fertilizers_used, annual_precipitation).
        Returns:
        - np.ndarray: The transformed and normalized feature vector.
        """
        # Extract raw inputs
        fertilizers_used = inputs["fertilizers_used"]
        land_area_equipped_for_irrigation = inputs["land_area_equipped_for_irrigation"]
        annual_precipitation = inputs["annual_precipitation"]
        employment = inputs["employment"]
        # Feature transformations
        fertilizers_used_squared = fertilizers_used**2
        # Combine features into a single vector
        feature_vector = np.array(
            [
                fertilizers_used,
                annual_precipitation,
                employment,
                land_area_equipped_for_irrigation,
                fertilizers_used_squared,
            ]
        )
        # Normalize the feature vector using training means and stds
        normalized_vector = (feature_vector - self.model_means) / self.model_stds
        # Add bias term (1 for the intercept)
        feature_vector_prepared = np.hstack(([1], normalized_vector))
        return feature_vector_prepared

    def predict(self, features):
        # Preprocess the features
        feature_vector = self._preprocess_features(features)
        # Calculate the prediction using the model coefficients
        # Calculate the prediction
        prediction = np.dot(feature_vector, self.model_beta)
        return prediction
