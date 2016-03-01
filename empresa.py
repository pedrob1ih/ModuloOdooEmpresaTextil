# -*- coding: utf-8 -*-

from openerp import models, fields

class departamentos (models.Model):
    _name='empresa.departamentos'
    _description = "Departamentos"


    name= fields.Char('Nombre departamento', required=True)
        # complete_name': fields.function(_dept_name_get_fnc, type="char", string='Name'),
        # company_id': fields.many2one('res.company', 'Company', select=True, required=False),
    parent_id= fields.Many2one('empresa.departamentos', 'Departamento padre', select=True)
    manager_id= fields.Many2one('empresa.empleados', 'Director', track_visibility='onchange')
    

class empleados (models.Model):
    
    _name='empresa.empleados'
    _description = "Empleados"
    
    
    name= fields.Char('Nombre ', required=True)
    correoT=fields.Char('Correo-e del trabajo ', size=240)
    telefonoT=fields.Integer('Teléfono del trabajo ', required=True)
    department_id= fields.Many2one('empresa.departamentos', 'Departamento')
    parent_id= fields.Many2one('empresa.empleados', 'Director')
    coach_id=fields.Many2one('empresa.empleados', 'Monitor')
    notes= fields.Text('Otra información')
    direccionOficina= fields.Char('Dirección ficina')
    identification_id= fields.Char('Nº identificación')
    passport_id= fields.Char('Nº pasaporte')
    other_id= fields.Char('Otro ID')
    gender= fields.Selection([('hombre', 'Hombre'), ('mujer', 'Mujer'), ('otro', 'Otro')], 'Género')
    marital= fields.Selection([('soltero', 'Soltero'), ('casado', 'Casado'), ('viudo', 'Viudo'), ('divorciado', 'Divorciado')], 'Estado civil')
    birthday= fields.Date("Fecha de nacimiento")
    cuentaBancaria= fields.Char('Cuenta bancaria')
    

class proveedores (models.Model):
    
    _name='empresa.proveedores'
    _description = "Proveedores"
    
    name= fields.Char('Nombre ', required=True)
    identification_id= fields.Char('Nº identificación')
    telefonoT=fields.Integer('Teléfono del trabajo ', required=True)
    procedencia=fields.Char('Procedencia ', required=True)
    cuentaBancaria= fields.Char('Cuenta bancaria')

class telas (models.Model):
    
    _name='empresa.telas'
    _description = "Telas"
    
    name= fields.Char('Nombre ', required=True)
    identification_id= fields.Char('Nº identificación')
    procedencia=fields.Char('Procedencia ', required=True)
