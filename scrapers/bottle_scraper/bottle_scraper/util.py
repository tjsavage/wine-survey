import urllib.request
import mimetypes

def is_image_url_valid(image_url):

    try:
        req = urllib.request.Request(image_url)
        with urllib.request.urlopen(req) as resp:
            if not resp.code in range(200, 209):
                print("code %d" % resp.code)
                return False
            if int(resp.headers.get('content-length')) < 1000:
                print("short content length")
                return False
        
        mimetype,encoding = mimetypes.guess_type(image_url)
        if not mimetype:
            print("not mimetype")
            return False
        if not mimetype.startswith('image'):
            return('not mimetype.startswith %s' % mimetype)
        return True
    except Exception as e:
        print("Exception")
        print(e)
        return False