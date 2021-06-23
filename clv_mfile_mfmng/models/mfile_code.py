# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class MediaFile(models.Model):
    _name = "clv.mfile"
    _inherit = 'clv.mfile', 'clv.abstract.code02'

    code = fields.Char(string='Media File Code', required=False, default='/')
    code_sequence_03 = fields.Char(default='clv.mfile.code_03')
    code_sequence_04 = fields.Char(default='clv.mfile.code_04')
    code_sequence_06 = fields.Char(default='clv.mfile.code_06')
    code_sequence_09 = fields.Char(default='clv.mfile.code_09')
    code_sequence_10 = fields.Char(default='clv.mfile.code_10')

    def _compute_path_str(self):
        for record in self:

            if record.alias:
                if record.code:
                    record.path = record.alias + '_' + record.code + '_'
                else:
                    record.path = record.alias
            else:
                if record.code:
                    record.path = '_' + record.code + '_'
