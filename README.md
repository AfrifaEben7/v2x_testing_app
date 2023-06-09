# V2X Testing App For For Proving Ground Use.

The V2X Testing App is a Python application that utilizes PyQt5 and pandas libraries for proving grounds testing. It integrates with Esmini, a simulation platform. This README provides instructions on how to install, set up, and run the application.

## Dependencies

Make sure you have the following dependencies installed:

1. PyQt5
1. pandas
1. matplotlib
1. Esmini (Please refer to the [Esmini documentation](https://esmini.github.io) for installation instructions specific to your system. (Building recommended))

## Note
  - Cloning this project will clone Esimi as well (use this command: git clone --recurse-submodules https://github.com/AfrifaEben7/v2x_testing_app.git).
  - I recommend building Esmini for your system.
  
## Setup

1. Clone the repository and navigate to the project's root directory.
1. Build Esmini.
1. Place the contents of the `scenario_examples` folder into the `esmini/resources/xosc` directory (`cp -r scenario_examples/* esmini/resources/xosc`). This step is necessary for demo purposes.
1. Ensure that both the `code` and `esmini` folders are in the same parent folder (ie, esmini should be in the root folder).


## Running the Application

To run the V2X Testing App, follow these steps:

1. Open a terminal or command prompt.
1. Navigate to the project's root directory.
1. Run the following command: `python code/pro_test.py`.
1. In the application's GUI, select a scenario file from the `esmini/resources/xosc` directory. Choose any of the moved `.xosc` files.
1. Click the "Start" button to initiate the scenario.
1. Press the "Esc" key to end the scenario.

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

