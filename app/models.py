from . import db
from datetime import datetime

class Mantencion(db.Model):
    __tablename__ = 'mantenciones'

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    ingeniero = db.Column(db.String(100), nullable=False)
    horario = db.Column(db.String(50), nullable=False)
    area = db.Column(db.String(100), nullable=False)
    responsable = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(20), nullable=False)  # (o), [x], pendiente, etc.
    comentario = db.Column(db.String(300), nullable=True)

class Turno(db.Model):
    __tablename__ = 'turnos'

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    ingeniero = db.Column(db.String(100), nullable=False)
    plataforma = db.Column(db.String(100), nullable=False)
    horario = db.Column(db.String(50), nullable=False)
    rol = db.Column(db.String(100), nullable=False)
    observaciones = db.Column(db.String(300), nullable=True)


class ILOMetric(db.Model):
    __tablename__ = 'ilo_metrics'

    id = db.Column(db.Integer, primary_key=True)
    servidor = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    ancho_banda = db.Column(db.Float, nullable=True)  # Mbps
    errores = db.Column(db.Integer, nullable=True)
    cpu = db.Column(db.Float, nullable=True)          # %
    memoria = db.Column(db.Float, nullable=True)      # %
    estado = db.Column(db.String(20), nullable=False) # OK, WARNING, CRITICAL