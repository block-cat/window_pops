# coding:utf-8

from odoo import models, api, _, fields


class customize_window_tip(models.TransientModel):
    _name = "window.pops"

    name = fields.Char(u'标题')
    text = fields.Char(u'弹窗内容',readonly=True)
    
    @api.model
    def get_action(self):
        form_view_id = self.env.ref('window_pops.customize_window_form_view').id
        return {
            'name':self.name,
            'type':'ir.actions.act_window',
            'res_model':'window.pops',
            'view_mode':'form',
            'target':'new',
            'res_id':self.id,
            'views':[(form_view_id,'form'),],
        }

    def btn_OK(self):
        return {
            'type':'ir.actions.act_window_close'
        }
