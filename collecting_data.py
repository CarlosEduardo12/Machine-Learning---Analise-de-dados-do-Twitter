import tweepy
import csv
import time

consumer_key = "v5DSx10na0FX64T8b1FHGBLP9"
consumer_secret = "eoSYXMer6lxqhkW4wgrTVDULKdqP8K0981MoLCGY79rRM5iOkx"
acess_token = "51471314-71TXLlEwCmJgwDCFriq5fgBJZHaSCuVr4OaINISTE"
acess_token_secret = "gmfYRqzCjpmX2U8NfVkBC8hhVcXhjipk7YIkCKKwGzvQG"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acess_token, acess_token_secret)

api = tweepy.API(auth)

arq = csv.writer(open("Base_teste.csv", "w", encoding="utf-8"))
arq2 = (open('Base_teste_json.json', 'w', encoding="utf-8"))

row = []

statuses = tweepy.Cursor(api.search, q='Eleições', since='2018-08-01', until='2018-09-02', lang='pt-br').items()

while True:
    try:
        status = statuses.next()
        row = str(status.user.screen_name), str(status.created_at), str(status.text), status.geo
        arq.writerow(row)

        arq2.write(str(status))
        arq2.write("\n")


    except tweepy.TweepError:
        print('Wait 15 minutes...')
        time.sleep(60*15)
        continue
    except StopIteration:
        print('Fim da coleta de dados')
        break
