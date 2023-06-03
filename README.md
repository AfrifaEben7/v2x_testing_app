# V2X Testing App For For Proving Ground Use.

The V2X Testing App is a Python application that utilizes PyQt5 and pandas libraries for testing V2X scenarios. It integrates with Esmini, a simulation platform. This README provides instructions on how to install, set up, and run the application.

## Dependencies

Make sure you have the following dependencies installed:

1. PyQt5
2. pandas, matplotlib
3. Esmini (Please refer to the [Esmini documentation](https://esmini.github.io) for installation instructions specific to your system.(Building recommended))

## Setup

1. Clone the repository and navigate to the project's root directory.
2. Place the contents of the `scenario_examples` folder into the `/esmini/resources/xosc` directory. This step is necessary for demo purposes.
3. Ensure that both the `v2x_testing_app` and `esmini` folders are located in the same parent folder.

## Running the Application

To run the V2X Testing App, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project's root directory.
3. Run the following command: `python pro_test.py`.
4. In the application's GUI, select a scenario file from the `/esmini/resources/xosc` directory. Choose any of the moved `.xosc` files.
5. Click the "Start" button to initiate the scenario.
6. Press the "Esc" key to end the scenario.

## Contributing

Contributions to the V2X Testing App are welcome! If you would like to contribute, please follow these guidelines:

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Commit your changes with descriptive commit messages.
5. Push your branch to your forked repository.
6. Open a pull request with a clear explanation of your changes.

Please ensure that your contributions adhere to the code style guidelines and best practices.

## License

The V2X Testing App is distributed under the [MIT License](LICENSE).

## Resources

For additional resources and documentation, please refer to the following:

- [Esmini Documentation](https://esmini.github.io)
- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [pandas Documentation](https://pandas.pydata.org/docs/) 
- [matplotlib Documentation](https://matplotlib.org/)

