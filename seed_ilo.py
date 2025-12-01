from datetime import datetime, timedelta
from app import create_app, db
from app.models import ILOMetric

app = create_app()

with app.app_context():
    # Opcional: limpiar solo tabla ILO
    ILOMetric.query.delete()

    ahora = datetime.utcnow()

    servidores = ["srv-ilo-01", "srv-ilo-02", "srv-ilo-03"]

    registros = []

    # 24 puntos (últimas 24 horas), cada 1 hora, por servidor
    for s in servidores:
        for i in range(24):
            ts = ahora - timedelta(hours=24 - i)

            base_cpu = 30 if s == "srv-ilo-01" else 40 if s == "srv-ilo-02" else 35
            base_bw = 100 if s == "srv-ilo-01" else 80 if s == "srv-ilo-02" else 60

            cpu = base_cpu + (i % 5) * 3
            ancho_banda = base_bw + (i % 4) * 10
            errores = 0 if i % 5 else (i % 3) + 1

            if errores == 0 and cpu < 70:
                estado = "OK"
            elif errores <= 2 or cpu < 85:
                estado = "WARNING"
            else:
                estado = "CRITICAL"

            registros.append(
                ILOMetric(
                    servidor=s,
                    timestamp=ts,
                    ancho_banda=ancho_banda,
                    errores=errores,
                    cpu=cpu,
                    memoria=60 + (i % 4) * 5,
                    estado=estado,
                )
            )

    db.session.add_all(registros)
    db.session.commit()
    print(f"Insertados {len(registros)} registros de ILO.")
