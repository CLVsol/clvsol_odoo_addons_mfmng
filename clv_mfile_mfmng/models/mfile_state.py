# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import api, fields, models
from openerp.exceptions import UserError


class Address(models.Model):
    _inherit = 'clv.mfile'

    state = fields.Selection(
        [('new', 'New'),
         ('getting', 'Getting'),
         ('stored', 'Stored'),
         ('checked', 'Checked'),
         ('in_use', 'In Use'),
         ('used', 'Used'),
         ('deleted', 'Deleted'),
         ], string='State', default='new', readonly=True, required=True
    )

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        return True

    @api.multi
    def change_state(self, new_state):
        for mfile in self:
            if mfile.is_allowed_transition(mfile.state, new_state):
                mfile.state = new_state
            else:
                raise UserError('Status transition (' + mfile.state + ', ' + new_state + ') is not allowed!')

    @api.multi
    def action_new(self):
        for mfile in self:
            mfile.change_state('new')

    @api.multi
    def action_getting(self):
        for mfile in self:
            mfile.change_state('getting')

    @api.multi
    def action_stored(self):
        for mfile in self:
            mfile.change_state('stored')

    @api.multi
    def action_checked(self):
        for mfile in self:
            mfile.change_state('checked')

    @api.multi
    def action_in_use(self):
        for mfile in self:
            mfile.change_state('in_use')

    @api.multi
    def action_used(self):
        for mfile in self:
            mfile.change_state('used')

    @api.multi
    def action_deleted(self):
        for mfile in self:
            mfile.change_state('deleted')
