# Automatic Website Creation

The goal of this project is to automatically generate a website from a scene folder that is produced by the MobileLighting app. Once the program is successfully executed, several HTML files will be generated, with the main page named home.html. There will also be a new folder named as the scene and contain all images displayed on the website. Right now, this program is designed for macOS and only works on macOS. However, it could be changed to adapt Windows system. Find more details in "Running the tests" section

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

You should have Python running on your computer in order to execute this program. 

The Python program uses yattag(http://www.yattag.org/) to make it easier to generate HTML files. In order to install yattag on your computer, it is suggested that you use pip to do so with this command:

```
pip install yattag
```

More details about installing yattag can be found here:http://www.yattag.org/download-install. This includes a way to install yattag without using pip.

You should also have ImageMagick(http://www.imagemagick.org/script/index.php) installed on your computer before you try to run the program since it uses ImageMagick to resize images and convert formats. Here is a link to the instrunctions to download ImageMagick onto your own computer: http://www.imagemagick.org/script/download.php. If you are not familiar with ImageMagick, here is a brief guide to what it can do and how to use it: http://www.imagemagick.org/Usage/. However, this is not necessary for this project since all ImageMagick commands are already written.



### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
