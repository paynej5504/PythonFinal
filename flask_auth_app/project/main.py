#import statements
from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from flask_login import login_required, current_user
from .models import Entry
from .form import entryform
from .form import EditEntryForm



main = Blueprint('main', __name__)


#route to main page
@main.route('/')
def index():
    #render index page
    return render_template('index.html')

@main.route('/profile')
# profile page of current user
@login_required
def profile():
    # render profile page
    return render_template('profile.html', name=current_user.name)

#help route
@main.route('/help')
@login_required
def help():
    # render help page
    return render_template('help.html')


#history table route
@main.route('/table')
@login_required
def tables():
   #gets all data from database
    entryTable = Entry.query.all()
    table = entryTable
   # render table page with data
    return render_template("table.html", table=table)

#map route
@main.route('/map')
@login_required
def map():
    # render map page
    return render_template('map.html')

#graph route
@main.route('/graph')
@login_required
def graph():
    # render graph page
    return render_template('graph.html')


#entry form route
@main.route('/entry', methods=['GET', 'POST'])
@login_required
def entry():
    # request form data
    form = entryform(request.form)
    if request.method == 'POST' and form.validate():
        entry = Entry()
        #call save_changes function and create new entry
        save_changes(entry, form, new=True)
        #flash message displays if successful
        flash('entry created successfully!')
        # redirect to tables page
        return redirect(url_for('main.tables'))
    return render_template('entry.html', form=form)


@main.route('/entry', methods = ['GET', 'POST'])
@login_required
def save_changes(entry, form, new=False):
    # assign the data that was entered in the form
    entry.houseId = form.houseId.data
    entry.date = form.date.data
    entry.id = form.id.data
    entry.eggs = form.eggs.data
    entry.alive = form.alive.data
    entry.dead = form.dead.data
    entry.species = form.species.data
    entry.cowbird = form.cowbird.data
    entry.damaged = form.damaged.data
    entry.comment = form.comment.data

    if new:
        # add new entry to database
        db.session.add(entry)
    #commit changes
    db.session.commit()
    # render history page
    return render_template('table.html')


#edit entry form route
@main.route('/<int:entryId>/edit-entry', methods=['GET', 'POST'])
@login_required
def editEntry(entryId):
    #gets form data from previous entry
    entry = Entry.query.get(entryId)
    form = EditEntryForm( obj=entry)
    if request.method == 'POST':
        # get info from editEntry form
            houseId = request.form.get('houseId')
            date = request.form.get('date')
            id = request.form.get('id')
            eggs = request.form.get('eggs')
            alive = request.form.get('alive')
            dead = request.form.get('dead')
            species = request.form.get('species')
            cowbird = request.form.get('cowbird')
            damaged = request.form.get('damaged')
            comment = request.form.get('comment')
            entryId = request.form.get('entryId')


        # error messages if field is left empty
            if houseId == "" or date == "" or id == "" or eggs == "" or alive == "" or dead == "" or species == "" or cowbird == "" or damaged == "" or comment == "":
                flash("Can't leave and fields empty")
                return redirect(url_for('main.entry'))

            #assign new values
            entry.houseId = houseId
            entry.date = date
            entry.id = id
            entry.eggs = eggs
            entry.alive = alive
            entry.dead = dead
            entry.species = species
            entry.cowbird = cowbird
            entry.damaged = damaged
            entry.comment = comment
            # commit changes
            db.session.commit()
        # flash message displays if successful
            flash('entry edited successfully!')
        #return history page if successfully edited
            return redirect(url_for('main.tables'))
    #render edit-entry page
    return render_template('edit-entry.html', title='Edit Entry', form=form, entry=entry)


#delete route
@main.route('/<int:entryId>/delete_entry', methods=['GET', 'POST'])
@login_required
def delete_entry(entryId):
    # get entry that matches the selected entryId
    entry = Entry.query.get(entryId)
    #delete selected entry
    Entry.query.filter(Entry.entryId == entryId).delete()
    #commit changes
    db.session.commit()
    # show success message
    flash('successfully deleted!')
    # redirect to history page
    return redirect(url_for('main.tables'))


@main.route('/entry', methods = ['GET', 'POST'])
@login_required
def entry_post():
    #get info from entry form
    houseId = request.form.get('house')
    date = request.form.get('date')
    id = request.form.get('user')
    eggs = request.form.get('eggs')
    alive = request.form.get('alive')
    dead = request.form.get('dead')
    species = request.form.get('species')
    cowbird = request.form.get('cowbird')
    damaged = request.form.get('damaged')
    comment = request.form.get('comment')

    # error messages
    if houseId == "" or date == "" or id == "" or eggs == "" or alive == "" or dead == "" or species == "" or cowbird == "" or damaged == "" or comment == "":
        flash("Can't leave and fields empty")
        return redirect(url_for('main.entry'))

    # create new entry and save to db
    new_entry = Entry(houseId=houseId, date=date, id=id, eggs=eggs, alive=alive, dead=dead, species=species,
                     cowbird=cowbird, damaged=damaged, comment=comment)

    # add user to database
    db.session.add(new_entry)
    # commit changes
    db.session.commit()
    #render history page
    return render_template('table.html')

