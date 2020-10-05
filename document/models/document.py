from odoo import api, models, fields
from datetime import  datetime

class project_document(models.Model):
    _name = 'document'
    _description = 'get the document downloaded'

class document_attachement(models.Model):
        _inherit = "ir.attachment"
        _inherit = "document"
        def action_attachment(self):
            action = self.env.ref('document_document.action_attachement').read()[0]
            action['domain'] = [('project_id','=',self.id)]
            action['context']= {'default_document_id':self.id}
            return action
