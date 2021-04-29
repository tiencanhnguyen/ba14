# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_group_ids = fields.Many2many(
        'sale.group', 'ref_sale_order_sale_group','sale_group_id', 'sale_order_id', string='Sales Groups', related='team_id.sales_groups_id')
