from flask import Blueprint, render_template, request, session, redirect
import pandas as pd
from app import db
from app.db.models import Account
import logging

LOG = logging.getLogger(__name__)


home_blueprint = Blueprint('home_blueprint', __name__)


def parseCSV(filePath):
    LOG.info('Parse Database Route Called')
    temp = list()

    # CVS Column Names
    col_names = ['AMOUNT', 'TYPE']
    try:
        LOG.logger.info('Parse Database Route file opened')
        # Use Pandas to parse the CSV file
        csvData = pd.read_csv(filePath, names=col_names, header=None)
        # Loop through the Rows
        for i, row in csvData.iterrows():
            temp.append([i[0], i[1]])
    except:
        LOG.logger.info('Parse Database Route Called but file cannot open')


    return temp


def add_data_in_database(filename, listtobeadded):
    skip_first = 0
    account_balance = 0
    username = session['user']
    for i in listtobeadded:
        if skip_first != 0:
            account_balance = account_balance + int(i[0])

        entry = Account(username=username, typeofbalance=i[1], balance=i[0])
        db.session.add(entry)
        db.session.commit()

        skip_first = 1
    return account_balance


@home_blueprint.route('/', methods=['POST', 'GET'])
def home():

    if 'user' not in session:
        LOG.info('Home  Route Called But system was not in Session')
        return redirect('/signin')

    LOG.info('Home  Route Called')
    username = session['user']

    get_all_the_record_against_a_user = Account.query.filter_by(username=username).all()

    skip_first = 0
    account_balance = 0

    for i in get_all_the_record_against_a_user:
        if i.balance != 'AMOUNT':
            account_balance = account_balance + int(i.balance)

    get_account_data = 0

    if request.method == 'POST':
        uploaded_file = request.files['file']
        getcsv_data = parseCSV(uploaded_file)
        get_account_data = add_data_in_database(session['user'], getcsv_data)

    return render_template('index.html', getcsv_data=get_all_the_record_against_a_user,
                           get_account_data=get_account_data, account_balance=account_balance)
