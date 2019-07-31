import os
from app import config
from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, get_flashed_messages, session, Response
from . import main
from .forms import StandupForm
from .helper import saveData


@main.route('/', methods=['GET', 'POST'])
def index():
    form = StandupForm()

    if form.validate_on_submit():
        date = form.date.data
        yesterday_tasks = form.yesterday_tasks.data
        today_tasks = form.today_tasks.data
        additional_info = form.additional_info.data
        save_data = saveData(date, yesterday_tasks, today_tasks, additional_info)
        
        if(save_data):
            flash('Saved succesfully', 'success')
        
        else:
            flash('Not saved! Error occured', 'danger')

    return render_template('home.html', form=form)