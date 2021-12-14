from flask_babel import _
from flask import Blueprint, request, render_template, redirect
from flask.helpers import url_for

from .models import Task
from app.src.db import db


task_bp = Blueprint('task', __name__)


@task_bp.route('/', methods=['GET'])
@task_bp.route('/<int:id>/', methods=['GET'])
def list_task(id=None):
    context = {'tasks': Task.query.all()}

    instance = Task.query.get(id)

    if instance:
        context['focus_task'] = instance

    return render_template('task/list.html', context=context)


@task_bp.route('/create', methods=['POST'])
def create_task():
    data = dict(request.values)
    instance = Task(**data)

    db.session.add(instance)
    db.session.commit()

    return redirect(url_for('task.list_task'))
