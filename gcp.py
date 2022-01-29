def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_args = request.args
    if request.args and "value1" in request_args:
        number = request_args["value1"]
        return {'name' : number} 
    else:
        return f'Can not handle the number provided!'
