from flask import flash, render_template

from app import application
from app.crop_predictor import CropPredictor
from app.forms import CropPredictionForm

features = [
    {
        "name": "fertilizers_used",
        "label": "Fertilizer Amount",
        "type": "number",
        "default": 200,
        "unit": "kg/ha",
        "description": "Amount of fertilizer used per hectare",
    },
    {
        "name": "employment",
        "label": "Agricultural Employment",
        "type": "number",
        "default": 50,
        "unit": "in 1000 No.",
        "description": "Employment in agriculture",
    },
    {
        "name": "annual_precipitation",
        "label": "Annual Precipitation",
        "type": "number",
        "default": 1500,
        "unit": "mm",
        "description": "Total annual rainfall",
    },
    {
        "name": "land_area_equipped_for_irrigation",
        "label": "Irrigated Land Area",
        "type": "number",
        "default": 100,
        "unit": "in 1000 hectares",
        "description": "Area of land equipped with irrigation facilities",
    },
]

predictor = CropPredictor()


@application.route("/", methods=["GET", "POST"])
def index():
    prefix = application.wsgi_app.prefix[:-1]
    form = CropPredictionForm()

    if form.validate_on_submit():
        input_values = form.get_data()
        # Make the prediction using the CropPredictor model
        prediction = predictor.predict(input_values)
        return render_template(
            "index.html",
            title="Crop Yield Prediction App",
            features=features,
            prediction=prediction,
            prefix=prefix,
            form=form,
            input_values=input_values,
        )
    else:
        # Flash error messages for all form validation errors
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{error}", "danger")  # Use "danger" for red alert

    return render_template(
        "index.html",
        prefix=prefix,
        features=features,
        form=form,
        prediction=None,
        input_values=None,
    )
