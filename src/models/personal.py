class Personal:
    nombre = ''
    apellidos = ''
    nombre_corto = ''
    fecha_de_nacimiento = ''
    numero_de_cuenta = ''
    correo = ''
    telefono = ''
    carrera = ''
    rfc = ''
    curp = ''
    estatus = ''
    modalidad = ''
    update = ''

    def __init__(self, nombre = '', apellidos = '', nombre_corto = '' ,fecha_de_nacimiento = '' ,numero_de_cuenta = '' ,correo = '' ,telefono = '' ,carrera = '' ,rfc = '' ,curp = '' ,estatus = '' ,modalidad = '', update = ''):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nombre_corto = nombre_corto
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.numero_de_cuenta = numero_de_cuenta
        self.correo = correo
        self.telefono = telefono
        self.carrera = carrera
        self.rfc = rfc
        self.curp = curp
        self.estatus = estatus
        self.modalidad = modalidad
        self.update = update

    def __str__(self):
        return f"Nombre: {self.nombre}\n" \
               f"Apellidos: {self.apellidos}\n" \
               f"Nombre corto: {self.nombre_corto}\n" \
               f"Fecha de nacimiento: {self.fecha_de_nacimiento}\n" \
               f"Número de cuenta: {self.numero_de_cuenta}\n" \
               f"Correo: {self.correo}\n" \
               f"Teléfono: {self.telefono}\n" \
               f"Carrera: {self.carrera}\n" \
               f"RFC: {self.rfc}\n" \
               f"CURP: {self.curp}\n" \
               f"Estatus: {self.estatus}\n" \
               f"Modalidad: {self.modalidad}\n" \
               f"Update: {self.update}"