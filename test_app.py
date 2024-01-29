import pytest
from main import app
from fastapi.testclient import TestClient
import pandas as pd

client = TestClient(app)

def test_hello():
    """
    fonction de test de la fonction hello de main.py
    On verifie si en sortie on a bien un status code de 200
    et un json de la forme demandé

    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}


def test_predict():
    """
    fonction de test de la fonction predict de main.py
    On verifie si en sortie on a bien un status code de 200
    et un json de la forme demandé

    """

    url_endpoint = '/predict'
    response = client.get(url_endpoint)
    idx_client = 104819

    assert response.status_code == 200
    
    data_response = response.json()
    list_client = response.json()['list_client_id']

    #verifier qu'on a bien les champs Reponse et Proba_client
    assert 'model' in data_response 
    assert 'list_client_id' in data_response

    #verifier qu'on a en retour les valeurs attendues
    assert data_response['model'] == "lightGBM"
    assert list_client.isin(lidx_client)



def test_predict_get():
    """
    fonction de test de la fonction predict_get de main.py
    On verifie si en sortie on a bien un status code de 200
    et un json de la forme demandé

    """
    url_endpoint = '/predict_get'

    idx_client = 104819
    id = {"sk_id" : str(idx_client)}
    response = client.get(url_endpoint, params = id)

    assert response.status_code == 200

    data_response = response.json()

    #verifier qu'on a bien les champs Reponse et Proba_client
    assert 'Réponse' in data_response 
    assert 'Proba_client' in data_response

    #verifier qu'on a en retour les valeurs attendues
    assert data_response['Réponse'] == "Oui"
    assert data_response['Proba_client'] == '0.1045381722774054'

def test_data_customer():

    """
    fonction de test de la fonction data_customer de main.py
    On verifie si en sortie on a bien un status code de 200
    et un json de la forme demandé

    """

    url_endpoint = '/data_customer'
    idx_client = 104819
    id = {"sk_id" : str(idx_client)}

    response = client.get(url_endpoint, params = id)
    
    assert response.status_code == 200
    
    data_response = response.json()
    info = response.json()['data']
    df_info = pd.DataFrame(info)

    #verifier qu'on a bien les champs Reponse et Proba_client
    assert 'status' in data_response 
    assert 'data' in data_response

    #verifier qu'on a en retour les valeurs attendues
    assert data_response['status'] == "ok"

    assert df_info['CODE_GENDER'] == "1"
