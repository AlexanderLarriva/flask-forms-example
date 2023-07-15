from flask import Flask, render_template, request

from flask_forms.data import generate_users

users = generate_users(100)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN (write your solution here)
# приходит GET (по умолчанию)
@app.route('/users')
def user_list():
    term = request.args.get('term')
    filtered_user_list = []
    if term:
        filtered_user_list = [user for user in users if
                              user['first_name'].lower().startswith(term.lower())] # noqa
        return render_template(
            'users/index.html',
            filtered_user_list=filtered_user_list,
            term=term
        )

    return render_template(
        'users/index.html',
        filtered_user_list=users,
        term=term
    )


# if __name__ == '__main__':
#     app.run()

# END
