from flask import current_app, flash, render_template

from app.crop_predictor import CropPredictor
from app.forms import CropPredictionForm

predictor = CropPredictor()


def register_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def index():
        # Access features from the app config
        features = current_app.config["FEATURES"]
        form = CropPredictionForm()

        if form.validate_on_submit():
            input_values = form.get_data()
            # Use the predictor to make predictions
            prediction = predictor.predict(input_values)

            # if prediction is negative, set it to '-' and indicate by the model's estimates these values are not viable for growing crops
            if prediction < 0:
                prediction = 0
            return render_template(
                "index.html",
                title="Crop Yield Prediction App",
                features=features,
                prediction=prediction,
                form=form,
                input_values=input_values,
            )
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"{error}", "danger")

        return render_template(
            "index.html",
            features=features,
            form=form,
            prediction=None,
            input_values=None,
        )
