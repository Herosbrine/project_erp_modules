from odoo import api, models, fields
from datetime import  datetime

class projet_contact(models.Model):
    _name = 'projetprojet'
    _description = 'Nouvelle fiche projet'
    _rec_name = 'name_projet'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _inherits = {
        'res.company': 'company_id',
    }
    user_id = fields.Many2one('res.users', ondelete='set null', string='Créateur du projet',default=lambda self: self.env.user)
    name_projet = fields.Text(string='Nom du projet', required=True, index=True, track_visibility="onchange")
    company_id = fields.Many2one('res.company', 'Organisation', required=True, index=True, ondelete='restrict')
    type_projet = fields.Selection([('Etatique', 'etatique'), ('Religieux', 'religieux'),('Associatif', 'associatif'), ('Autre','autre'), ],'Type de projet', default='Associatif')
    date = fields.Date(string='Date de création du projet',default=datetime.today())
    status = fields.Selection([('Annuler', 'annulé'), ('Confirmer', 'confirmé'), ('Brouillon', 'brouillon'), ('En cours', 'en cours'), ],'Statut', default='Brouillon', track_visibility="onchange")
    notes = fields.Text(string='Notes')
    name = fields.Text()
    Etapes = fields.Selection([('Nouveau', 'nouveau'), ('Etude', 'étude'), ('Validé', 'validé'), ('Refusé', 'refusé'), ('En cours', 'en cours'), ('Cloture', 'cloture'), ], string='Etapes', readonly=True, default='Nouveau', track_visibility="onchange")
    country_id1 = fields.Many2one('res.country', 'Pays', required=True, index=True)
    is_document = fields.Boolean("Is Document")
    res_model = fields.Char('Resource Model', readonly=True, help="The database object this attachment will be attached to.")
    res_id = fields.Many2oneReference('Resource ID', model_field='res_model', readonly=True, help="The record id this is attached to.")
    document_new = fields.Integer()
    adresse_postale = fields.Text()
    ville = fields.Char()
    departement = fields.Char()
    description_projet = fields.Text(string='description du projet')
    code_analytique = fields.Char(track_visibility="onchange")
    budget_list_lines = fields.One2many('projetprojet.budget', 'the_budget_id', string='Budget list')
    contact_list_lines = fields.One2many('projetprojet.contact', 'the_contact_id', string='Contact list')
    event_list_lines = fields.One2many('projetprojet.event', 'the_event_id', string="Event list")
    versement_list_lines = fields.One2many('projetprojet.versement', 'the_versement_id', string='Vers list')
    evaluation_list_lines = fields.One2many('projetprojet.evaluation', 'the_evaluation_id', string='Eval list') 
    materiel_list_lines = fields.One2many('projetprojet.materiel', 'the_materiel_id', string='Materiel list')
    mattechnique_list_lines = fields.One2many('projetprojet.mattechnique', 'the_mattechnique_id', string='Materiel technique liste')
    batiments_list_lines = fields.One2many('projetprojet.batiments', 'the_batiments_id', string='Batiments liste')
    beneficiaire_list_lines = fields.One2many('projetprojet.beneficiaire', 'the_beneficiaire_id', string='Beneficiaire liste')
    histoire_project = fields.Text(string="Histoire")
    tel_project = fields.Char()
    adresse_email = fields.Char()
    context_ville = fields.Text()
    context_pays = fields.Text()
    nombres_beneficiaire = fields.Integer()
    role = fields.Char(string='Nature')
    nombre = fields.Integer(string="Nombre")
    role1 = fields.Char(string='Nature')
    nombre1 = fields.Integer(string="Nombre")

    def action_etude(self):
        for rec in self:
            rec.Etapes = 'Etude'
    def action_valider(self):
        for rec in self:
            rec.Etapes = 'Validé'
    def action_refuser(self):
        for rec in self:
            rec.Etapes = 'Cloture'
    def action_encour(self):
        for rec in self:
            rec.Etapes = 'En cours'
    def action_cloture(self):
        for rec in self:
            rec.Etapes = 'Cloture'
    @api.onchange('state_id')
    def onchange_state(self):
        if self.state_id:
            self.country_id = self.state_id.country_id.id
class parent_projet(models.Model):
        _inherit ="res.partner"
        _inherit ="res.users"
        _inherit ="res.country"
        _inherit = "ir.attachment"

        def action_projet_button(self):
            action = self.env.ref('projet_projet.action_projet_button').read()[0]
            action['domain'] = [('projet_id','=',self.id)]
            action['context']= {'default_projet_id':self.id}
            return action
class contact_list(models.Model):
        _name = 'projetprojet.contact'
        _description = 'contact liste'

        begin_date = fields.Date(string='Date de début',default=datetime.today())
        contact_represent = fields.Selection([('Représentant', 'représentant'), ('Superviseur', 'superviseur'), ('Référent', 'référent'), ('Partenaires', 'partenaires'), ], string='Rôle')
        organisation = fields.Many2one('res.company', ondelete='set null', string='Organisation')
        the_contact_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche contact')
        the_contact_id1 = fields.Many2one('res.users', ondelete='set null', string='Fiche contact', default=lambda self: self.env.user)
        end_date = fields.Date(string='Date de fin')

class budget_list(models.Model):
        _name = 'projetprojet.budget'
        _description = 'budget liste'

        the_budget_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche budget')
        currency_id = fields.Many2one('res.currency', string='Currency')
        commission_date = fields.Date(string='date de commission')
        annee = fields.Selection('year_selection', default="2020", string='année')
        demande = fields.Monetary(string='demande')
        valider = fields.Monetary(string='validé')
        depasser = fields.Monetary(string='dépensé')
        def year_selection(self):
            year = 2000
            year_list = []
            while year != 2100:
                year_list.append((str(year), str(year)))
                year += 1
            return year_list

class event_list(models.Model):
        _name = 'projetprojet.event'
        _description = 'event liste'

        the_event_id = fields.Many2one('projetprojet', ondelete='set null', string='Liste event')
        type_passage = fields.Selection([('Visite', 'visite'), ('Soiree', 'soirée'), ('Fete', 'fête'), ('Inspection', 'inspection'), ], string='Type')
        date = fields.Date(string='Date')
        description = fields.Text(string='Description')
class versement_list(models.Model):
        _name = 'projetprojet.versement'
        _description = 'versement liste'

        the_versement_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche versement')
        currency_id = fields.Many2one('res.currency', string='Currency')
        date = fields.Date(string='Date de paiement')
        montant = fields.Monetary(string='Montant')
        object = fields.Text(string='Objet')

class evaluation_list(models.Model):
        _name = 'projetprojet.evaluation'
        _description = 'evaluation liste'

        the_evaluation_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche evaluation')
        annee = fields.Selection('year_selection', default="2020", string='Année')
        objectif_fixer = fields.Text(string='Objectifs fixés')
        evaluation_milieu = fields.Text(string='Evaluation Milieu/Année')
        evaluation_fin = fields.Text(string='Evaluation Fin/Année')
        resultat_evaluation = fields.Text(string='Resultat Evaluation')

        @api.model
        def year_selection(self):
            year = 2000
            year_list = []
            while year != 2100:
                year_list.append((str(year), str(year)))
                year += 1
            return year_list
class materiel_list(models.Model):
    _name = 'projetprojet.materiel'
    _description = 'materiel liste'

    the_materiel_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche materiel')
    vehicule = fields.Char()
    type_vehicule = fields.Selection([('Moto', 'moto'), ('Voiture', 'voiture'), ], string='Type')
    Immatriculation = fields.Char()
    date_aqui = fields.Date(string="Date d'aquisition")
    etat = fields.Selection([('Neuf', 'neuf'), ('Bon', 'bon'), ('Moyen', 'moyen'), ('Mauvais', 'mauvais'), ], string='Etat')

class materiel_tech(models.Model):
    _name = 'projetprojet.mattechnique'
    _description = 'materiel technique liste'

    the_mattechnique_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche materiel technique')
    date_aqui = fields.Date(string="Date d'aquisition")
    etat = fields.Selection([('Neuf', 'neuf'), ('Bon', 'bon'), ('Moyen', 'moyen'), ('Mauvais', 'mauvais'), ], string='Etat')
    type_materiel = fields.Selection([('Outil', 'outil'), ('Decoration', 'decoration'), ('Nourriture', 'nourriture'), ], string='Type')
    nombre = fields.Integer()
    nom = fields.Char()
class batiments_list(models.Model):
    _name = 'projetprojet.batiments'
    _description = 'batiment liste'

    the_batiments_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche batiments')
    type_batiments = fields.Selection([('Immeuble', 'immeuble'), ('Maison', 'maison'), ('Appartement', 'appartement'), ], string='Type')
    date_aqui = fields.Date(string="Date d'aquisition")
    etat = fields.Selection([('Neuf', 'neuf'), ('Bon', 'bon'), ('Moyen', 'moyen'), ('Mauvais', 'mauvais'), ], string='Etat')
    ville = fields.Char()
    fonction = fields.Selection([('Hopital', 'hopital'), ('Logement', 'logement'), ('Bureau', 'bureau'), ('Commerce','commerce'), ('Autre', 'autre'), ], string='Fonction')
class beneficiaire_list(models.Model):
    _name = 'projetprojet.beneficiaire'
    _description = 'beneficiaire liste'

    the_beneficiaire_id = fields.Many2one('projetprojet', ondelete='set null', string='Fiche contact')
    the_contact_id = fields.Many2one('res.partner', ondelete='set null', string='Nom des bénéficiaires')
