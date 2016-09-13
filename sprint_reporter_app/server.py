from flask import Flask, render_template, redirect, url_for, request
from sprint import *

app = Flask(__name__)
app.config.from_object(__name__)

#csatlakozik az adatbázishoz, csinál egy táblát ha még nincs ilyen, bezárja
def init_db():
    db.connect()
    db.create_tables([Sprint], safe=True)
    db.close()


@app.route('/', methods=['GET'])
def start():
    return render_template('start.html')


@app.route('/new_sprint', methods=['GET', 'POST'])
def new_sprint():
    if request.method == 'POST':
        title = request.form['title']
        story = request.form['story']
        criteria = request.form['criteria']
        value = request.form['value']
        estimation = request.form['time']
        status = request.form['status']
        Sprint.create(
            title=title,
            user_story=story,
            acceptance_criteria=criteria,
            business_value=value,
            estimation=estimation,
            status=status
        )
        return redirect(url_for('list'))
    else:
        return render_template('new_sprint.html', data=False)


@app.route('/new_sprint/<sprintname>', methods=['POST'])
def update_sprint(sprintname):
    row = Sprint.select().where(Sprint.sprint_id == sprintname).get()
    return render_template('new_sprint.html', data=row)


@app.route('/update', methods=['POST'])
def update():
    number = request.form['sprint_id']
    row_update = Sprint.select().where(Sprint.sprint_id == number).get()
    title = request.form['title']
    story = request.form['story']
    criteria = request.form['criteria']
    value = request.form['value']
    estimation = request.form['time']
    status = request.form['status']
    row_update.title = title
    row_update.user_story = story
    row_update.acceptance_criteria = criteria
    row_update.business_value = value
    row_update.estimation = estimation
    row_update.status = status
    row_update.save()
    return redirect(url_for('list'))


@app.route('/list', methods=['GET'])
def list():
    all_data = Sprint.select()
    return render_template('list.html', sprints=all_data)

@app.route('/delete', methods=['POST'])
def delete_sprint():
    number = request.form['sprint_id']
    row_to_delete = Sprint.select().where(Sprint.sprint_id == number).get()
    row_to_delete.delete_instance()
    return redirect(url_for('list'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
