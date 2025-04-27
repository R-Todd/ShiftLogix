from app import db

class ShiftChange(db.Model):
    __tablename__ = "shift_changes"

    id          = db.Column(db.Integer, primary_key=True)
    shift_id    = db.Column(db.Integer, db.ForeignKey("shifts.shiftId"), nullable=False)
    add_or_drop = db.Column(db.String(10), nullable=False)  # "add" or "drop"
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.userId"), nullable=False)
    reason      = db.Column(db.Text, nullable=True)
    status      = db.Column(db.String(20), nullable=False, default="pending")

    def __repr__(self):
        return (f"<ShiftChange id={self.id} shift={self.shift_id} "
                f"action={self.add_or_drop} by={self.employee_id}>")
