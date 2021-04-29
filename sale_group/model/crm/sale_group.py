from odoo import api, fields, models


class ResPartner(models.Model):
    _name = 'sale.group'

    name = fields.Char(string='Name', required=True)
    user_ids = fields.Many2many('res.users', string='Users Allowed')
    sales_teams = fields.Many2many('crm.team', 'ref_sale_group_crm_team', 'team_id', 'sale_group_id', string='Sales Teams')
    sequence = fields.Integer(default=10)

    @api.model
    def create(self, vals):
        sale_group = super(ResPartner, self).create(vals)
        for team in sale_group.sales_teams:
            team.sales_groups_id = [(4, sale_group.id)]
        return sale_group

    def write(self, vals):
        before_save = []
        for x in self:
            before_save = x.sales_teams.ids
        sale_group = super(ResPartner, self).write(vals)
        for rec in self:
            for team in rec.sales_teams:
                if team.id in before_save:
                    before_save.remove(team.id)
                team.sales_groups_id = [(4, rec.id)]
            sale_team_env = self.env['crm.team']
            for rm_id in before_save:
                sale_team = sale_team_env.browse(rm_id)
                sale_team.sales_groups_id = [(3, rec.id)]
        return sale_group
