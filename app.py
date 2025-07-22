from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Fixed credentials
USERNAME = "admin"
PASSWORD = "123"

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USERNAME and password == PASSWORD:
            return redirect('/home')
        else:
            error = "❌ Invalid username or password."
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/goods_services')
def goods_services():
    return render_template('goods_services.html')

@app.route('/customer_care', methods=['GET', 'POST'])
def customer_care():
    ai_reply = None
    if request.method == 'POST':
        question = request.form.get('question')
        ai_reply = f"🤖 AI Reply: I understand your question '{question}', and we’ll get back with helpful advice soon!"
    return render_template('customer_care.html', ai_reply=ai_reply)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    message = None
    if request.method == 'POST':
        rating = request.form.get('rating')
        comment = request.form.get('comment')
        print(f"User rated: {rating}, Comment: {comment}")
        message = "✅ Thank you for your feedback!"
    return render_template('feedback.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
