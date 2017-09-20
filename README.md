# Bay Area Bike Share

Bay Area Bike Share uses the [SF Bay Area Bike Share](https://www.kaggle.com/benhamner/sf-bay-area-bike-share) dataset. The purpose of the project is to create beautiful graphics of relevant features from the station, trip, weather, and status data.

## Getting Started

Clone this repo and download the [data](https://www.kaggle.com/benhamner/sf-bay-area-bike-share) from Kaggle. Once downloaded, unzip and grab the `station.csv` and move it into a new directory called `data` in the project root.

### Prerequisites

This app was developed in Dash using Python 2.7. It is recommended to use a virtual environment when installing Python packages on your system. Application dependencies in `requirements.txt`.

In the project root:
`pip install -r requirements.txt`

### Installing

To start the app, from the project root:
`python app/bikeshare.py`

Open `localhost:8050` in your browser.

Once loaded, try clicking a City to filter the graph.


## Built With

* [Dash](https://plot.ly/dash/)


## License

This project is licensed under the MIT License.
