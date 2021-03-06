# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.osv import expression


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        if self._context.get("maintenance_manager", False):
            rmts_managers = self.search([]).filtered(
                lambda user: user.has_group("maintenance_management.group_maintenance_manager"))
            args = expression.AND([
                args or [],
                [('id', 'in', rmts_managers.ids)]
            ])
        return super(ResUsers, self)._name_search(name, args=args, operator=operator, limit=limit,
                                                  name_get_uid=name_get_uid)
