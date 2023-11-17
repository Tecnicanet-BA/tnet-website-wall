# -*- coding: utf-8 -*-
from odoo import models, fields, api,_

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    min_amount = fields.Float('Minimum Amount',related="company_id.min_amount" ,readonly=False)
    is_amount = fields.Boolean('Is Amount')