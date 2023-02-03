# Virtual Orb

This project includes:
1) a virtual Orb device that simulates status report and signups by sending POST requests to a configurable address
2) a mock-server that is used to test the virtual orb device


The mock-server is just a Flask server that implements 2 API endpoints:
- signup => to test the signup functionality of the virtual orb
- status report => to test the status report functionality of the virtual orb

The png images that are received by this mock-server are saved in `./mock_server/stored-irises` folder.

To launch the virtual orb app locally, from `orb_device` folder please run:
`./orb/run_orb.sh`. This will build a docker image for the Orb device and start the container. 

To also launch the mock-server locally, from `orb_device` folder  please run:
`./mock_server/run_mock_server.sh`. This will simply run the mock-server locally in order to test the orb device.
