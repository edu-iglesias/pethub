from petpy import Petfinder

PF_LIENT_ID = 'OcmwMa0qVChnuCSLItAu1W2wxSg3P0cEfBaDP2ohOlG1R87pbj'
PF_CLIENT_SECRET = '8KVJumjN7UqmzrrajX9yF8WUXXI0OPoTIhEdIFjq'

def pet_finder_generate_token():
    pf = Petfinder(key=PF_LIENT_ID, secret=PF_CLIENT_SECRET)
    return pf


