#https://medium.com/coinmonks/bitcoin-with-python-6595588c2fcf
#actualmente este es el mejor candidato para wallet


from bitcoin import *
def walletCreation():
    
    my_private_key1 = random_key()
    print('Private Key 1: ' + my_private_key1)
    my_public_key1 = privtopub(my_private_key1)
    print('Public Key 1: ' + my_public_key1)
    my_private_key2 = random_key()
    print('Private Key 2: ' + my_private_key2)
    my_public_key2 = privtopub(my_private_key2)
    print('Public Key 2: ' + my_public_key2)
    my_private_key3 = random_key()
    print('Private Key 3: ' + my_private_key3)
    my_public_key3 = privtopub(my_private_key3)
    print('Public Key 3: ' + my_public_key3)
    my_multi_sig = mk_multisig_script(my_private_key1, my_private_key2, my_private_key3, 2,3)
    my_multi_address = scriptaddr(my_multi_sig)
    print('Multi-Address: ' + my_multi_address)
    

def wall2():
    from pywallet import wallet
    # generate 12 word mnemonic seed
    seed = wallet.generate_mnemonic()
    print(seed)
    # create bitcoin wallet
    w = wallet.create_wallet(network="BTC", seed=seed, children=1)
    print(w)



#void main()
#walletCreation()
wall2()
#i = 0
#while (i < 1000):
#    walletCreation()
#    i = i+ 1
