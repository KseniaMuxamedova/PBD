from datetime import datetime
from datetime import date

import flask

from app_config import app, db
from flask import request, render_template, redirect, url_for, flash
# from jinja2 import escape
from sqlalchemy import desc
from forms import CompanyEditForm, JournalEditForm, ModelEditForm, SearchForm
from model import Company, Models, Journal

PIn = 'uGv^@zl/hL'


@app.after_request
def set_x_frame_options(response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response


@app.route('/')
def index():
    return render_template(
        'index.html',
        title='Ниточка с иголочкой'

    )


@app.route('/companits')
def companits():
    companies = db.session.query(Company). \
        order_by(Company.inn). \
        all()
    return render_template(
        'companits.html',
        title='Компании',
        companies=companies,
        count=Company.query.count()

    )


@app.route('/searchcompanits', methods=['GET', 'POST'])
def searchcompanits():
    s = request.form.get('q')
    if s=="":
        companies = db.session.query(Company). \
            order_by(Company.inn). \
            all()
        count = db.session.query(Company). \
            count()
    else:
            companies = db.session.query(Company). \
                filter(Company.name == s). \
                all()
            count = db.session.query(Company). \
                filter(Company.name == s). \
                count()

    return render_template(
        'companits.html',
        title='Компании',
        companies=companies,
        count=count

    )

@app.route('/filterjournals', methods=['GET', 'POST'])
def filterjournals():
    s = request.form.get('f')
    journals = db.session.query(Journal). \
        filter(Journal.date_of_issue == s). \
        all()
    count = db.session.query(Journal). \
        filter(Journal.date_of_issue == s). \
        count()
    return render_template(
        'journals.html',
        title='Журналы',
        journals=journals,
        count=count
    )


@app.route('/journals')
def journals():
    journals = db.session.query(Journal). \
        order_by(Journal.id). \
        all()
    return render_template(
        'journals.html',
        title='Журналы',
        journals=journals,
        count=Journal.query.count()

    )





@app.route('/company/<int:inn>')
def company(inn):
    cat = db.session.query(Company).filter(Company.inn == inn).one_or_none()
    if cat is None:
        return 'Not Found', 404

    n = db.session.query(Models). \
        filter(Models.company_INN == cat.inn). \
        order_by(desc(Models.company_INN)). \
        all()

    return render_template(
        "company.html",
        company=cat,
        models=n,
        count=Models.query.filter(Models.company_INN == cat.inn).count()
    )


@app.route('/edit_company/<int:inn>', methods=['GET', 'POST'])
def edit_company(inn):

    cat = db.session.query(Company).filter(Company.inn == inn). \
            one_or_none()
    if cat is None:
        return 'Not Found', 404

    form = CompanyEditForm(request.form)

    if form.button_save.data:
        if form.validate():
            if form.pin.data == PIn:
                cat.name = form.name.data
                db.session.add(cat)
                db.session.commit()
                flash("Шалость удалась!")
            else:
                flash("Неверный код доступа")
    elif form.button_delete.data:
        db.session.delete(cat)
        db.session.commit()
        return redirect(url_for('companits'))
    else:
        form.name.data = cat.name

    return render_template(
        'edit_company.html',
        company=cat,
        form=form
    )


@app.route('/edit_journal/<int:id>', methods=['GET', 'POST'])
def edit_journal(id):
    if id == 0:
        cat = Journal()
        cat.id  = db.session.query(Journal). \
        count() + 10
    else:
        cat = db.session.query(Journal).filter(Journal.id == id). \
            one_or_none()
    if cat is None:
        return 'Not Found', 404

    form = JournalEditForm(request.form)
    if form.button_save.data:
        if form.validate():
            if form.pin.data == PIn:
                cat.name = form.name.data
                cat.date_of_issue = form.date_of_issue.data
                db.session.add(cat)
                db.session.commit()
                if id == 0:
                    db.session.flush()
                    return redirect(url_for('edit_journal', id=cat.id))
                flash("Шалость удалась!")
            else:
                flash("Неверный код доступа")
    elif form.button_delete.data:
        if form.pin.data == PIn:
            db.session.delete(cat)
            db.session.commit()
            return redirect(url_for('journals'))
        else:
            flash("Неверный код доступа")
    else:
        form.name.data = cat.name
        print(cat.date_of_issue)
        if id == 0:
            form.date_of_issue.data = date.today()

        else:
            form.date_of_issue.data = datetime.strptime(cat.date_of_issue, '%Y-%m-%d').date()

    return render_template(
        'edit_journal.html',
        journal=cat,
        form=form
    )


@app.route('/edit_model/<int:id>', methods=['GET', 'POST'])
def edit_model(id):
    if id == 0:
        cat = Models()
        cat.id = Models.query.count()
    else:
        cat = db.session.query(Models).filter(Models.id == id). \
            one_or_none()
    if cat is None:
        return 'Not Found', 404

    form = ModelEditForm(request.form)
    if form.button_save.data:
        if form.validate():
            if form.pin.data == PIn:
                cat.pattern = form.pattern.data
                cat.algoritnm = form.pattern.data
                cat.result = form.pattern.data
                cat.sizes = form.sizes.data
                cat.fabric_consumption = form.consumption.data
                db.session.add(cat)
                db.session.commit()
                if id == 0:
                    db.session.flush()
                    return redirect(url_for('edit_model', id=cat.id))
                flash("Шалость удалась!")
            else:
                flash("Неверный код доступа")
    elif form.button_delete.data:
        if form.pin.data == PIn:
            db.session.delete(cat)
            db.session.commit()
            return redirect(url_for('company'))
        else:
            flash("Неверный код доступа")
    else:
        if id == 0:
            form.date_of_issue.data = date.today()

        else:
            form.pattern.data = cat.pattern
            form.pattern.data = cat.algoritnm
            form.pattern.data = cat.result
            form.sizes.data = cat.sizes
            form.consumption.data = cat.fabric_consumption

    return render_template(
        'edit_model.html',
        model=cat,
        form=form
    )


if __name__ == '__main__':
    # Create scheme if not exists
    with app.app_context():
        db.create_all()
        db.session.commit()

    app.run(debug=True)
