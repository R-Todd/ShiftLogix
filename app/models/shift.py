from app import db

class Shift(db.Model):
    shiftId      = db.Column(db.Integer, primary_key=True)
    employee_id  = db.Column(db.Integer, db.ForeignKey('employee.userId'), nullable=False)
    start_time   = db.Column(db.DateTime, nullable=False)
    end_time     = db.Column(db.DateTime, nullable=False)

    def duration(self):
        return self.end_time - self.start_time