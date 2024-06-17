from odoo import models, fields # type: ignore
class alumno(models.Model):
     _name = 'colegio.alumno'
     _description = 'alumnos'

     name = fields.Char(string="Nombre", required=True)
     profesor = fields.Many2one("colegio.profesor")
     edad = fields.Integer(string="Edad", required=True)
     fecha_nacimiento = fields.Date(string ="Fecha de Nacimiento")
     direccion = fields.Text(string="direccion")
     carnet_identidad = fields.Text(string = "carnet de identidad")
     grado = fields.Selection(
        [
            ("basico","Basicoaaaaaa"),
            ("primaria","Primaria"),
            ("secundaria","Secundaria"),
        ],
        string = "Grado",
        default = "primaria",
        required = True,
     )