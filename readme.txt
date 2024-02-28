I am writing this file to provide some information regarding the project.
As I have not been directed to use any credentials. So I developed this project to test this project on url which is mentioned below:-
 1. https://in.linkedin.com/in/saurav-soni-94142216?trk=people-guest_people_search-card


API endpoint :-  https://127.0.0.1:8000/api/profile/
curl request :-  curl -H 'Content-Type: application/json' -X POST -d '{"profile_url": "https://in.linkedin.com/in/saurav-soni-94142216?trk=people-guest_people_search-card"}' http://127.0.0.1:8000/api/profile/



Step to test the project on local server:-
1. install the requirements
2. run the local server
3. send a curl request using the above curl request
4. results will be returned in json format