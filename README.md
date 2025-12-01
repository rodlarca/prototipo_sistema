# Prototipo Sistema de Mantenciones, Turnos e ILO

Este proyecto es un prototipo funcional desarrollado para el ramo **TALLER DE DISEÑO DE SISTEMAS**, dictado por el profesor **Juan Manuel Martínez Morales**, como parte de la evaluación del semestre.

El prototipo fue desarrollado por los estudiantes:

- **Rodrigo Lara Cáceres**
- **Edgardo Ledezma**

---

## 🎯 Objetivo del proyecto

Construir un prototipo funcional que represente un sistema real con:

- Entrada y captura de datos  
- Procesamiento de información  
- Controles internos y GUI  
- Visualización de métricas  
- Aplicación de principios de calidad basados en ISO  

El prototipo simula una plataforma interna utilizada para:

- Gestión de **mantenciones**
- Administración de **turnos** de ingenieros
- Monitoreo de **servidores ILO** con métricas simuladas en tiempo real

---

## 🛠 Tecnologías utilizadas

- Python 3.x  
- Flask  
- Flask SQLAlchemy  
- SQLite  
- Bootstrap 5  
- Chart.js  

---

## 📁 Estructura del proyecto

```text
prototipo_sistema/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates/
│   └── static/
│
├── instance/
│   └── database.db (opcional — puede regenerarse con seed scripts)
│
├── config.py
├── run.py
├── crea_db.py
├── seed_db.py
├── seed_ilo.py
├── requirements.txt
└── .gitignore
