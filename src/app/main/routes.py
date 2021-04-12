
#from __main__ import app

from app.main.service import bp



#@app.route('/test', methods=['GET', 'POST'])
#@login_required
def test():
    return "{test:'Test123'}"
