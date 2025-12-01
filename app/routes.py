from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Mantencion, Turno, ILOMetric
from . import db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


# ---------- MANTENCIONES ----------

@main.route('/mantenciones')
def mantenciones():
    registros = Mantencion.query.order_by(Mantencion.fecha.desc()).all()
    return render_template('mantenciones.html', mantenciones=registros)


@main.route('/mantenciones/nueva', methods=['GET', 'POST'])
def nueva_mantencion():
    if request.method == 'POST':
        fecha_str = request.form.get('fecha')
        ingeniero = request.form.get('ingeniero')
        horario = request.form.get('horario')
        area = request.form.get('area')
        responsable = request.form.get('responsable')
        estado = request.form.get('estado')
        comentario = request.form.get('comentario')

        if not fecha_str or not ingeniero or not horario or not area or not responsable or not estado:
            flash("Todos los campos obligatorios deben estar completos.", "danger")
            return redirect(url_for('main.nueva_mantencion'))

        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            flash("La fecha no tiene un formato válido.", "danger")
            return redirect(url_for('main.nueva_mantencion'))

        nueva = Mantencion(
            fecha=fecha,
            ingeniero=ingeniero,
            horario=horario,
            area=area,
            responsable=responsable,
            estado=estado,
            comentario=comentario
        )
        db.session.add(nueva)
        db.session.commit()
        flash("Mantención creada correctamente.", "success")
        return redirect(url_for('main.mantenciones'))

    return render_template('mantencion_nueva.html')


@main.route('/mantenciones/<int:id>/editar', methods=['GET', 'POST'])
def editar_mantencion(id):
    mantencion = Mantencion.query.get_or_404(id)

    if request.method == 'POST':
        fecha_str = request.form.get('fecha')
        ingeniero = request.form.get('ingeniero')
        horario = request.form.get('horario')
        area = request.form.get('area')
        responsable = request.form.get('responsable')
        estado = request.form.get('estado')
        comentario = request.form.get('comentario')

        if not fecha_str or not ingeniero or not horario or not area or not responsable or not estado:
            flash("Todos los campos obligatorios deben estar completos.", "danger")
            return redirect(url_for('main.editar_mantencion', id=id))

        try:
            mantencion.fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            flash("La fecha no tiene un formato válido.", "danger")
            return redirect(url_for('main.editar_mantencion', id=id))

        mantencion.ingeniero = ingeniero
        mantencion.horario = horario
        mantencion.area = area
        mantencion.responsable = responsable
        mantencion.estado = estado
        mantencion.comentario = comentario

        db.session.commit()
        flash("Mantención actualizada correctamente.", "success")
        return redirect(url_for('main.mantenciones'))

    return render_template('mantencion_editar.html', mantencion=mantencion)


@main.route('/mantenciones/<int:id>/eliminar', methods=['POST'])
def eliminar_mantencion(id):
    mantencion = Mantencion.query.get_or_404(id)
    db.session.delete(mantencion)
    db.session.commit()
    flash("Mantención eliminada correctamente.", "success")
    return redirect(url_for('main.mantenciones'))


# ---------- TURNOS ----------

@main.route('/turnos')
def turnos():
    registros = Turno.query.order_by(Turno.fecha.desc()).all()
    return render_template('turnos.html', turnos=registros)


@main.route('/turnos/nuevo', methods=['GET', 'POST'])
def nuevo_turno():
    if request.method == 'POST':
        fecha_str = request.form.get('fecha')
        ingeniero = request.form.get('ingeniero')
        plataforma = request.form.get('plataforma')
        horario = request.form.get('horario')
        rol = request.form.get('rol')
        observaciones = request.form.get('observaciones')

        if not fecha_str or not ingeniero or not plataforma or not horario or not rol:
            flash("Todos los campos obligatorios deben estar completos.", "danger")
            return redirect(url_for('main.nuevo_turno'))

        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            flash("La fecha no tiene un formato válido.", "danger")
            return redirect(url_for('main.nuevo_turno'))

        nuevo = Turno(
            fecha=fecha,
            ingeniero=ingeniero,
            plataforma=plataforma,
            horario=horario,
            rol=rol,
            observaciones=observaciones
        )
        db.session.add(nuevo)
        db.session.commit()
        flash("Turno creado correctamente.", "success")
        return redirect(url_for('main.turnos'))

    return render_template('turno_nuevo.html')


@main.route('/turnos/<int:id>/editar', methods=['GET', 'POST'])
def editar_turno(id):
    turno = Turno.query.get_or_404(id)

    if request.method == 'POST':
        fecha_str = request.form.get('fecha')
        ingeniero = request.form.get('ingeniero')
        plataforma = request.form.get('plataforma')
        horario = request.form.get('horario')
        rol = request.form.get('rol')
        observaciones = request.form.get('observaciones')

        if not fecha_str or not ingeniero or not plataforma or not horario or not rol:
            flash("Todos los campos obligatorios deben estar completos.", "danger")
            return redirect(url_for('main.editar_turno', id=id))

        try:
            turno.fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            flash("La fecha no tiene un formato válido.", "danger")
            return redirect(url_for('main.editar_turno', id=id))

        turno.ingeniero = ingeniero
        turno.plataforma = plataforma
        turno.horario = horario
        turno.rol = rol
        turno.observaciones = observaciones

        db.session.commit()
        flash("Turno actualizado correctamente.", "success")
        return redirect(url_for('main.turnos'))

    return render_template('turno_editar.html', turno=turno)


@main.route('/turnos/<int:id>/eliminar', methods=['POST'])
def eliminar_turno(id):
    turno = Turno.query.get_or_404(id)
    db.session.delete(turno)
    db.session.commit()
    flash("Turno eliminado correctamente.", "success")
    return redirect(url_for('main.turnos'))


# ---------- ILO ----------

@main.route('/ilo')
def ilo():
    servidor = "srv-ilo-01"

    # Métricas en el tiempo para un servidor
    metrics = (
        ILOMetric.query
        .filter_by(servidor=servidor)
        .order_by(ILOMetric.timestamp)
        .all()
    )

    labels = [m.timestamp.strftime("%d-%m %H:%M") for m in metrics]
    cpu = [m.cpu for m in metrics]
    bw = [m.ancho_banda for m in metrics]
    errores = [m.errores for m in metrics]
    memoria = [m.memoria for m in metrics]

    # Errores totales por servidor
    errores_por_servidor = (
        db.session.query(ILOMetric.servidor, db.func.sum(ILOMetric.errores))
        .group_by(ILOMetric.servidor)
        .all()
    )
    servidores = [s for s, _ in errores_por_servidor]
    errores_totales = [int(e or 0) for _, e in errores_por_servidor]

    # CPU promedio por servidor
    cpu_prom_por_servidor = (
        db.session.query(ILOMetric.servidor, db.func.avg(ILOMetric.cpu))
        .group_by(ILOMetric.servidor)
        .all()
    )
    servidores_cpu = [s for s, _ in cpu_prom_por_servidor]
    cpu_promedios = [round(c or 0, 1) for _, c in cpu_prom_por_servidor]

    # Distribución por estado (OK / WARNING / CRITICAL)
    estados_data = (
        db.session.query(ILOMetric.estado, db.func.count())
        .group_by(ILOMetric.estado)
        .all()
    )
    estados_labels = [e for e, _ in estados_data]
    estados_counts = [int(c or 0) for _, c in estados_data]

    return render_template(
        'ilo.html',
        labels=labels,
        cpu=cpu,
        bw=bw,
        errores=errores,
        memoria=memoria,
        servidores=servidores,
        errores_totales=errores_totales,
        servidores_cpu=servidores_cpu,
        cpu_promedios=cpu_promedios,
        estados_labels=estados_labels,
        estados_counts=estados_counts,
        servidor_actual=servidor,
    )