import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = (
        os.environ.get("SECRET_KEY") or "very-secret-key"
    )  # Ideally, it will be from .env but for this purpose, I will just leave it here just so CSRF can work

    FEATURES = [
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
