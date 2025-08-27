from Crypto.PublicKey import RSA
from Crypto.Util.Padding import unpad
from Crypto.Cipher import PKCS1_OAEP, AES
import os
import sys

private_key_b = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA0msOiJwzNiQygj42HzBNSLg9yKWai/TqVm69C9b0pK1rAZbY
5iNOn2JgFjFfRfOVDGllNyLdWeugspi1+bj+yj4EVnQr3woUFqG5hFdgpXXmfRsE
ZCT8Ww1Ucp441iyTmJn3KXY3lIFk+oA+9DNo1ooGu3viXd18fnmB4aw7sWZEvhtT
+VusImAbrZgnDAPkyhTrPnjIg0sOVMiOP8oOBBjCX2UzqFxNltjM69BfzteuTcDM
L3DEr44fTa7gcCjpz/d8jyexolEFQIIDiWwdoXCek91nzEJAqBHETYF502YMC9TT
iFsMr1wCvM98lXCWb+y1Mq2yveGxH4CQOV3RlQIDAQABAoIBABGPXCDj8jUmO63Z
XcBoEkcLkyJjyZw89fJ9Hts2VufITioNie/YyfasqcqoV6RZkdp9kDQT/YeDzb8h
1evvd5nup4OEgeXE7EzANeB4v0jHqFLP9qOZ35KEsAO5txIOmcmuLa2A314OF1x9
Z+OOx8TBs5KhYdCGC53ta3ynGDszYCIQucaEKZvw1CYvcnDnqBYblrMIO6Tj4EHa
QTFe6C6LUfCENIe+2tEQuBmpa/gaBs2aT2hxxEk/CqakupRcbyfbNMxgyjYNgPJt
lOCq0LVeg801/uXaZZLY5M/SMgmrwKKfFlOk7VMXBqIHf+E60DkbzL2HSvyP96d8
2KlqvtECgYEA2qECA27rOBsj+wIu4mfErJnyHvwavQz9mivZbk0dOXhv/O9pexHG
RlOvXu9jr1KyBXRnkLdAT0Ehp3IPdIPDRmVI+vhufqLUwLfc5RylhQA7EQNjNpdh
oTt+n5JmqlHtSP4cXx5pyNp1gPtKQ1cLyNJrRWMSn0TzgTKKCkbXLpECgYEA9mLB
KSol7i2qnJdBl9klat4oHplckuSRSzdinosxCNrVXhVMowAwOEvsv4SY5IKPVMb+
rvFIbMV7Op0hDiQey4FRwyZh1Fl/SWqm6BfzwlyCXgJqV8hgWedx8CUKaUkCO12W
JcRZq3Y9bdNBDaHTlhIN6X6CxU+sDN6C4RGNPMUCgYEAqZSNzT/x75kNtZsh5rd6
lC7s4R/HVbCH3Vf51Va3Pmau5tCFTtKgqtgqhUbGWa2ZLCX4VwXtOgxZIFqWple1
1hqmGxUsD8oZoEp9arFnqdxd9HpeMHAHaFqPgxK5046ssRt5wkYC46qfziYcmlMg
burYDgAk56lB/4rGC+aa7iECgYEAsnKwCAp40lrM2QFMBpjFWvNwB0l4HQPin6GL
kdyqNQmZw7yVdvEp+3wyCjwVKFvPR82gpEAo/m7BY6BuUnmivC37c+YWsN/pKtlN
7Yd7iufJnCEPuGhuMG9KvG13bu3r6edMWiot79uBfkulMCRmxKhq3xQ7zoB30hJO
pIg7zSkCgYEAumrwy2uo4PBZjDDxHUbTso0N7HWFz8HzoALvN1W8UQ2AkhRh6R2J
q8uHQ6meFQqTt+WCb8/XsQa9kcSyIQXEsOGesvyL3trRZsTSBNZMTcxwRQFflbmE
bD5yKng/nf3HJz3LHHx3dzuptpnRfYK8hgRHok1BdBO2BNhPT93HOro=
-----END RSA PRIVATE KEY-----"""

if len(sys.argv) < 2:
    print("please input a file")
    

private_key = RSA.import_key(private_key_b)

shared_key_location = sys.argv[1]

with open(shared_key_location, "rb") as f:
    encrypted_shared_key = f.read()

cipher_rsa = PKCS1_OAEP.new(private_key)
shared_key = cipher_rsa.decrypt(encrypted_shared_key)

with open("DecryptedSharedKey", "wb") as f:
    f.write(shared_key)
