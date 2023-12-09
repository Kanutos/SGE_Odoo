from odoo import models, fields, api, exceptions

class videojuego(models.Model):
    _name = 'u3a3.videojuego'
    _description = 'Videojuego'

    codigo = fields.Integer()
    titulo = fields.Char()
    oferta = fields.Boolean()
    descuento = fields.Float(string='Descuento (%)')
    tipo = fields.Selection(selection=[('0', 'Accion'), ('1', 'Aventura'), ('2', 'Plataformas'), ('3', 'MOBA'), ('4', 'Terror'), ('5', 'Shooter')], required=True, string='Tipo')
    consola = fields.Many2one(comodel_name='u3a3.consola')
    precio = fields.Float()
    fecha_venta = fields.Date()
    personajes = fields.One2many(comodel_name='u3a3.personaje', inverse_name='videojuego_id', string='Personajes')

    def calcular_media(self):
        valores_enteros = [registro.precio for registro in self]
        media = sum(valores_enteros) / len(valores_enteros) if valores_enteros else 0
        return media

    @api.constrains('precio')
    def _check_precio_no_negativo(self):
        for videojuego in self:
            if videojuego.precio < 0:
                raise exceptions.ValidationError("El precio no puede ser negativo.")
            
class consola(models.Model):
    _name = 'u3a3.consola'
    _description = 'Consola'
    
    codigo = fields.Integer()
    nombre = fields.Char()
    ano_lanzamiento = fields.Date(string='Año de lanzamiento')
    descripcion = fields.Char()
    videojuego = fields.Many2many(comodel_name='u3a3.videojuego', relation='consola_videojuego_rel', column1='consola_id', column2='videojuego_id', string='Videojuegos')

class personaje(models.Model):
    _name = 'u3a3.personaje'
    _description = 'Personaje'

    nombre = fields.Char()
    descripcion = fields.Text()
    videojuego_id = fields.Many2one(comodel_name='u3a3.videojuego', string='Videojuego')
