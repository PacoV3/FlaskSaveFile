# flask-file-api

flask-file-api is a simple example of how to save an image through Flask and Flask_restful including the Docker file used to make it work out of the box based on the implementation of "[File Upload in Restful Flask](https://github.com/flask-restful/flask-restful/issues/485)".

## Implementation

In order to use the API with docker the first step is to build the image with the next command, executing it from the code folder.

```bash
docker build -t [name_for_image] .
```

Then use the image with this last command.

```bash
docker run --rm -v [project_route]:/app --name [name_for_container] -p 5001:5001 [name_for_image]
```

## Usage

For examples on how to use the app, here is a way to test it with [curl](https://curl.se/docs/manpage.html) (you'll need to have the files in the route you are executing it).

For a single file you can execute:

```bash
curl -X POST -F files=@'test.png' http://127.0.0.1:5001/upload
```

For multiple files:

```bash
curl -X POST -F files=@'test.png' -F files=@'pc.png' http://127.0.0.1:5001/multi_upload
```
