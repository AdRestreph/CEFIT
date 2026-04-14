import qtawesome as qta
from ui.themes import tema_actual


def icono(nombre, color=None):
    t = tema_actual()
    if color is None:
        color = "#D4B483" if t == "charcoal" else "#C9A84C"
    return qta.icon(nombre, color=color)


def iconos_crud(btn_nuevo, btn_editar, btn_eliminar,
                btn_excel=None, btn_pdf=None,
                btn_buscar=None, btn_limpiar=None):
    t     = tema_actual()
    dorado = "#D4B483" if t == "charcoal" else "#C9A84C"
    rojo   = "#FF6B6B" if t == "charcoal" else "#DC2626"
    verde  = "#63C98A" if t == "charcoal" else "#16A34A"
    gris   = "#AEAEB2" if t == "charcoal" else "#6B7280"
    naranja = "#D4B483" if t == "charcoal" else "#D97706"

    btn_nuevo.setIcon(qta.icon("fa5s.plus",         color=dorado))
    btn_editar.setIcon(qta.icon("fa5s.pen",          color=dorado))
    btn_eliminar.setIcon(qta.icon("fa5s.trash-alt",  color=rojo))
    if btn_excel:
        btn_excel.setIcon(qta.icon("fa5s.file-excel",   color=verde))
    if btn_pdf:
        btn_pdf.setIcon(qta.icon("fa5s.file-pdf",       color=naranja))
    if btn_buscar:
        btn_buscar.setIcon(qta.icon("fa5s.search",      color=gris))
    if btn_limpiar:
        btn_limpiar.setIcon(qta.icon("fa5s.times",      color=gris))


def iconos_formulario(btn_guardar, btn_cancelar, btn_imagen=None):
    t      = tema_actual()
    verde  = "#63C98A" if t == "charcoal" else "#16A34A"
    gris   = "#AEAEB2" if t == "charcoal" else "#6B7280"
    morado = "#AEAEB2" if t == "charcoal" else "#8B5CF6"

    btn_guardar.setIcon(qta.icon("fa5s.check",       color=verde))
    btn_cancelar.setIcon(qta.icon("fa5s.times",      color=gris))
    if btn_imagen:
        btn_imagen.setIcon(qta.icon("fa5s.image",    color=morado))


def favicon(nombre_ventana):
    t     = tema_actual()
    dorado = "#D4B483" if t == "charcoal" else "#C9A84C"
    mapeo = {
        "app":          ("fa5s.building",      dorado),
        "clientes":     ("fa5s.users",         "#60A5FA"),
        "consultores":  ("fa5s.user-tie",      "#86EFAC"),
        "servicios":    ("fa5s.briefcase",     "#FEF3C7"),
        "proyectos":    ("fa5s.project-diagram","#C4B5FD"),
        "propuestas":   ("fa5s.file-alt",      "#FCA5A5"),
        "fases":        ("fa5s.tasks",         "#A5F3FC"),
        "entregables":  ("fa5s.box-open",      "#A7F3D0"),
        "horas":        ("fa5s.clock",         "#E5E7EB"),
        "facturas":     ("fa5s.receipt",       dorado),
        "conocimiento": ("fa5s.book",          "#FCA5A5"),
        "formulario":   ("fa5s.edit",          dorado),
    }
    icono_nombre, color = mapeo.get(nombre_ventana, ("fa5s.circle", dorado))
    return qta.icon(icono_nombre, color=color)