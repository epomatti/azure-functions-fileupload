# File Upload with Azure Functions

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
