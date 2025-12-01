from datetime import date
from app import create_app, db
from app.models import Mantencion, Turno  # importa los modelos

app = create_app()

with app.app_context():
    # 👇 Asegura que las tablas existan
    db.create_all()

    # Limpiar tablas (si ya existen filas)
    Mantencion.query.delete()
    Turno.query.delete()

    # Mantenciones de ejemplo
    m1 = Mantencion(
        fecha=date(2025, 2, 1),
        ingeniero="Rodrigo Lara",
        horario="08:00 - 20:00",
        area="IPTV",
        responsable="Supervisión IPTV",
        estado="Pendiente",
        comentario="Revisión general de plataforma IPTV."
    )

    m2 = Mantencion(
        fecha=date(2025, 2, 1),
        ingeniero="Paulina Soto",
        horario="20:00 - 08:00",
        area="Broadcast",
        responsable="Jefatura NOC",
        estado="Completada",
        comentario="Verificación enlaces de contribución."
    )

    m3 = Mantencion(
        fecha=date(2025, 2, 2),
        ingeniero="Carlos Muñoz",
        horario="08:00 - 20:00",
        area="Telefonía",
        responsable="Supervisor Soporte",
        estado="En progreso",
        comentario="Pruebas de failover en central telefónica."
    )

    # Turnos de ejemplo
    t1 = Turno(
        fecha=date(2025, 2, 1),
        ingeniero="Rodrigo Lara",
        plataforma="IPTV",
        horario="08:00 - 20:00",
        rol="Supervisor TV",
        observaciones="Turno diurno, foco en alarmas críticas."
    )

    t2 = Turno(
        fecha=date(2025, 2, 1),
        ingeniero="Valentina Pizarro",
        plataforma="IPTV",
        horario="20:00 - 08:00",
        rol="Operador NOC",
        observaciones="Monitoreo plataforma OTT."
    )

    db.session.add_all([m1, m2, m3, t1, t2])
    db.session.commit()

    print("Datos de ejemplo insertados correctamente.")
