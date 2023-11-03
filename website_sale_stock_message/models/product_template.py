from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    show_stock_message_1 = fields.Boolean(string='Show Stock High', default=False)
    stock_message_1_condition = fields.Float(string="Message Condition")
    stock_message_1 = fields.Text(string="Message")

    show_stock_message_2 = fields.Boolean(string='Show Medium Stock', default=False)
    stock_message_2_condition_1 = fields.Float(string="Message Condition(1)")
    stock_message_2_condition_2 = fields.Float(string="Message Condition(2)")
    stock_message_2 = fields.Text(string="Message")

    show_stock_message_3 = fields.Boolean(string='Show Low Stock', default=False)
    stock_message_3_condition_1 = fields.Float(string="Message Condition(1)")
    stock_message_3_condition_2 = fields.Float(string="Message Condition(2)")
    stock_message_3 = fields.Text(string="Message")

    show_stock_message_4 = fields.Boolean(string='Show Out of Stock', default=False)
    stock_message_4_condition = fields.Float(string="Message Condition")
    stock_message_4 = fields.Text(string="Message")