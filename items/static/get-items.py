import urllib.request, os, ssl, requests, shutil
from background_task import background
from users.models import Login

@background(schedule=30)
def download_item_images():
    #Ignore SSL warnings and errors
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
        getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context

    url = 'http://rune-nifelheim.com/db/'
    for i in range(512,50000000):
        try:
            response = requests.get(url+'items/img/'+str(i)+'.gif', stream=True)
            response2 = requests.get(url+'items/collection/'+str(i)+'.gif', stream=True)
            print('[GET] ', i, response.raw.status)
            if response.raw.status == 200:
                with open("./icon/"+str(i)+".gif", 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
            if response2.raw.status == 200:
                with open("./collection/"+str(i)+".gif", 'wb') as out_file:
                    shutil.copyfileobj(response2.raw, out_file)
            del response
            del response2
        except() as err:
            pass
