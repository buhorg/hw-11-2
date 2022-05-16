import utils
from flask import Flask, render_template


candidate_list = utils.get_candidates_list('static/candidates.json')
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', candidate_list=candidate_list)


@app.route('/candidate/<int:uid>')
def profile(uid):
    candidate = utils.get_person_by_id(uid, candidate_list)
    return render_template("candidate.html", candidate=candidate)


@app.route('/search/<uid>')
def profile_name(uid):
    candidates = utils.get_persons_by_name(uid, candidate_list)
    return render_template("search.html", candidates=candidates, uid=uid, len_list=len(candidates))


@app.route('/skill/<uid>')
def profile_skill(uid):
    candidates = utils.get_persons_by_skill(uid, candidate_list)
    return render_template("skill.html", candidates=candidates, uid=uid, len_list=len(candidates))


if __name__ == '__main__':
    app.run(debug=True)

