# File Upload with Azure Functions

![python](https://github.com/epomatti/azure-functions-fileupload/actions/workflows/python-app.yml/badge.svg)

File upload implementation with an Azure Functions app.

<img src="arnold.jpg" width=250/>

### Running it

```sh
# install the dependencies
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt

# start the function
func start

# upload a file
curl -v -F filename='arnold.jpg' -F upload='@arnold.jpg' 'http://localhost:7071/api/upload'
```
