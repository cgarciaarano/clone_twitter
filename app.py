from flask import Flask, request, jsonify, render_template
from uuid import uuid1 as randint
from sendgrid import Mail, SendGridClient

app = Flask(__name__)
app.debug = True

tweets = []

@app.route('/', methods=['GET'])
def view_tweets():
  return render_template('index.html', tweets=list(tweets))

@app.route('/tweet', methods=['POST', 'GET'])
def handle_create():
  if request.method == 'POST':
    new_tweet = {'id': str(randint()).split('-')[0], 'text': request.form['tweet']}
    tweets.append(new_tweet)
    return jsonify(new_tweet)
  else:
    return jsonify({"tweets": tweets})


@app.route('/tweet/<id>', methods=['PUT', 'GET', 'DELETE'])
def handle_single_tweet(id):
  for tweet in tweets:
    if tweet['id'] == id:
      if request.method == 'GET':
        return jsonify(tweet)
      elif request.method == 'PUT':
        tweet['text'] = request.form('text')
        return jsonify(tweet)
      else:
        removed = tweet
        tweets.remove(tweet)
        return jsonify(removed)
  return jsonify({"error": "Not found"})

@app.route('/tweet/emailhook', methods=['POST'])
def email_tweet():
  new_tweet = {'id': randint(), 'text': request.form['subject']}
  tweets.append(new_tweet)
  return jsonify(new_tweet)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
