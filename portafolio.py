from flask import (
    Blueprint, current_app, render_template, request, url_for
)

from sendgrid.helpers.mail import *
import sendgrid