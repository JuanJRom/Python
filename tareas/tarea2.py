# Homework two regular expressions
import re


# Email validation
def email_validation(tex):
    ev = '^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,3}$'
    if re.match(ev, tex):
        return print('The email is valid')
    else:
        return print('The email is invalid')


# Email validation
def phone_validation(tex):
    pv = '^[0-9]{10}|\([0-9]{2}\)[0-9]{8}|\([0-9]{3}\)[0-9]{7}$'
    if re.match(pv, tex):
        return print('The phone is valid')
    else:
        return print('The phone is invalid')


# CURP validation
def curp_validation(tex):
    cv = '^[A-Z]{4}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM][A-Z]{2}[B-DF-HJ-NP-TV-Z]{3}[A-Z\d](\d)$'
    if re.match(cv, tex):
        return print('The CURP is valid')
    else:
        return print('The CURP is invalid')


# RFC validation
def rfc_validation(tex):
    rv = '^[A-Z]{4}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[A-Z0-9]{3}$'
    if re.match(rv, tex):
        return print('The RFC is valid')
    else:
        return print('The RFC is invalid')

# Correo valido
email = 'jjosue.romero@alumnos.udg.mx'
email_validation(email)
# Correo invalido
email1 = 'jjosue.r%mero@alumnos.udg.mx'
email_validation(email1)

# Telefono valido
phone = '(33)12295634'
phone_validation(phone)
# Telefono invalido
phone = '(333)322295634'
phone_validation(phone)

# CURP valida
curp = 'ZARE000516MJCTVMA0'
curp_validation(curp)
# CURP invalida
curp = 'ZARE000556MJCTVMA0'  # se modifico a un dia de mes que no existe
curp_validation(curp)

rfc = 'ROHJ910211FD0'
rfc_validation(rfc)
