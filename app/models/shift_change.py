from app import db
from datetime import datetime

class ShiftChange(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    shift_id    = db.Column(db.Integer, db.ForeignKey('shift.shiftId'), nullable=False)
    requested_at = db.Column(db.DateTime, default=datetime.utcnow)
    status      = db.Column(db.String(32), default='pending')
    reason      = db.Column(db.Text, nullable=False)