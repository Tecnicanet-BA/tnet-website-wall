from odoo import _, fields, models  # type: ignore

class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"
    
    base = fields.Selection(selection_add=[('x_studio_precio_en_us', 'Precio en US')], 
                            ondelete={'x_studio_precio_en_us': 'set default'})
