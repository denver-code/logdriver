# LogDriver Python Library

The LogDriver  Python Library is a tool that allows you to easily send and retrieve logs from a [log server](https://github.com/denver-code/logunit). It provides a user-friendly interface to interact with the log server's API endpoints. This library is particularly useful for applications where security is not a primary concern, as it lacks authentication and encryption mechanisms.

## Getting Started

To start using the LogDriver Python Library, you can install it directly from the GitHub repository. Follow these steps:

1. **Clone the Repository**: Clone the LogDriver Unsecured repository to your local machine using the following command:

```bash
git clone https://github.com/denver-code/logdriver.git
 ```

2. **Move the logdriver** folder to your project's root or utils directory.

3. **Import the library**: Import the library into your project using the following command:

```python
import logdriver
```


## Unsecured LogDriver usage

1. **Initialize the UnsecureLogDriver**: Initialize the LogDriver using the following command:

```python
from logdriver.unsecured import UnsecuredDriver

udriver = UnsecuredDriver("driver-client", "http://localhost:8000")
```

2. **Send a log**: Send a log to the LogDriver using the following command:

```python
udriver.log({"message": "Hello world!", "data": {"foo": "bar"}})
```

3. **Retrieve log by reference**: Retrieve logs from the LogDriver using the following command:

```python
reference_id = udriver.log({"message": "Hello world!", "data": {"foo": "bar"}})
udriver.get(reference_id)
```

4. **Retrieve today's logs**: Retrieve logs from the LogDriver using the following command:

```python
udriver.today()
```

5. **Log query filters**: Retrieve logs from the LogDriver using the following command:

```python
udriver.today(offset=0, limit=1, service='driver-client', level='INFO')
```