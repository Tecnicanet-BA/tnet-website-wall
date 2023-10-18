from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    show_stock_message_1 = fields.Boolean(string='Show Message(1)', default=False)
    stock_message_1_condition = fields.Float(string="Message(1) Condition")
    stock_message_1 = fields.Text(string="Message(1)")

    show_stock_message_2 = fields.Boolean(string='Show Message(2)', default=False)
    stock_message_2_condition_1 = fields.Float(string="Message(2) Condition(1)")
    stock_message_2_condition_2 = fields.Float(string="Message(2) Condition(2)")
    stock_message_2 = fields.Text(string="Message(2)")

    show_stock_message_3 = fields.Boolean(string='Show Message(3)', default=False)
    stock_message_3_condition_1 = fields.Float(string="Message(3) Condition(1)")
    stock_message_3_condition_2 = fields.Float(string="Message(3) Condition(2)")
    stock_message_3 = fields.Text(string="Message(3)")

    show_stock_message_4 = fields.Boolean(string='Show Message(4)', default=False)
    stock_message_4_condition = fields.Float(string="Message(4) Condition")
    stock_message_4 = fields.Text(string="Message(4)")