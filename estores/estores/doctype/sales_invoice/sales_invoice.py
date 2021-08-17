# -*- coding: utf-8 -*-
# Copyright (c) 2021, Estores and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import cint, cstr, flt, nowdate, comma_and, date_diff, getdate

class SalesInvoice(Document):
	def validate(self):
		total = 0
		total_tax = 0
		paid_amount = 0
		for item in self.items:
			item.amount = flt(item.qty)*flt(item.price)
			total = total+item.amount
		
		self.total = total
		self.total_without_tax = total


		for taxes in self.taxes:
			taxes.total_amount = total
			taxes.tax_value = total*(taxes.rate/100)
			total_tax = total_tax+(taxes.tax_value)
		

		for payments in self.payments:
			paid_amount = paid_amount+payments.value
		
		self.paid_amount = paid_amount
		self.total_tax_amount = total_tax
		self.grand_total = self.total_without_tax+self.total_tax_amount
		self.unpaid_amount = self.grand_total-self.paid_amount

