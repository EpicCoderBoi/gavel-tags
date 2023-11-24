from gavel.models import db

class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tags = db.Column(db.String(255), nullable=False)

    def __init__(self, tags):
        self.tags = tags