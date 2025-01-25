import os
import pyaes

## Abrindo o arquivo criptografado
file_name = "teste.txt.ransomwareinu"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Removendo o arquivo criptografado
os.remove(file_name)

## Criando o arquivo descriptografado
new_file = "teste.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
