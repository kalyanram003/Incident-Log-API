from app import create_app
from app.database import db
from app.models import Incident

app = create_app()

with app.app_context():
    db.create_all()
    sample_incidents = [
        Incident(title="Unexpected Output", description="AI model returned toxic output", severity="High"),
        Incident(title="Bias Detected", description="Model favors one demographic group", severity="Medium"),
    ]
    db.session.bulk_save_objects(sample_incidents)
    db.session.commit()
