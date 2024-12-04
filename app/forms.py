from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class CropPredictionForm(FlaskForm):
    fertilizers_used = FloatField(
        "Fertilizer Amount (kg/ha)",
        validators=[
            DataRequired(),
            NumberRange(
                min=1,
                max=200,
                message="Fertilizer amount must be between 1 and 200 kg/ha",
            ),
        ],
    )

    employment = FloatField(
        "Employment in Agriculture in terms of Number of People",
        validators=[
            DataRequired(),
            NumberRange(
                min=1, max=5000, message="Employment number must be between 1 and 5000"
            ),
        ],
    )

    annual_precipitation = FloatField(
        "Annual Precipitation (mm)",
        validators=[
            DataRequired(),
        ],
    )

    land_area_equipped_for_irrigation = FloatField(
        "Irrigated Land Area (hectares)",
        validators=[
            DataRequired(),
        ],
    )

    submit = SubmitField("Predict Yield")

    def get_data(self):
        """Return form data as a dictionary"""
        return {
            "fertilizers_used": self.fertilizers_used.data,
            "employment": self.employment.data,
            "annual_precipitation": self.annual_precipitation.data,
            "land_area_equipped_for_irrigation": self.land_area_equipped_for_irrigation.data,
        }
