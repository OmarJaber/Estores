# encoding=utf8
# -*- coding: utf-8 -*- u
from __future__ import unicode_literals
from __future__ import division
import frappe
import frappe, os , math
from frappe import _
from frappe.model.document import Document
from frappe.utils import get_site_base_path, cint, cstr, date_diff, flt, formatdate, getdate, get_link_to_form, \
    comma_or, get_fullname, add_years, add_months, add_days, nowdate
from frappe.utils.data import flt, nowdate, getdate, cint, rounded, add_months, add_days, get_last_day
from frappe.utils.csvutils import read_csv_content_from_uploaded_file
from frappe.utils.password import update_password as _update_password
from frappe.utils import cint, cstr, flt, nowdate, comma_and, date_diff, getdate, formatdate
# from umalqurra.hijri_date import HijriDate
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from erpnext.hr.doctype.salary_slip.salary_slip import SalarySlip
from erpnext.hr.doctype.leave_application.leave_application import get_leaves_for_period
from erpnext.hr.doctype.leave_application.leave_application import get_leave_allocation_records
from frappe.model.mapper import get_mapped_doc
import sys
from frappe.core.doctype.sms_settings.sms_settings import send_sms
from werkzeug.wrappers import Response
import json
import frappe, json
from frappe.utils.file_manager import save_file



@frappe.whitelist(allow_guest = True)
def add_job_applicant(formName, formEmail, formPhone, formJobTitle, filedata, formBasicMessage):
    if frappe.db.exists("Job Applicant", {"email_id": formEmail, "job_title": formJobTitle}):
        return "You have already applied for this job"
    else:

        if not frappe.db.exists("Job Opening", {"job_title": formJobTitle}):
            return "Job Opening {0} is not exist".format(formJobTitle)


        job_applican_doc = frappe.get_doc({
            "doctype": "Job Applicant",
            "applicant_name": formName,
            "email_id": formEmail,
            "phone_number": formPhone,
            "job_title": formJobTitle,
            "resume_attachment": "/private/files/"+cstr(filedata['files_data'][0]['filename']),
            "cover_letter": formBasicMessage
        })

        job_applican_doc.flags.ignore_validate = True
        job_applican_doc.flags.ignore_permissions = True
        job_applican_doc.flags.ignore_mandatory = True
        job_applican_doc.insert()
        frappe.db.commit()

        # if filedata:
        #     fd_json = json.loads(filedata)
        #     fd_list = list(fd_json["files_data"])
        #     for fd in fd_list:
        filename=filedata['files_data'][0]['filename']
        dataurl=filedata['files_data'][0]['dataurl']
        save_file(filename, dataurl, "Job Applicant", job_applican_doc.name, decode=True, is_private=1)
        # filedoc = save_file(fd["filename"], fd["dataurl"], "Job Applicant", job_applican_doc.name, decode=True, is_private=1)
        frappe.db.commit()
                
        return "Successfully saved"




