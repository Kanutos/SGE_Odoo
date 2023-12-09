from odoo import models, fields

class videojuego(models.Model):
    _name = 'u3a2.videojuego'
    codigo = fields.Integer()
    titulo = fields.Char()
    oferta = fields.Boolean()
    tipo = fields.Selection(selection=[('0', 'Accion'), ('1', 'Aventura'), ('2', 'Plataformas'), ('3', 'MOBA'), ('4', 'Terror'),('5', 'Shooter')], required=True, string='Tipo')
    consola = fields.Many2one(comodel_name='u3a2.consola')
    precio = fields.Float()
    fecha_venta = fields.Date()

class consola(models.Model):
    _name = 'u3a2.consola'
    codigo = fields.Integer()
    nombre = fields.Char()
    ano_lanzamiento = fields.Date(string='Año de lanzamiento')
    descripcion = fields.Char()
    videojuego = fields.Many2many(comodel_name='u3a2.videojuego', relation='consola_videojuego_rel', column1='consola_id', column2='videojuego_id', string='videojuegos')