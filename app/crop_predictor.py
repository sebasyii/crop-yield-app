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
                237423.77476249254,
                17973.92599596955,
                5558.628732232614,
                5792.007801726939,
                -10368.478825357055,
            ]
        )
        means = np.array(
            [
                14.38539767032609,
                269.42857142857144,
                1867.042857142857,
                3622.3757142857144,
            ]
        )
        stds = np.array(
            [
                12.715518433002499,
                3.8584653817341446,
                168.33683471067215,
                303.05596692488257,
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
        # Combine features into a single vector
        feature_vector = np.array(
            [
                fertilizers_used,
                land_area_equipped_for_irrigation,
                annual_precipitation,
                employment,
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
