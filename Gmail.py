#!/usr/bin/python
#-*- coding: utf-8 -*-
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.header import Header
from email import Encoders
import os

global gmail_user
global gmain_pwd

def getAccount(filename):
  cfgfile = open(filename, 'r')
  gmain_user = cfgfile.readline().strip()
  gmain_pwd  = cfgfile.readline().strip()

def sendMail(to, subject, text):
  get_account("account.txt")
  sebdMailAttach(to, subject, text, "")

def sendMailAttach(to, subject, text, attach):
  get_account("account.txt")
  msg = MIMEMultipart('alternative')
  msg['From'] = gmail_user
  msg['To']   = to
  msg['Subject'] = Header(s=subject, charset = "utf-8")
  msg.attach(MIMEText(text, _charset="utf-8"))
  if attach != "":
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)
  mailServer = smtplib.SMTP("smtp.gmail.com", 587)
  mailServer.ehlo()
  mailServer.starttls()
  mailServer.ehlo()
  mailServer.login(gmail_user, gmail_pwd)
  mailServer.sendmail(gmail_user, to, msg.as_string())
  mailServer.close()

