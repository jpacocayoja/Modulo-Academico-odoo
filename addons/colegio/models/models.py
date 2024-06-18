# -*- coding: utf-8 -*-

from odoo import models, fields # type: ignore


class profesor(models.Model):
     _name = 'colegio.profesor'
     _description = 'profesor'

     name = fields.Char(string="Nombre", required=True)
     description =  fields.Text(string="Descripcion")
     edad = fields.Integer(string="Edad", required=True)
     fecha_nacimiento = fields.Date(string ="Fecha de Nacimiento")
     saldo = fields.Float(string ="Saldo")
     estado = fields.Boolean(string ="Estado del profesor")
     grado = fields.Selection(
        [
            ("basico","Basico"),
            ("primaria","primaria"),
            ("secundaria","secundaria"),
        ],
        string = "Grado",
        default = "primaria",
        required = True,
     )


     
    
    