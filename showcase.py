from logdriver.unsecured import UnsecuredDriver
from logdriver.secured import SecuredDriver

# udriver = UnsecuredDriver("driver-client", "http://localhost:8000")

# reference_id = udriver.log({"message": "Hello world!", "data": {"foo": "bar"}})
# print(f"{reference_id=}")
# # reference_id='64da4dbc40dd88d5de000729'

# print(f"{udriver.get(reference_id)=}")
# # udriver.get(reference_id)={'id': '64da4dbc40dd88d5de000729', 'service': 'driver-client', 'level': 'INFO', 'payload': {'message': 'Hello world!', 'data': {'foo': 'bar'}}, 'date': '2023-08-14T16:52:28'}

# print(f"{udriver=}")
# # udriver=UnsecuredDriver(service_name=driver-client, url=http://localhost:8000)

# print(f"{udriver.today()=}")
# # udriver.today()={'limit': 100, 'offset': 0, 'logs': [{'id': '64da4dbc40dd88d5de000729', 'service': 'driver-client', 'level': 'INFO', 'payload': {'message': 'Hello world!', 'data': {'foo': 'bar'}}, 'date': '2023-08-14T16:52:28'}], 'total_count': 1}

# print(f"{udriver.today(offset=0, limit=1)=}")
# # udriver.today(offset=0, limit=1)={'limit': 1, 'offset': 0, 'logs': [{'id': '64da4dbc40dd88d5de000729', 'service': 'driver-client', 'level': 'INFO', 'payload': {'message': 'Hello world!', 'data': {'foo': 'bar'}}, 'date': '2023-08-14T16:52:28'}], 'total_count': 1}

# print(f"{udriver.today(offset=0, limit=1, service='driver-client', level='INFO')=}")
# # udriver.today(offset=0, limit=1, service='driver-client', level='INFO')={'limit': 1, 'offset': 0, 'logs': [{'id': '64da4dbc40dd88d5de000729', 'service': 'driver-client', 'level': 'INFO', 'payload': {'message': 'Hello world!', 'data': {'foo': 'bar'}}, 'date': '2023-08-14T16:52:28'}], 'total_count': 1}

sdriver = SecuredDriver("driver-client", token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmUiOjE2OTQ1NTc4NDcuMTgxMzc1LCJzZXJ2aWNlX25hbWUiOiJiYW5raW5nIiwiYWNjZXNzIjoxLCJhY2Nlc3NfY29kZSI6NDA2ODU5M30.Rkbs6G-MFfZd3ZUNL353_IhhtzQ72mjBt1OxypngvQk")

reference_id = "64da73b4086e81d4fb269a10"#sdriver.log({"message": "Hello world!", "data": {"foo": "bar"}})
print(f"{reference_id=}")
print(f"{sdriver.get(reference_id)=}")