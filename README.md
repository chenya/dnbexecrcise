# dnbexecrcise

### How to run

Enter to the cloned folder and than type the commands:
```bash
docker image build -t dnbexecrcise .     
docker container run -p 8000:8000 -e exercise_toekn=<your_token> dnbexecrcise
```
* The token is mandatory
### Choices made in the execrcise:
1. Project structure is divided to '_src_' folder and '_tests_' folder following the recommended in _pytest_ [best practices](https://docs.pytest.org/en/7.2.x/explanation/goodpractices.html)
    
1. The exercise made with _FastAPI_ web framework and _uvicorn_ as the server
1. For scarping the _selectolax_ is used due to a simpler implementation than _Beautiful Soup_
1. The _httpx_ is used for the asynchronous http requests
1. _pytest_ for running the unittests also added a script file for testing multiple request on different stock symbols.


