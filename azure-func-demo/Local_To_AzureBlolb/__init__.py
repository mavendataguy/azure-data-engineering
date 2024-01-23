import logging

import azure.functions as func


def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 # The below will return the name of the blob created in the Azure container
                 f"Name: {myblob.name}\n"
                 # Here we can write a set of custom steps that needs to be perfomed  
                 f"Blob Size: {myblob.length} bytes")
