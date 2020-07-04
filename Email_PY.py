#!/usr/bin/env python
# coding: utf-8

# In[16]:


import smtplib
import os

#https://myaccount.google.com/lesssecureapps
#Need to access to obtain an app password

EMAIL_ADDRESS = os.environ.get('USER_EMAIL')
EMAIL_PASSWORD = os.environ.get('USER_PASS')

print(EMAIL_ADDRESS)
print(EMAIL_PASSWORD)

subject = 'Sample Subject line'
body = 'Sample Body Text'
msg = f'Subject: {subject}\n\n{body}'
#smtp.sendmail(SENDER, RECEIVER, msg)

"""
server = smtplib.SMTP('smtp.gmail.com','587')
server.starttls()
server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
server.sendmail(EMAIL_ADDRESS,"Robbyhsiu329@gmail.com", msg)
"""

with smtplib.SMTP('smtp.gmail.com','587', timeout=120) as smtp:
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.sendmail(EMAIL_ADDRESS, 'Robbyhsiu329@gmail.com', msg)


# In[ ]:





# In[ ]:





# In[ ]:




