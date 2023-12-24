from datetime import datetime  
import json  
import os  
import random  
import uuid  


def get_payment():  
    return {  
        'url': os.getenv("WEBHOOK_ADDRESS", ""),  
        'webhookId': uuid.uuid4().hex,  
        'data': {  
            'id': uuid.uuid4().hex,  
            'payment': f"PY-{''.join((random.choice('abcdxyzpqr').capitalize() for i in range(5)))}",  
            'event': random.choice(["accepted", "completed", "canceled"]),  
            'created': datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),  
        }  
    }  