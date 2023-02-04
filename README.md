# Virtual Orb

This project includes:
1) a virtual Orb device that simulates status reports and signups by sending POST requests to a configurable address
2) a mock-server that is used to test the virtual orb device.

The mock-server is just a Flask server that implements 2 API endpoints:
- signup => to test the signup functionality of the virtual orb
- status report => to test the status report functionality of the virtual orb

The png images that are received by this mock-server are saved in `./orb_device/mock_server/stored_irises` folder in the container.

The virtual orb device simulates a new signup by sending a POST request to the target server with a png image of an iris.
The image is randomly picked from a pool of 6 iris pictures found on Google and saved in `./orb_device/orb/irises` folder.

To launch the whole project, from `orb_device` folder please run `docker-compose up --build`. This will build the images and start the containers of both the orb and the mock-server.

To launch the virtual orb app locally, from `orb_device` folder please run `./orb/run_orb.sh`. This will build a docker image of the Orb device and start the container. 

To launch the mock-server locally, from `orb_device` folder please run `./mock_server/run_mock_server.sh`. This will simply run the mock-server locally, it could be useful in order to test the orb device.

To manually run the unit tests for the orb device, from `orb_device` folder please run `pytest orb/tests.py`. Please notice that the tests also run as part of the orb image build.

