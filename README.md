# FlaskApiSaveImg

FlaskApiSaveImg is a simple example of how to save an image through Flask and Flask_restful including the Docker file used to make it work out of the box based on the implementation of "[File Upload in Restful Flask](https://github.com/flask-restful/flask-restful/issues/485)".

## Usage

In order to use the API with docker the first step is to build the image with the next command, executing it from the code folder.

```bash
docker build -t [name_for_image] .
```

Then use the image with this last command.

```bash
docker run --rm -v [project_route]:/app --name [name_for_container] -p 5001:5001 [name_for_image]
```
