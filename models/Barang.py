from odoo import api, fields, models


class Barang(models.Model):
    _name = 'audreymarket.barang'
    _description = 'New Description'

    name = fields.Char(string='Nama Barang')
    harga_beli = fields.Integer(string='Harga Modal', required=True)
    harga_jual = fields.Integer(string='Harga Jual', required=True)

    #COMODEL MENENTUKAN MODEL YANG MENJADI ONE-NYA 
    kelompokbarang_id = fields.Many2one(comodel_name='audreymarket.kelompokbarang',
        ondelete='cascade' ,
        string='Kelompok Barang')

    supplier_id = fields.Many2many(
        comodel_name='audreymarket.supplier',
        # Penulisan String
        string='Supplier')

    stok = fields.Integer(
        string='stok',
    )
    
    
    

    