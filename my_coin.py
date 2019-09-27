#!usr/bin/env python3

'''
__author__ = 'abba y abdullahi,lastloade@gmail.com'
__copyright__ ' copyright (c) 2019 by ay abdullahi'

'''

from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair


user1, user2 = generate_keypair(), generate_keypair()
bdb = BigchainDB(
    'https://url',
    headers={'app_id': 'da9c76b69j53',
             'app_key': '34f1acaf209503732a3521afb184560a'})
Test_asset = {
    'data': {
        'test22': {
            'serial_number': 'abcdfg1234128904',
            'manufacturer': 'danmalam'
        },
    },
}
Test_asset_metadata = {
    'country': 'nigeria'
}
prepared_creation_tx = bdb.transactions.prepare(
    operation='CREATE',
    signers=user1.public_key,
    asset=Test_asset,
    metadata=Test_asset_metadata
)
fulfilled_creation_tx = bdb.transactions.fulfill(
    prepared_creation_tx,
    private_keys=user1.private_key
)

sent_creation_tx = bdb.transactions.send_commit(fulfilled_creation_tx)
print('create')
print(sent_creation_tx)
txid = fulfilled_creation_tx['id']

b = bdb.transactions.get(asset_id=txid)
print('b')
print(b)
b =  {'asset': {'data': {'bicycle': {'manufacturer': 'danmlam', 'serial_number': 'abcdfg1234128904'}}}, 'id': 'd7fb62d90f1c67861e520cffeb6e7c6a62ed3b7ba335ebfc784c8baba46592a0', 'inputs': [{'fulfillment': 'pGSAIIg31Ki3DZbYOAZMnBmVgV0-hfy_xeDiz9d83I6jBmxagUBKbgqZksjvhMAeyGPSHNDnIjBqmgM8qVdy641Z0PQNB27dbZNYsnGac2fgzkZxXyDx6YqBx1WNCG-wT8BCTokL', 'fulfills': None, 'owners_before': ['AAjpnRqzJRhS8xpQsXNLV1hdaB8gUwgE41qJhinfGtqw']}], 'metadata': {'planet': 'earth'}, 'operation': 'CREATE', 'outputs': [{'amount': '1', 'condition': {'details': {'public_key': 'AAjpnRqzJRhS8xpQsXNLV1hdaB8gUwgE41qJhinfGtqw', 'type': 'ed25519-sha-256'}, 'uri': 'ni:///sha-256;oFneJQzJm7Nq5k786xXdDRUCd-48WFQ1HLlkyojar3M?fpt=ed25519-sha-256&cost=131072'}, 'public_keys': ['AAjpnRqzJRhS8xpQsXNLV1hdaB8gUwgE41qJhinfGtqw']}], 'version': '2.0'}
bdb = BigchainDB(
    'https://url',
    headers={'app_id': 'da9c76b69j53',b '2523' , 'app_key': '34f1acaf209503732a3521afb184560a'})

             

b = block_height = bdb.blocks.get(txid='d7fb62d90f1c67861e520cffeb6e7c6a62ed3b7ba335ebfc784c8baba46592a0')
print('Block Number')
print(b)
