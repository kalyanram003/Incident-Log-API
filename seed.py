from app import create_app
from app.database import db
from app.models import Incident

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    incident1 = Incident(
        title="Bias in facial recognition",
        description="Model misclassified individuals based on ethnicity.",
        severity="High"
    )
    incident2 = Incident(
        title="Hallucinated facts in output",
        description="Model outputted incorrect medical data.",
        severity="Medium"
    )
    db.session.add_all([incident1, incident2])
    db.session.commit()
    print("Sample incidents added.")
