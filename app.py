from flask import Flask
app = Flask(__name__)
import os
@app.route('/')
def hello():
    return 'Green Test Environment!\n'
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
