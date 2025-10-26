Homework notebooks for the Machine Leraning Zoomcamp course (2025 cohort)

Links for the course:
- https://courses.datatalks.club/ml-zoomcamp-2025/
- https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/cohorts/2025


# Useful commands (for homework 5)

To run the app (with auto-reload):
`uvicorn predict:app --host 0.0.0.0 --port 9696 --reload`

## Docker commands
To build Docker image:
`docker build -t churn_prediction .`

To run in interactive mode:
`docker run -it --rm -p 9696:9696 churn_prediction`