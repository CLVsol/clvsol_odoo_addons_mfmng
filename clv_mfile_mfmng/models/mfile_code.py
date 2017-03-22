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

from odoo import api, fields, models


class MediaFile(models.Model):
    _name = "clv.mfile"
    _inherit = 'clv.mfile', 'clv.code02.model'

    code = fields.Char(string='Media File Code', required=False, default='/')
    code_sequence_03 = fields.Char(default='clv.mfile.code_03')
    code_sequence_04 = fields.Char(default='clv.mfile.code_04')
    code_sequence_06 = fields.Char(default='clv.mfile.code_06')
    code_sequence_09 = fields.Char(default='clv.mfile.code_09')
    code_sequence_10 = fields.Char(default='clv.mfile.code_10')

    @api.one
    def _compute_path_str(self):
        if self.alias:
            self.path = self.alias + '_' + self.code + '_'
        else:
            self.path = '_' + self.code + '_'
