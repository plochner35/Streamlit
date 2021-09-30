# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 17:49:51 2021

@author: User1
"""
import streamlit as st

st.title("Pro Rated Time")
st.write("""Shown is the prorated time for billable and total hours""")

audit_bill = st.number_input("Enter billable audit hours: ", min_value=0.000,max_value=25000.000,value=1.000, step=.001)
tax_bill = st.number_input("Enter billable tax hours: ", min_value=0.000,max_value=25000.000,value=1.000, step=.001)
admin_hours = st.number_input("Enter nonbillable admin hours: ", min_value=0.000,max_value=25000.000,value=1.000, step=.001)
tb = audit_bill + tax_bill
prop = audit_bill/tb
nonbill_audit = admin_hours*prop
total_audit = audit_bill + nonbill_audit
tax_nonbill = admin_hours - nonbill_audit
total_tax = tax_bill + tax_nonbill

#print(("Audit:", audit_bill, nonbill_audit, total_audit))
#print (("Tax:", tax_bill, tax_nonbill, total_tax))

st.write(("Audit:", audit_bill, nonbill_audit, total_audit))
st.write(("Tax:", tax_bill, tax_nonbill, total_tax))
