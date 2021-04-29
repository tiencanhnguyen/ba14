from odoo import fields, models


class CrmTeam(models.Model):
    _inherit = 'crm.team'

    sales_groups_id = fields.Many2many(
        'sale.group',
        'ref_crm_team_sale_group',
        'sale_group_id',
        'team_id',
        string='Sales Groups')
