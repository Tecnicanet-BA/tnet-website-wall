from odoo import api, models, _

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    @api.model
    def _search_get_detail(self, website, order, options):
        res = super(ProductTemplate, self)._search_get_detail(website, order, options)
        res['fetch_fields'].append('default_code')
        res['mapping']['name']['name'] = "default_code"
        return res
