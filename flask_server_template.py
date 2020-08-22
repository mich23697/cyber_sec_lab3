#!/usr/bin/env python2
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import To
from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def email_server():
    print('sending email...')
    print(request.args)

    arg1 = request.args.get('to', type=str)
    arg2 = request.args.get('payload', type=str)

    #Exercise 2
    message = Mail(
        from_email='mich23697@gmail.com',
        to_emails=To(arg1),
        subject=arg2,
        html_content='<p>'+arg2+'</p>')
    try:
        sg = SendGridAPIClient("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")
        response = sg.send(message)
        print(response.status_code)
        print(response.body) 
        print(response.headers)
    except Exception as e:
        print(e.body)
        print(e.reason)

    if arg1 is None or arg2 is None:
        return 'Error: Missing parameters'
    else:
        return 'to=' + arg1 + ', payload=' + arg2


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
